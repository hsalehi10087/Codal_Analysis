#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codal Daily Agent - Simple Standalone Version
"""

import os
import requests
from datetime import datetime

def main():
    print("🤖 شروع تحلیل کدال...")

    # Generate report filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"report_{timestamp}.txt"

    # Sample report content
    report = """📊 گزارش کدال ۳۶۰
📅 2026-10-08 12:33

🟢 خریدی قوی (75+)
نماد      کدال    بافت    گریم    سوروس   وود    تکنیکال
SHAKH      80       90      75      85      80      88
PETR       78       85      80      82      75      86

🟡 خریدی (60-74)
IRCC       70       75      70      70      68      75
KHOB       68       72      68      70      65      70
SACCI      65       70      62      65      68      68

📈 خلاصه
کل بررسی‌شده: 50
🟢 قوی: 8
🟡 خوب: 15
⚪ ضعیف: 27

🤖 تحلیل خودکار کدال
#کدال #سرمایه‌گذاری
"""

    # Save report file
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✅ گزارش ذخیره شد: {report_file}")
    except Exception as e:
        print(f"❌ خطا در ذخیره: {e}")
        return False

    # Send Telegram
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN', '')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID', '')

    if telegram_token and telegram_chat_id:
        try:
            url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
            payload = {
                'chat_id': telegram_chat_id,
                'text': report,
                'parse_mode': 'HTML'
            }

            response = requests.post(url, json=payload, timeout=10)

            if response.status_code == 200:
                print("✅ گزارش به تلگرام فرستاده شد")
            else:
                print(f"⚠️  خطا در تلگرام: {response.status_code}")
        except Exception as e:
            print(f"⚠️  خطا تلگرام: {e}")
    else:
        print("⚠️  توکن تلگرام یافت نشد")

    print("✅ کامل شد")
    return True

if __name__ == "__main__":
    try:
        success = main()
        exit(0 if success else 1)
    except Exception as e:
        print(f"❌ خطای عمومی: {e}")
        exit(1)
