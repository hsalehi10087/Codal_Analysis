#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codal 360 Scraper
گره‌ای از Codal.ir را دریافت می‌کند
"""

import requests
import json
import re
from datetime import datetime
from typing import List, Dict

class CogalScraper:
    def __init__(self):
        self.base_url = "https://codal.ir"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.timeout = 10

    def fetch_latest_reports(self, limit: int = 50) -> List[Dict]:
        """
        آخرین گزارش‌های کدال را دریافت می‌کند
        """
        try:
            # Codal API (عمومی)
            url = f"{self.base_url}/api/search/v2"

            params = {
                'Type': '1',  # بخش‌نامه‌های مالی
                'Mains': '0',
                'Isic': '0',
                'Audited': '-1',
                'PageNumber': '1',
                'PageSize': str(limit),
                'sortby': '1'  # newest first
            }

            response = requests.get(url, headers=self.headers, params=params, timeout=self.timeout)
            response.encoding = 'utf-8'

            if response.status_code == 200:
                data = response.json()
                reports = []

                if 'result' in data and data['result']:
                    for item in data['result']:
                        report = {
                            'ticker': item.get('code', ''),
                            'company': item.get('name', ''),
                            'report_date': item.get('pubDate', ''),
                            'report_id': item.get('id', ''),
                            'type': item.get('type', ''),
                            'url': f"{self.base_url}/report/id/{item.get('id', '')}"
                        }
                        reports.append(report)

                return reports
            else:
                print(f"❌ Codal API خطا: {response.status_code}")
                return []

        except Exception as e:
            print(f"❌ Scraper خطا: {str(e)}")
            return []

    def get_report_details(self, report_id: str) -> Dict:
        """
        جزئیات گزارش را دریافت می‌کند
        """
        try:
            url = f"{self.base_url}/api/report/detail/id/{report_id}"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.encoding = 'utf-8'

            if response.status_code == 200:
                return response.json()
            return {}
        except Exception as e:
            print(f"❌ Detail fetch خطا: {str(e)}")
            return {}

if __name__ == "__main__":
    scraper = CogalScraper()
    reports = scraper.fetch_latest_reports(limit=30)
    print(f"✅ {len(reports)} گزارش پیدا شد")
    for r in reports[:5]:
        print(f"   {r['ticker']}: {r['company']}")
