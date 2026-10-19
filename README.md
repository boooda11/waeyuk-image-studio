# Waeyuk Image Studio 🎨 — الطراز الهولوجرامي (Holographic Glass)

الاستوديو البصري الرسمي لتوليد **صور الأدوات والاختبارات النفسية** في منصة [وعيك](https://waeyuk.com) — مطبّق على 646 صورة إنتاجية بالفعل، ومنقّح بفحص رؤية (Vision QA) حقيقي.

كل صورة = مشهد كوني داكن فيه جسد زجاجي هولوجرامي شفاف على منصّة نيون متوهجة بوضعية وعنصر ضوئي رمزي ممثّلين المفهوم النفسي. هوية موحّدة، صورة بلا نصوص، إحساس رحيم هادئ.

![مثال] نموذج الصورة: جسد زجاجي أزرق شفاف جاثٍ منحنيًا فوق منصّة نيون زرقاء متحدة المركز، يختزن بين ذراعيه كرة ضوء ثقيلة تمثّل الحزن، على خلفية كونية داكنة بنجوم وسُدم.

---

## 📦 محتويات المستودع

| الملف | الجمهور | الوظيفة |
|---|---|---|
| `SKILL.md` | 🤖 الوكلاء (Agents) | Skill بصيغة OpenCode/Claude — انسخها لمجلد skills عندك ووِكيلك يشتغل مباشرة |
| `STYLE-GUIDE.md` | 👤 البشر | الدليل الكامل: تشريح الصورة، علم اللون النفسي، قاموس الرموز، الفحص |
| `PROMPTS.md` | 🌍 الكل | 41 برومبت إنتاجية فعلية جاهزة — مثال حي لكل الحالات |
| `tools/generate_images.py` | 🤖 الوكلاء | سكربت توليد عبر Cloudflare Flux — تحويل تلقائي 560×560 WebP |

> ⚠️ **لا توجد أي توكن أسرار في هذا المستودع.** السكربت يقرأ بيانات الاعتماد من متغيرات البيئة حصريًا.

---

## 🚀 الاستخدام السريع

### لذوي التطبيق (لك كـ وكلاء)
انسخ `SKILL.md` إلى:
```
~/.agents/skills/waeyuk-image-studio/SKILL.md   # global (OpenCode)
# or
<project>/.opencode/skills/waeyuk-image-studio/SKILL.md   # per project (OpenCode)
```
ثم اسأل الوكيل: «ولّد صورة لأداة X بالطراز الهولوجرامي».

### سطر الأوامر مباشرة (بدون وكيل)
```bash
export CLOUDFLARE_ACCOUNT_ID="your-account-id"
export CLOUDFLARE_API_TOKEN="your-api-token"

# صورة واحدة
python3 tools/generate_images.py \
  --name my-tool \
  --outdir out/ \
  --prompt "3D holographic translucent glass-like figure standing determined..."

# دفعة كاملة من ملف JSON
python3 tools/generate_images.py --batch prompts.json --outdir out/
```
يتطلب `pip install Pillow`.

### برومبت واحد جاهز
انسخ أي برومبت من `PROMPTS.md` لـ Midjourney / DALL·E / SDXL — القالب مكتوب بصيغة عامة توافق كل المولّدات (راجع جدول الحمولة في `STYLE-GUIDE.md` §8).

---

## 🧬 جوهر النمط في 20 ثانية

1. **الجسد**: `3D holographic translucent glass-like figure` بنسب بالغ متسقة
2. **الوضعية**: تمثل الحالة (انحناء = اكتئاب، يدين على الوجه = ذعر…)
3. **الرمز**: عنصر ضوئي متصل بالجسد (`heavy weight pressing on chest`, `swirling thoughts`)
4. **الخلفية**: `dark cosmic space background with stars and nebula`
5. **المنصّة**: `glowing circular platform with {color} neon rings beneath the figure`
6. **الباليتة**: لونان عاطفيان (`futuristic sci-fi aesthetic, deep blues`)
7. **الختام**: `no text, ethereal glass-like human form`

القاعدة الذهبية: **الرمز واحد، متصل بالجسد، واضح المعنى** — لا عناصر عائمة ولا فوضى.

---

## 📐 مواصفات المعالجة (كما في إنتاج وعيك)

- الموديل: Cloudflare Workers AI `@cf/black-forest-labs/flux-1-schnell` (4 خطوات)
- الناتج: **560×560 WebP جودة 85** (Resize `LANCZOS`)
- التسمية: **slug الأداة** `teen-depression-test.webp`
- الاستخدام: بطاقات الأدوات والاختبارات في المنصة

---

## 📝 دروس من فحص الرؤية الفعلي (Real Vision QA)

أخطاء حقيقية مرّت في الإنتاج وصارت قواعد إلزامية:
1. خلفية سوداء خامدة **بلا نجوم** → أضف صراحة `with stars and nebula`
2. جسد بنسب **طفولية** في برومبت القلق → راقب `adult proportions`
3. **عناصر دخيلة** (أشياء طائر داخل خيوط الأفكار!) → رجّع التوليد
4. لون المفهوم **ما نزلتش للمُصدّد** → اذكر تنك اللون بلغة الأدوات
الحل: معاينة القايمة في `STYLE-GUIDE.md` §7 قبل قبول أي صورة.

---

## 📄 License (MIT)

المستودع حر — الاستخدام والتعديل وإعادة التوزيع بأي غرض (بما فيه التجاري)، دون أي ضمانات. راجع `LICENSE`.

## 🙏 About

تطوير وبناء: منصة **وعيك** (waeyuk.com) — الوكيل النفسي العربي الأول، مبني على أدوات التنمية الإنسانية.
النمط مبني على 646 صورة إنتاجية، ونُقّح عبر فحص رؤية فعلي.
