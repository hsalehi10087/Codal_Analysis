#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Commodities & Crypto Analyzer
تحلیل کالاهای اساسی و رمزارز
"""

from typing import List, Dict
from datetime import datetime

class CommoditiesAnalyzer:
    """تحلیل کالاهای اساسی (طلا، نفت، دلار، نقره، مس، اوره، متانول) و بیتکوین"""

    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.commodities = {
            'GOLD': {
                'name': 'طلا',
                'symbol': 'XAU/USD',
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
                'price': 42850.00,
                'day_change': 2.3,
                'week_change': 5.1,
                'month_change': 8.7,
                'fundamentals': 'تقاضای نهادی، نگرانی‌های تورم، تحولات نظارتی',
                'news': 'تایید ETF اسپات بیتکوین جریان بزرگی از سرمایه را جذب کرد'
            }
        }

    def analyze(self) -> List[Dict]:
        """تحلیل تمام کالاها و رمزارزها"""
        analyzed = []

        for code, data in self.commodities.items():
            analyzed.append({
                'code': code,
                'name': data['name'],
                'symbol': data['symbol'],
                'price': data['price'],
                'day_change': data['day_change'],
                'week_change': data['week_change'],
                'month_change': data['month_change'],
                'fundamentals': data['fundamentals'],
                'news': data['news'],
                'trend': self._determine_trend(data['day_change'], data['month_change']),
                'signal': self._generate_signal(data['day_change'], data['month_change'])
            })

        return analyzed

    def _determine_trend(self, day_change: float, month_change: float) -> str:
        """تعیین روند عمومی"""
        if day_change > 1 and month_change > 2:
            return 'صعودی قوی'
        elif day_change > 0 and month_change > 0:
            return 'صعودی'
        elif day_change < -1 and month_change < -2:
            return 'نزولی قوی'
        elif day_change < 0 and month_change < 0:
            return 'نزولی'
        else:
            return 'خنثی'

    def _generate_signal(self, day_change: float, month_change: float) -> str:
        """تولید سیگنال معاملاتی"""
        if day_change > 1.5 and month_change > 3:
            return '📈 خرید (شتاب صعودی)'
        elif day_change > 0 and month_change > 1:
            return '📊 نگاه (روند صعودی)'
        elif day_change < -1.5 and month_change < -3:
            return '📉 فروش (شتاب نزولی)'
        elif day_change < 0 and month_change < -1:
            return '📊 نگاه (روند نزولی)'
        else:
            return '⚪ نقطه‌تحول (موقعیت نامعین)'

    def generate_summary_table(self) -> str:
        """تولید جدول خلاصه برای تلگرام"""
        analyzed = self.analyze()

        table = "<code>"
        table += "کالا        قیمت    روزانه   هفتگی   ماهانه\n"
        table += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

        for item in analyzed:
            name = item['name'].ljust(10)
            price = str(round(item['price'], 2)).ljust(8)

            day = str(round(item['day_change'], 1)).rjust(6) + '%'
            week = str(round(item['week_change'], 1)).rjust(6) + '%'
            month = str(round(item['month_change'], 1)).rjust(6) + '%'

            table += f"{name}{price}{day}{week}{month}\n"

        table += "</code>"
        return table

    def generate_detailed_report(self) -> str:
        """تولید گزارش تفصیلی برای تلگرام"""
        analyzed = self.analyze()

        report = f"""💎 گزارش کالاهای اساسی و رمزارز
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 {self.timestamp}

"""

        # Summary table
        report += self.generate_summary_table()
        report += "\n\n"

        # Detailed analysis
        for item in analyzed:
            trend_emoji = {
                'صعودی قوی': '🔥',
                'صعودی': '📈',
                'نزولی قوی': '🔴',
                'نزولی': '📉',
                'خنثی': '⚪'
            }.get(item['trend'], '⚪')

            report += f"""{trend_emoji} <b>{item['name']}</b> ({item['symbol']})
┌─ قیمت: ${item['price']}
├─ روند: {item['trend']}
├─ سیگنال: {item['signal']}
├─ تحلیل بنیادی: {item['fundamentals']}
└─ اخبار: {item['news']}

"""

        report += """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 کالاها و رمزارزها - تحلیل خودکار
#کالاها #رمزارز #تحلیل_فنی #سرمایه‌گذاری
"""

        return report
