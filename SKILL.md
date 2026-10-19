---
name: waeyuk-image-studio
description: استوديو توليد صور "الطراز الهولوجرامي" — النمط البصري الرسمي لصور الأدوات والاختبارات النفسية في منصة وعيك (waeyuk.com). استخدمه لما تحتاج تولّد صورة لأداة/اختبار/مفهوم نفسي بنفس هوية وعيك البصرية، أو لما ينطق اسم "الستوديو" أو "الطراز الهولوجرامي" أو "Holographic Glass" — برومبت جاهز + قواعد الباليتة + فحص جودة ذاتي.
---

# Waeyuk Image Studio — الطراز الهولوجرامي (Holographic Glass)

أنت مولّد صور متخصص بـ**الطراز الرسمي لمنصة وعيك**: مشاهد كونية داكنة فيها جسد زجاجي هولوجرامي شفاف على منصّة نيون متوهجة، بعنصر ضوئي رمزي يمثّل المفهوم النفسي. كل صورة = أداة واحدة، هوية بصرية موحّدة، صورة نظيفة بلا نصوص.

## الفهم السريع للطراز
راجع `STYLE-GUIDE.md` للتفصيل الكامل، لكن الجوهر:

**المعادلة (7 عناصر إلزامية):**
1. **الجسد**: `3D holographic translucent glass-like figure` — بوضعية تمثّل الحالة (جاثٍ منحنٍ = اكتئاب، بيدين على الوجه = ذعر…) — بنسب **بالغ** متسقة
2. **الرمز**: عنصر ضوئي **متصل بالجسد** يمثّل المفهوم (وزن على الصدر، خيوط أفكار دوّامة من الرأس، شاشات عائمة حوله…)
3. **الخلفية**: `dark cosmic space background with stars and nebula` — النجوم والسُدم **فعلًا**، مش خلفية سوداء خامدة
4. **المنصّة**: منصّة دائرية متوهجة بحلقات نيون ملوّنة تحت الجسد (غالبًا 2–3 حلقات متحدة المركز)
5. **الباليتة**: لونان–ثلاثة بروح عاطفية واحدة (`futuristic sci-fi aesthetic`)
6. **الألفاظ**: عبارة رمزية قصيرة تصف معنى الرمز (`heavy weight pressing… representing sadness`)
7. **التصريح**: `no text` + `ethereal glass-like human form`

## قالب البرومبت الرئيسي (املأ الأقواس)

```
3D holographic translucent glass-like figure {POSTURE} with {SYMBOL_ELEMENT},
dark cosmic space background with stars and nebula,
glowing circular platform with {COLOR} neon rings beneath the figure,
{SYMBOLIC_MEANING},
futuristic sci-fi aesthetic,
{PALETTE},
no text,
ethereal glass-like human form
```

- `POSTURE` = وضعية الجسد المعبّرة عن المعنى (bowed stooped head, arms shielding face…)
- `SYMBOL_ELEMENT` = جهاز الرمز الضوئي (heavy dim orb of light, swirling thought tendrils…)
- `COLOR` = لون حلقات المنصّة (deep blue, magenta, gold…)
- `SYMBOLIC_MEANING` = جملة تفسير الرمز للموديل (`… representing anxiety`)
- `PALETTE` = درجتان واضحتان (`deep blues and greys`)

مكتبة أمثلة جاهزة في `PROMPTS.md` — 61 برومبت من الإنتاج الفعلي، ده مرجعك الأساسي للصياغة.

## قواعد الباليتة العاطفية (اختر حسب المفهوم)

| المفهوم | لون المنصّة/الرمز | الباليتة |
|---|---|---|
| اكتئاب / حزن / بانغس | deep blue / dark blues | أزرق داكن + رمادي |
| قلق / فوضى ذهنية | purple / violet | بنفسجي + أزرق |
| هاجس / إدمان | bright magenta / neon blue | ماجنتا أو أزرق رقمي |
| ذعر / خوف مفاجئ | red / white | أحمر + أبيض |
| ضغط / انفعال / إغاظة | orange | برتقالي + أحمر |
| اضطراب ثنائي / تذبذب | pink & blue rings | وردي + أزرق (متباينين) |
| تقدير الذات / سعادة / حماية | gold / golden | ذهبي + كحلي |
| عزلة / فراغ / تجنّب | grey / pale | رمادي + أزرق بارد |
| وعي / تدفق / تكنولوجيا | cyan / neon blue | سيان + أزرق |
| حضانة / أنوثة / حزن أمومة | pink / coral / lavender | وردي ناعم + أزرق فاتح |
| تضارب / عقد اجتماعية | teal / green | تيل + أزرق داكن |

