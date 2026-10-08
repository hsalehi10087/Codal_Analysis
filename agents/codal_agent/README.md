# 🤖 Codal Daily Agent

سیستم تحلیل خودکار گزارش‌های کدال ۳۶۰ با امتیاز‌دهی چندمعیاری

## 📋 مزایا

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
codal_agent/
├── main.py              # Orchestrator
├── scraper.py           # دریافت از codal.ir
├── analyzer.py          # ۶ معیار امتیاز‌دهی
├── report_generator.py   # تولید گزارش تلگرام
├── codal_daily.yml      # GitHub Actions workflow
└── README.md            # این فایل
```

## 🚀 نصب و راه‌اندازی

### ۱️⃣ کپی فایل‌ها به مخزن GitHub

```bash
# در ریشهٔ مخزن خود:
mkdir -p agents/codal_agent
cp *.py agents/codal_agent/

# GitHub Actions workflow:
mkdir -p .github/workflows
cp codal_daily.yml .github/workflows/
```

### ۲️⃣ تنظیم GitHub Secrets

```
Repo Settings → Secrets and variables → Actions → New repository secret

TELEGRAM_BOT_TOKEN=<توکن بات تلگرام شما>
TELEGRAM_CHAT_ID=<ID چت خصوصی شما>
```

### ۳️⃣ فعال‌سازی Workflow

```bash
git add .github/workflows/codal_daily.yml agents/codal_agent/
git commit -m "Add Codal Daily Agent"
git push
```

## 🧪 تست محلی

```bash
# Requirements
pip install requests

# متغیرهای محیط را تنظیم کنید:
export TELEGRAM_BOT_TOKEN="your_token"
export TELEGRAM_CHAT_ID="your_chat_id"

# اجرا:
cd agents/codal_agent
python main.py
```

## 📊 نمونهٔ گزارش

```
📊 گزارش کدال ۳۶۰
📅 2026-10-08 20:30

🟢 خریدی قوی (75+)
نماد      کدال    بافت    گریم    سوروس   وود    تکنیکال
SHAKH      80       90      75      85      80      88

🟡 خریدی (60-74)
نماد      کدال    بافت    گریم    سوروس   وود    تکنیکال
IRCC       70       75      70      70      68      75

📈 خلاصه
کل بررسی‌شده: 50
🟢 قوی: 8
🟡 خوب: 15
⚪ ضعیف: 27

🤖 تحلیل خودکار کدال
#کدال #سرمایه‌گذاری
```

## 🔧 تنظیمات

### تغییر زمان اجرا

فایل `.github/workflows/codal_daily.yml` را ویرایش کنید:

```yaml
schedule:
  # Cron format: minute hour day month weekday
  - cron: '30 20 * * 1-5'  # ۲۰:۳۰ UTC (۴:۳۰ PM ET)
```

### تعداد سهام‌های تحلیل‌شده

فایل `main.py` را ویرایش کنید:

```python
analyzed_stocks = self.analyze_stocks(reports[:100])  # ۱۰۰ سهام
```

## 🔌 یکپارچگی

### Telegram

- توکن و Chat ID از `@BotFather`
- برای اضافه کردن چنل خصوصی شما به بات

### Codal.ir API

- عمومی و بدون احتیاج به احراز هویت
- دریافت ۵۰ آخرین گزارش

### داده‌های مالی (آینده)

برای دریافت داده‌های واقعی سهام:

```python
# استفاده از Finnhub (نیاز به API Key):
# pip install finnhub-python
```

## 📝 نکات مهم

⚠️ **داده‌های نمونه**
- الآن analyzer از داده‌های ثابت استفاده می‌کند
- برای داده‌های واقعی، Finnhub یا منابع دیگر را ادغام کنید

⚠️ **محدودیت‌های API**
- Codal.ir: ۵۰ گزارش فی درخواست
- Telegram: ۳۰ پیام/ثانیه

⚠️ **بک‌تست**
- این سیستم برای استفادهٔ لحظه‌ای طراحی شده
- برای بک‌تست، داده‌های تاریخی نیاز است

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
- اگر timeout: محدودیت‌ سرویس را بررسی کنید
```

## 📈 بهبود‌های آینده

- [ ] ادغام داده‌های مالی واقعی (Finnhub)
- [ ] تاریخچهٔ امتیاز‌ها و نمودارها
- [ ] فیلتر براساس سکتور و بازار‌سرمایه
- [ ] هشدارهای قیمتی
- [ ] Backtest قابلیت
- [ ] Multi-language support

## 📞 پشتیبانی

برای مسائل:
1. بررسی لاگ‌های Workflow در GitHub Actions
2. تست محلی با `python main.py`
3. بررسی توکن‌های Telegram و Codal

---

**ایجاد شده با ❤️ برای تحلیل هوشمند کدال**
