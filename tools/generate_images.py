#!/usr/bin/env python3
"""
Waeyuk Image Studio — مولّد صور بالطراز الهولوجرامي (Holographic Glass style)

Generates tool/test images via Cloudflare Workers AI (Flux-1-Schnell),
then exports them to the platform spec: 560x560 WebP (quality 85).

Usage:
  export CLOUDFLARE_ACCOUNT_ID="your-account-id"
  export CLOUDFLARE_API_TOKEN="your-api-token"

  # Single image:
  python3 generate_images.py --name depression-test --prompt "..." --outdir out/

  # Batch from a JSON file ({name: prompt, ...}):
  python3 generate_images.py --batch prompts.json --outdir out/

Requirements:
  pip install Pillow

Security:
  Credentials are read from environment variables ONLY.
  Never hardcode tokens in files, logs, or commits.
"""

import argparse
import base64
import io
import json
import os
import sys
import time
import urllib.request
from PIL import Image

API_URL = "https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/black-forest-labs/flux-1-schnell"
OUTPUT_SIZE = (560, 560)


def resolve_credentials() -> tuple[str, str]:
    account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "").strip()
    api_token = os.environ.get("CLOUDFLARE_API_TOKEN", "").strip()
    if not account_id or not api_token:
        sys.exit(
            "Missing credentials. Set CLOUDFLARE_ACCOUNT_ID and CLOUDFLARE_API_TOKEN "
            "as environment variables (never hardcode them in files)."
        )
    return account_id, api_token


def generate_image(account_id: str, api_token: str, prompt: str) -> bytes:
    """Call Flux-1-Schnell and return raw image bytes."""
    url = API_URL.format(account_id=account_id)
    body = json.dumps({"prompt": prompt}).encode("utf-8")

    request = urllib.request.Request(url, data=body, method="POST")
    request.add_header("Authorization", f"Bearer {api_token}")
    request.add_header("Content-Type", "application/json")

    with urllib.request.urlopen(request, timeout=120) as response:
        payload = json.loads(response.read().decode("utf-8"))

    result = payload.get("result") or {}
    if "image" in result:
        return base64.b64decode(result["image"])

    message = (payload.get("errors") or [{}])[0].get("message", "Unknown error")
    raise RuntimeError(f"Generation failed: {message}")


def export_webp(raw: bytes, out_path: str) -> None:
    """Resize to 560x560 (LANCZOS) and save as WebP q85 — platform spec."""
    image = Image.open(io.BytesIO(raw))
    image = image.resize(OUTPUT_SIZE, Image.LANCZOS)
    image.save(out_path, "WEBP", quality=85)


def run(items: list[tuple[str, str]], outdir: str) -> None:
    account_id, api_token = resolve_credentials()
    os.makedirs(outdir, exist_ok=True)

    results: dict[str, bool] = {}
    for name, prompt in items:
        out_path = os.path.join(outdir, f"{name}.webp")
        print(f"Generating {name} ...", flush=True)
        try:
            raw = generate_image(account_id, api_token, prompt)
            export_webp(raw, out_path)
            print(f"  OK  {out_path}")
            results[name] = True
        except Exception as exc:  # noqa: BLE001 — report and continue batch
            print(f"  FAIL {name}: {exc}")
            results[name] = False
        time.sleep(1)  # polite rate limiting

    ok = sum(results.values())
    print(f"\n=== Summary: {ok}/{len(results)} succeeded ===")
    failed = [n for n, good in results.items() if not good]
    if failed:
        print("Failed:", ", ".join(failed))
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Waeyuk holographic-glass image generator")
    parser.add_argument("--name", help="tool/test slug (file name without extension)")
    parser.add_argument("--prompt", help="full holographic-glass prompt text")
    parser.add_argument("--batch", help="JSON file: {\"slug\": \"prompt\", ...}")
    parser.add_argument("--outdir", default="out", help="output directory (default: out/)")
    args = parser.parse_args()

    if args.batch:
        with open(args.batch, encoding="utf-8") as handle:
            batch = json.load(handle)
        items = [(str(k), str(v)) for k, v in batch.items()]
    elif args.name and args.prompt:
        items = [(args.name, args.prompt)]
    else:
        parser.error("provide --name + --prompt, or --batch <prompts.json>")

    run(items, args.outdir)


if __name__ == "__main__":
    main()
