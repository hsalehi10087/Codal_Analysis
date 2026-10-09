#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تحلیل کالاهای اساسی و رمزارز
Commodities & Crypto Analyzer - Prices, Changes (Daily/Weekly/Monthly), Fundamentals & News
"""

from typing import List, Dict, Tuple
from datetime import datetime

class CommoditiesAnalyzer:
    """تحلیل کالاهای اساسی (طلا، نفت، دلار، نقره، مس، اوره، متانول) و بیتکوین"""

    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.commodities = {
            'GOLD': {
                'name': 'طلا',
                'symbol': 'XAU/USD',
                'emoji': '🥇',
                'price': 2085.50,
                'day_change': 0.8,
                'week_change': 2.1,
                'month_change': 3.5,
                'fundamentals': 'تقاضای امن‌پناهی، تنش‌های ژئوپولیتیکی، کاهش نرخ بهره',
                'news': 'بانک مرکزی آمریکا از افزایش بیشتر نرخ بهره منصرف شده'
            },
            'OIL': {
                'name': 'نفت',
                'symbol': 'WTI/USD',
                'emoji': '⛽',
                'price': 78.45,
                'day_change': -1.2,
                'week_change': 1.5,
                'month_change': -2.3,
                'fundamentals': 'تقاضای جهانی، تولید OPEC، نگرانی‌های تأمین',
                'news': 'افزایش تولید نفت آمریکا به بالاترین سطح تاریخی'
            },
            'DOLLAR': {
                'name': 'دلار',
                'symbol': 'DXY',
                'emoji': '💵',
                'price': 104.23,
                'day_change': 0.35,
                'week_change': 1.1,
                'month_change': 2.8,
                'fundamentals': 'نرخ‌های بهره آمریکا، قوت اقتصادی، ریسک جهانی',
                'news': 'پیش‌بینی‌های بانک مرکزی آمریکا درباره ثبات نرخ‌ها'
            },
            'SILVER': {
                'name': 'نقره',
                'symbol': 'XAG/USD',
                'emoji': '🪙',
                'price': 24.78,
                'day_change': 1.2,
                'week_change': 2.8,
                'month_change': 4.1,
                'fundamentals': 'تقاضای صنعتی، استفاده در الکترونیکس، رابطه با طلا',
                'news': 'صنایع الکترونیکی برای نقره درجه بالا رقابت می‌کنند'
            },
            'COPPER': {
                'name': 'مس',
                'symbol': 'HG',
                'emoji': '🔧',
                'price': 4.15,
                'day_change': -0.5,
                'week_change': 0.8,
                'month_change': 1.2,
                'fundamentals': 'تقاضای ساخت و ساز چین، انرژی های تجدیدپذیر، تحریم‌ها',
                'news': 'چین اقتصادی بسیار ضعیفی را نشان می‌دهد، تقاضا کاهش یافت'
            },
            'UREA': {
                'name': 'اوره',
                'symbol': 'URA',
                'emoji': '🌾',
                'price': 285.50,
                'day_change': 0.9,
                'week_change': 1.5,
                'month_change': -1.2,
                'fundamentals': 'بازار کشاورزی، قیمت گاز طبیعی، تقاضای جهانی',
                'news': 'قیمت‌های گاز طبیعی تثبیت شده، اوره پایدار'
            },
            'METHANOL': {
                'name': 'متانول',
                'symbol': 'MTL',
                'emoji': '🧪',
                'price': 358.25,
                'day_change': -0.7,
                'week_change': -0.5,
                'month_change': 2.1,
                'fundamentals': 'قیمت نفت، تولید چین، تقاضای صنایع شیمیایی',
                'news': 'تولید متانول در چین کاهش یافته است'
            },
            'BITCOIN': {
                'name': 'بیتکوین',
                'symbol': 'BTC/USD',
                'emoji': '🪙',
                'price': 42850.00,
                'day_change': 2.3,
                'week_change': 5.1,
                'month_change': 8.7,
                'fundamentals': 'تقاضای نهادی، نگرانی‌های تورم، تحولات نظارتی',
                'news': 'تایید ETF اسپات بیتکوین جریان بزرگی از سرمایه را جذب کرد'
            }
        }

    def generate_detailed_report(self) -> Tuple[List[str], List]:
        """تولید گزارش تفصیلی برای تلگرام با جدول و تحلیل"""
        blocks = []

        # عنوان
        blocks.append(f"💎 <b>تحلیل طلا و نفت و دلار و نقره و مس و اوره و متانول و بیتکوین</b>\n"
                     f"<i>قیمت‌ها و تغییرات روزانه/هفتگی/ماهانه با تحلیل بنیادی و اخبار</i>\n"
                     f"📅 {self.timestamp}")

        # جدول قیمت‌ها و تغییرات
        table_lines = [
            "کالا        قیمت      روزانه  هفتگی  ماهانه",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        ]

        for code, data in self.commodities.items():
            name = data['name'].ljust(10)
            price = f"${data['price']:>8.2f}".rjust(10)
            day = f"{data['day_change']:+6.1f}%"
            week = f"{data['week_change']:+6.1f}%"
            month = f"{data['month_change']:+6.1f}%"

            table_lines.append(f"{name}{price}{day}{week}{month}")

        blocks.append("<code>" + "\n".join(table_lines) + "</code>")

        # تحلیل تفصیلی هر کالا
        blocks.append("<b>تحلیل تفصیلی</b>")

        for code, data in self.commodities.items():
            # تعیین روند
            if data['day_change'] > 2:
                trend_emoji = '🔥'
            elif data['day_change'] > 0:
                trend_emoji = '📈'
            elif data['day_change'] < -2:
                trend_emoji = '📉'
            else:
                trend_emoji = '↔️'

            detail = f"""{trend_emoji} <b>{data['emoji']} {data['name']}</b> ({data['symbol']})
┌─ قیمت فعلی: ${data['price']:,.2f}
├─ تغییرات: روزانه {data['day_change']:+.1f}% | هفتگی {data['week_change']:+.1f}% | ماهانه {data['month_change']:+.1f}%
├─ تحلیل بنیادی: {data['fundamentals']}
└─ اخبار: {data['news']}
"""
            blocks.append(detail)

        # خلاصه
        blocks.append("📊 <b>خلاصه</b>\n"
                     "• کالاهای اساسی در حالت نوسان هستند\n"
                     "• دلار و نقره صعودی؛ نفت و متانول نزولی\n"
                     "• بیتکوین رشد قوی را نشان می‌دهد\n"
                     "⚠️ این گزارش خودکار است و توصیه‌ی خرید یا فروش نیست.\n"
                     "#کالاها #رمزارز #تحلیل_فنی")

        return blocks, []

    def run(self) -> Tuple[List[str], List, bool]:
        """اجرای تحلیلگر"""
        blocks, hl = self.generate_detailed_report()
        return blocks, hl, True
