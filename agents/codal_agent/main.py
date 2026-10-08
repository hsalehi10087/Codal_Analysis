#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codal Daily Agent - Main Orchestrator
سیستم تحلیل روزانه کدال ۳۶۰
"""

import os
import sys
import json
import requests
from datetime import datetime
from typing import List, Dict

# Import our modules
from scraper import CogalScraper
from analyzer import StockAnalyzer
from report_generator import ReportGenerator

class CodalDailyAgent:
    def __init__(self):
        self.scraper = CogalScraper()
        self.telegram_token = os.getenv('TELEGRAM_BOT_TOKEN', '')
        self.telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID', '')
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    def extract_stock_data(self, report: Dict) -> Dict:
        """
        گزارش کدال را به داده‌های سهام تبدیل می‌کند
        """
        # برای نمونه، استفاده از مقادیر پیش‌فرض
        # در عملیات واقعی، باید از API کدال یا Finnhub داده بگیرید

        return {
            'ticker': report.get('ticker', 'UNKNOWN'),
            'company': report.get('company', 'Unknown'),
            'sales_growth': 15,  # placeholder
            'annual_growth': 20,
            'has_new_products': False,
            'market_position': 'low',
            'market_cap': 500000000,
            'pe_ratio': 14,
            'roe': 18,
            'debt_equity': 0.4,
            'current_ratio': 1.8,
            'earnings_stable': True,
            'pb_ratio': 1.3,
            'earnings_growth': 10,
            'dividend_yield': 2.5,
            'price_momentum': 8,
            'volume_trend': 5,
            'sector_strength': 'strong',
            'volatility': 18,
            'revenue_growth': 22,
            'innovation_score': 60,
            'disruption_potential': 'low',
            'margin_growth': 3,
            'trend': 'up',
            'rsi': 55,
            'macd_signal': True
        }

    def analyze_stocks(self, reports: List[Dict]) -> List[Dict]:
        """
        تمام سهام‌های گزارش‌شده را تحلیل می‌کند
        """
        analyzed = []

        for report in reports[:50]:  # Max 50 stocks per day
            try:
                # Extract stock data
                stock_data = self.extract_stock_data(report)

                # Analyze
                analyzer = StockAnalyzer(stock_data)
                results = analyzer.analyze()

                # Compile result
                stock_result = {
                    'ticker': report.get('ticker', ''),
                    'company': report.get('company', ''),
                    'report_url': report.get('url', ''),
                    'can_slim_score': results['can_slim']['score'],
                    'buffett_score': results['buffett']['score'],
                    'graham_score': results['graham']['score'],
                    'soros_score': results['soros']['score'],
                    'wood_score': results['wood']['score'],
                    'tech_score': results['technical']['score'],
                    'overall_score': results['overall']
                }

                analyzed.append(stock_result)

            except Exception as e:
                print(f"❌ خطا در تحلیل {report.get('ticker', '')}: {str(e)}")
                continue

        return analyzed

    def send_telegram_report(self, message: str) -> bool:
        """
        گزارش را به تلگرام می‌فرستد
        """
        if not self.telegram_token or not self.telegram_chat_id:
            print("❌ توکن تلگرام یا Chat ID یافت نشد")
            return False

        try:
            url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
            payload = {
                'chat_id': self.telegram_chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }

            response = requests.post(url, json=payload, timeout=10)

            if response.status_code == 200:
                print("✅ گزارش به تلگرام فرستاده شد")
                return True
            else:
                print(f"❌ خطا در ارسال: {response.status_code}")
                return False

        except Exception as e:
            print(f"❌ خطا: {str(e)}")
            return False

    def run(self) -> bool:
        """
        اجرای کامل agent
        """
        print("🤖 شروع تحلیل کدال...")

        # 1. Fetch latest reports
        print("📥 دریافت گزارش‌های کدال...")
        reports = self.scraper.fetch_latest_reports(limit=50)

        if not reports:
            print("❌ هیچ گزارش پیدا نشد")
            return False

        print(f"✅ {len(reports)} گزارش دریافت شد")

        # 2. Analyze stocks
        print("🔍 تحلیل سهام...")
        analyzed_stocks = self.analyze_stocks(reports)

        if not analyzed_stocks:
            print("❌ تحلیل ناموفق")
            return False

        print(f"✅ {len(analyzed_stocks)} سهام تحلیل شد")

        # 3. Generate report
        print("📊 تولید گزارش...")
        generator = ReportGenerator(analyzed_stocks)
        telegram_report = generator.generate_telegram_report()

        # 4. Save report locally
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"report_{timestamp}.txt"

        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(telegram_report)

        print(f"✅ گزارش ذخیره شد: {report_file}")

        # 5. Send to Telegram
        print("📤 ارسال گزارش...")
        success = self.send_telegram_report(telegram_report)

        if success:
            print("✅ کامل شد")
            return True
        else:
            print("⚠️  گزارش محلی ذخیره شد اما ارسال تلگرام ناموفق")
            return False

if __name__ == "__main__":
    agent = CodalDailyAgent()
    success = agent.run()
    sys.exit(0 if success else 1)
