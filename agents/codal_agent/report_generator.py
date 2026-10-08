#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Report Generator
جدول‌های تلگرام را تولید می‌کند
"""

from typing import List, Dict
from datetime import datetime
import json

class ReportGenerator:
    def __init__(self, stocks_analysis: List[Dict]):
        self.stocks = stocks_analysis
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def generate_telegram_report(self) -> str:
        """
        گزارش تلگرام را تولید می‌کند
        """
        lines = [
            "📊 <b>گزارش کدال ۳۶۰</b>",
            f"📅 {self.date}",
            "",
            self.generate_strong_buys(),
            "",
            self.generate_buys(),
            "",
            self.generate_holds(),
            "",
            self.generate_summary()
        ]

        return "\n".join(lines)

    def generate_strong_buys(self) -> str:
        """
        سهام‌های خریدی قوی
        """
        strong = [s for s in self.stocks if s.get('overall_score', 0) >= 75]

        if not strong:
            return "🔴 خریدی قوی: ندارد"

        lines = ["🟢 <b>خریدی قوی (75+)</b>"]
        lines.append("<code>نماد      کدال    بافت    گریم    سوروس   وود    تکنیکال</code>")

        for stock in sorted(strong, key=lambda x: x.get('overall_score', 0), reverse=True)[:5]:
            ticker = stock.get('ticker', '')[:6].ljust(6)
            codal = str(stock.get('can_slim_score', 0))[:2].rjust(3)
            buffett = str(stock.get('buffett_score', 0))[:2].rjust(4)
            graham = str(stock.get('graham_score', 0))[:2].rjust(5)
            soros = str(stock.get('soros_score', 0))[:2].rjust(5)
            wood = str(stock.get('wood_score', 0))[:2].rjust(3)
            tech = str(stock.get('tech_score', 0))[:2].rjust(4)

            lines.append(f"<code>{ticker}{codal}{buffett}{graham}{soros}{wood}{tech}</code>")

        return "\n".join(lines)

    def generate_buys(self) -> str:
        """
        سهام‌های خریدی معمولی
        """
        buys = [s for s in self.stocks if 60 <= s.get('overall_score', 0) < 75]

        if not buys:
            return "🟡 خریدی: ندارد"

        lines = ["🟡 <b>خریدی (60-74)</b>"]
        lines.append("<code>نماد      کدال    بافت    گریم    سوروس   وود    تکنیکال</code>")

        for stock in sorted(buys, key=lambda x: x.get('overall_score', 0), reverse=True)[:8]:
            ticker = stock.get('ticker', '')[:6].ljust(6)
            codal = str(stock.get('can_slim_score', 0))[:2].rjust(3)
            buffett = str(stock.get('buffett_score', 0))[:2].rjust(4)
            graham = str(stock.get('graham_score', 0))[:2].rjust(5)
            soros = str(stock.get('soros_score', 0))[:2].rjust(5)
            wood = str(stock.get('wood_score', 0))[:2].rjust(3)
            tech = str(stock.get('tech_score', 0))[:2].rjust(4)

            lines.append(f"<code>{ticker}{codal}{buffett}{graham}{soros}{wood}{tech}</code>")

        return "\n".join(lines)

    def generate_holds(self) -> str:
        """
        سهام‌های نگاه
        """
        holds = [s for s in self.stocks if s.get('overall_score', 0) < 60]

        if not holds:
            return "⚪ نگاه: ندارد"

        lines = ["⚪ <b>نگاه (<60)</b>"]
        lines.append(f"تعداد: {len(holds)}")

        return "\n".join(lines)

    def generate_summary(self) -> str:
        """
        خلاصهٔ آماری
        """
        total = len(self.stocks)
        strong = len([s for s in self.stocks if s.get('overall_score', 0) >= 75])
        good = len([s for s in self.stocks if 60 <= s.get('overall_score', 0) < 75])
        weak = len([s for s in self.stocks if s.get('overall_score', 0) < 60])

        lines = [
            "📈 <b>خلاصه</b>",
            f"کل بررسی‌شده: {total}",
            f"🟢 قوی: {strong}",
            f"🟡 خوب: {good}",
            f"⚪ ضعیف: {weak}",
            "",
            "🤖 تحلیل خودکار کدال",
            "#کدال #سرمایه‌گذاری"
        ]

        return "\n".join(lines)

    def generate_html_report(self) -> str:
        """
        گزارش HTML (برای ذخیره)
        """
        html = [
            "<html><head><meta charset='utf-8'><title>کدال</title></head><body>",
            "<h1>گزارش کدال ۳۶۰</h1>",
            f"<p>تاریخ: {self.date}</p>",
            self.generate_strong_buys(),
            self.generate_buys(),
            self.generate_holds(),
            "</body></html>"
        ]

        return "\n".join(html)

if __name__ == "__main__":
    # Test
    test_stocks = [
        {
            'ticker': 'SHAKH',
            'company': 'شاه',
            'overall_score': 85,
            'can_slim_score': 80,
            'buffett_score': 90,
            'graham_score': 75,
            'soros_score': 85,
            'wood_score': 80,
            'tech_score': 88
        },
        {
            'ticker': 'IRCC',
            'company': 'بیمه ایران',
            'overall_score': 72,
            'can_slim_score': 70,
            'buffett_score': 75,
            'graham_score': 70,
            'soros_score': 70,
            'wood_score': 68,
            'tech_score': 75
        }
    ]

    gen = ReportGenerator(test_stocks)
    report = gen.generate_telegram_report()
    print(report)
