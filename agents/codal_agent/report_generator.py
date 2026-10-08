#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Report Generator - Persian Telegram Format
تولید گزارش به فارسی برای تلگرام
"""

from typing import List, Dict
from datetime import datetime

class ReportGenerator:
    """تولید گزارش تلگرام به فارسی"""

    def __init__(self, stocks: List[Dict]):
        self.stocks = stocks
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    def generate_telegram_report(self) -> str:
        """تولید گزارش تلگرام به فارسی"""

        # Categorize stocks
        strong_buys = [s for s in self.stocks if s.get('overall_score', 0) >= 75]
        buys = [s for s in self.stocks if 60 <= s.get('overall_score', 0) < 75]
        holds = [s for s in self.stocks if s.get('overall_score', 0) < 60]

        report = f"""📊 گزارش کدال ۳۶۰
📅 {self.timestamp}

"""

        # Strong buys
        if strong_buys:
            report += """🟢 خریدی قوی (75+)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
            report += self._generate_table(strong_buys[:5])
            if len(strong_buys) > 5:
                report += f"\n... و {len(strong_buys) - 5} سهم دیگر\n"
            report += "\n"

        # Buys
        if buys:
            report += """🟡 خریدی (60-74)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
            report += self._generate_table(buys[:8])
            if len(buys) > 8:
                report += f"\n... و {len(buys) - 8} سهم دیگر\n"
            report += "\n"

        # Summary
        report += f"""📈 خلاصه
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
کل بررسی‌شده: {len(self.stocks)}
🟢 خریدی قوی: {len(strong_buys)}
🟡 خریدی: {len(buys)}
⚪ نگاه: {len(holds)}

🤖 تحلیل خودکار کدال
#کدال #سرمایه‌گذاری #بورس
"""

        return report

    def _generate_table(self, stocks: List[Dict]) -> str:
        """تولید جدول سهام‌ها"""

        # Header
        table = "<code>"
        table += "نماد    کدال  بافت  گریم  سوروس وود  تکنیکال\n"
        table += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

        for stock in stocks:
            ticker = stock.get('ticker', '').ljust(6)
            can_slim = str(int(stock.get('can_slim_score', 0))).rjust(4)
            buffett = str(int(stock.get('buffett_score', 0))).rjust(4)
            graham = str(int(stock.get('graham_score', 0))).rjust(4)
            soros = str(int(stock.get('soros_score', 0))).rjust(4)
            wood = str(int(stock.get('wood_score', 0))).rjust(4)
            tech = str(int(stock.get('tech_score', 0))).rjust(4)

            table += f"{ticker}{can_slim}{buffett}{graham}{soros}{wood}{tech}\n"

        table += "</code>"

        return table

    def generate_strong_buys(self) -> str:
        """تولید لیست خریدهای قوی"""
        strong = [s for s in self.stocks if s.get('overall_score', 0) >= 75]
        return f"🟢 خریدی قوی: {len(strong)}"

    def generate_buys(self) -> str:
        """تولید لیست خریدها"""
        buys = [s for s in self.stocks if 60 <= s.get('overall_score', 0) < 75]
        return f"🟡 خریدی: {len(buys)}"

    def generate_holds(self) -> str:
        """تولید لیست نگاه‌ها"""
        holds = [s for s in self.stocks if s.get('overall_score', 0) < 60]
        return f"⚪ نگاه: {len(holds)}"

    def generate_summary(self) -> str:
        """تولید خلاصهٔ کلی"""
        strong = [s for s in self.stocks if s.get('overall_score', 0) >= 75]
        buys = [s for s in self.stocks if 60 <= s.get('overall_score', 0) < 75]
        holds = [s for s in self.stocks if s.get('overall_score', 0) < 60]

        return f"""📊 خلاصهٔ تحلیل
━━━━━━━━━━━━━━━━━━━━━━
کل: {len(self.stocks)}
🟢 قوی: {len(strong)}
🟡 خوب: {len(buys)}
⚪ ضعیف: {len(holds)}
"""