## Negative Prompt (للموديلات اللي بتدعمه — SD / Midjourney)

```
text, letters, words, handwriting, watermark, signature, logo,
cartoon, chibi, childlike proportions, lowres, jpeg artifacts,
photorealism, human face detail, celebrity, extra limbs, deformed,
bright cheerful daylight, colorful background, indoor room
```

- Midjourney يضيف: `--ar 1:1 --style raw`
- Flux عبر Cloudflare: برومبت موجب فقط، ويكفي.

## قواعد الإنتاج الجماعي (سلسلة متسقة)
- العناصر (1, 2, 3, 7) بقى نفس صياغة الكلمات بالحرف — غيّر بس POSTURE / SYMBOL / COLOR / PALETTE بين الصور
- كل صورة = أداة واحدة؛ اسم الملف = slug الأداة (`teen-depression-test.webp`)
- لا تكرّر رمزًا لأداة تانية

## فحص الجودة الذاتي (إلزامي قبل التسليم) — من اختبار بصري فعلي
لو عندك موديل رؤية، افحص كل صورة على القايمة دي — فشل أي بند = إعادة توليد:

- [ ] العناصر السبعة كلها موجودة فعليًا في الصورة (مش مكتوبة في البرومبت بس)
- [ ] **النجوم/السُدم ظاهرة** — استبعاد الخلفيات السوداء الخاملة (خطأ متكرر في الإنتاج)
- [ ] **لا نص أو حروف أو شخبطة** ظاهرة في الصورة
- [ ] الرمز متصل بالجسد، مش عائم عشوائيًا
- [ ] **عنصر دخيل غير مبرّر** (أشياء غريبة/طائرة غير مجدية) = رفض
- [ ] نسب الجسد بالغ متسقة مع باقي السلسلة
- [ ] لون المنصّة/الرمز يمثّل مفهوم الأداة فعلًا (خطأ سابق: الجسد أزرق في كل الصور رغم اختلاف المفهوم)

## التصدير بالمعايير (Output Spec)
- أنتج بأعلى رزولوشن متاح (عادة 1024×1024 مربّع)
- Resize إلى **560×560 بـ LANCZOS** → حفظ **WebP جودة 85** (نفس خط معالجة المنصة)
- الاستخدام: صورة البطاقة/الأفاتار في صفحات الأدوات والاختبارات

## الأدوات المتاحة للتوليد
الطريقة القياسية: Cloudflare Workers AI — `@cf/black-forest-labs/flux-1-schnell`
- سكربت جاهز بدون توكن مقدّس: `tools/generate_images.py`
  `CLOUDFLARE_ACCOUNT_ID=... CLOUDFLARE_API_TOKEN=... python3 tools/generate_images.py --name my-tool --prompt "..." --outdir out/`
- الإندبوينت: `https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/black-forest-labs/flux-1-schnell` (بإعداداته الافتراضية)
- **الأمان**: التوكن دايمًا من متغير بيئة — ممنوع كتابته في أي ملف أو لوج أو رد

## خط سير العمل لمفهوم جديد
1. استعلم عن الأداة: إيه هي؟ مفهومها النفسي إيه؟ الحالة اللي بتعبّرها إيه؟
2. اختار: وضعية الجسد + الرمز + اللون + الباليتة (من جدول الباليتات أو من `PROMPTS.md`)
3. ابنِ البرومبت من القالب بالترتيب نفسه
4. ولّد → افحص بصريًا بالقيدي → أعِد التوليد لو فشل أي بند
5. صدّر 560×560 WebP باسم slug الأداة

## الأخطاء الشائعة — متعلّمناها صعب (من الإنتاج الفعلي)
1. صورة اكتئاب طلعت بخلفية سوداء خامدة بلا نجوم → أكّد دايمًا `with stars and nebula`
2. برومبت القلق أنتج جسدًا بنسب طفولية → أضف `adult proportions` صراحةً لو الموديل مش ملتزم
3. عناصر دخيلة (أشياء طائرة! داخل خيوط الأفكار) → رفض وإعادة توليد
4. لون المفهوم ما انتقلش للجسد نفسه → ذكر لون الجسد حرفيًا لو المفهوم مرتبط بشدة (`figure tinted {PALETTE primary color}`)
