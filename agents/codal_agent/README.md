# 🤖 Codal Daily Agent

سیستم تحلیل خودکار گزارش‌های کدال ۳۶۰ با امتیاز‌دهی چندمعیاری

## 📋 ویژگی‌ها

✅ **تحلیل ۶ معیار سرمایه‌گذاری:**
- CAN SLIM (William O'Neil)
- Buffett Value Investing
- Graham Safety Margin
- Soros Macro + Momentum
- Cathie Wood Growth
- تحلیل تکنیکال

✅ **گزارش تلگرام روزانه:**
- سهام‌های خریدی قوی (75+)
- سهام‌های خریدی (60-74)
- سهام‌های نگاه (<60)

✅ **اتوماسیون کامل:**
- اجرای خودکار هر روز (۴:۳۰ بعد از ظهر ET)
- ذخیره محلی گزارش‌ها
- ارسال فوری به تلگرام

## 📁 ساختار فایل‌ها

```
agents/codal_agent/
├── main.py              # Orchestrator
├── scraper.py           # دریافت از codal.ir
├── analyzer.py          # ۶ معیار امتیاز‌دهی
├── report_generator.py   # تولید گزارش تلگرام
├── requirements.txt      # وابستگی‌ها
├── README.md            # این فایل
└── .github/workflows/codal_daily.yml  # GitHub Actions
```

## 🚀 نصب و راه‌اندازی

### مرحلهٔ ۱: آپلود فایل‌ها به GitHub

1. **به مخزن GitHub خود بروید:**
   - Codal_Analysis

2. **ایجاد پوشه:**
   - کلیک "Add file" → Create new file
   - مسیر: `agents/codal_agent/main.py`
   - کپی کنید: محتوای `main.py`

3. **فایل‌های دیگر را آپلود کنید:**
   - `agents/codal_agent/scraper.py`
   - `agents/codal_agent/analyzer.py`
   - `agents/codal_agent/report_generator.py`
   - `agents/codal_agent/requirements.txt`

4. **GitHub Actions Workflow:**
   - مسیر: `.github/workflows/codal_daily.yml`
   - کپی کنید: محتوای `codal_daily.yml`

### مرحلهٔ ۲: تنظیم GitHub Secrets

1. **به Settings بروید:**
   ```
   Repo → Settings → Secrets and variables → Actions
   ```

2. **دو secret اضافه کنید:**

   **New repository secret:**
   ```
   Name: TELEGRAM_BOT_TOKEN
   Value: 8752723544:AAGXaTb5icR_VQLCBD-t7aDyoGVpdYLBp9w
   ```

   **New repository secret:**
   ```
   Name: TELEGRAM_CHAT_ID
   Value: -75439320
   ```

### مرحلهٔ ۳: فعال‌سازی Workflow

1. **به Actions بروید:**
   ```
   Repo → Actions
   ```

2. **Codal Daily Agent را انتخاب کنید**

3. **کلیک "Run workflow"**

4. **منتظر 1-2 دقیقه باشید**

## 📊 نمونهٔ گزارش

```
📊 گزارش کدال ۳۶۰
📅 2026-10-08 20:30

🟢 خریدی قوی (75+)
نماد    کدال  بافت  گریم  سوروس وود  تکنیکال
SHAKH   80    90    75    85    80    88
PETR    78    85    80    82    75    86

🟡 خریدی (60-74)
نماد    کدال  بافت  گریم  سوروس وود  تکنیکال
IRCC    70    75    70    70    68    75

📈 خلاصه
کل بررسی‌شده: 50
🟢 قوی: 8
🟡 خوب: 15
⚪ ضعیف: 27

🤖 تحلیل خودکار کدال
#کدال #سرمایه‌گذاری
```

## 🧪 تست محلی

### نصب وابستگی‌ها

```bash
pip install requests
```

### اجرا

```bash
export TELEGRAM_BOT_TOKEN="your_token"
export TELEGRAM_CHAT_ID="your_chat_id"

cd agents/codal_agent
python main.py
```

## 🔧 تنظیمات

### تغییر زمان اجرا

فایل `.github/workflows/codal_daily.yml` را ویرایش کنید:

```yaml
schedule:
  - cron: '30 20 * * 1-5'  # ۲۰:۳۰ UTC (۴:۳۰ PM ET)
```

**فرمت Cron:**
```
minute hour day month weekday
0      0    *   *     *
↑      ↑    ↑   ↑     ↑
دقیقه  ساعت روز ماه روز هفته
```

**مثال‌ها:**
- `0 8 * * 1-5` = صبح ۸ شب (اوقات دوشنبه تا جمعه)
- `30 16 * * *` = ۱۶:۳۰ (هر روز)
- `0 0 * * 0` = شب (هر یکشنبه)

### تعداد سهام‌های تحلیل‌شده

فایل `main.py` را ویرایش کنید:

```python
analyzed_stocks = self.analyze_stocks(reports[:100])  # ۱۰۰ سهام
```

## 🔌 یکپارچگی

### Telegram

- توکن و Chat ID از `@BotFather`
- بات را admin کنید

### Codal.ir API

- عمومی و بدون احتیاج به احراز هویت
- دریافت ۵۰ آخرین گزارش

## 📝 نکات مهم

⚠️ **داده‌های نمونه**
- الآن analyzer از داده‌های ثابت استفاده می‌کند
- برای داده‌های واقعی، Finnhub یا منابع دیگر را ادغام کنید

⚠️ **محدودیت‌های API**
- Codal.ir: ۵۰ گزارش فی درخواست
- Telegram: ۳۰ پیام/ثانیه

⚠️ **مراحل اول**
1. فایل‌ها را آپلود کنید
2. GitHub Secrets را تنظیم کنید
3. Workflow را اجرا کنید
4. گزارش را در Telegram بررسی کنید

## 🐛 عیب‌یابی

**❌ Workflow نمی‌رود:**
```
Settings → Actions → عام → Workflow permissions → Read and write
```

**❌ Telegram پیام دریافت نمی‌کند:**
```
- توکن و Chat ID را بررسی کنید
- بات را admin کنید
```

**❌ Codal.ir پاسخ نمی‌دهد:**
```
- User-Agent مناسب استفاده می‌شود
- اگر timeout: محدودیت‌های سرویس را بررسی کنید
```

## 📈 بهبود‌های آینده

- [ ] ادغام داده‌های مالی واقعی (Finnhub)
- [ ] تاریخچهٔ امتیاز‌ها و نمودارها
- [ ] فیلتر براساس سکتور
- [ ] هشدارهای قیمتی
- [ ] Backtest قابلیت

## 📞 پشتیبانی

برای مسائل:
1. بررسی لاگ‌های Workflow در GitHub Actions
2. تست محلی با `python main.py`
3. بررسی توکن‌های Telegram و Codal

---

**ایجاد شده با ❤️ برای تحلیل هوشمند کدال**
