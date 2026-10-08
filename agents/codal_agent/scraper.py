#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codal.ir Web Scraper
دریافت گزارش‌های کدال ۳۶۰
"""

import requests
from typing import List, Dict
from datetime import datetime

class CogalScraper:
    """دریافت گزارش‌های کدال از API"""

    def __init__(self):
        self.base_url = "https://codal.ir/api/search/v2"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def fetch_latest_reports(self, limit: int = 50) -> List[Dict]:
        """
        آخرین گزارش‌های کدال را دریافت می‌کند

        Args:
            limit: تعداد گزارش‌های دریافتی

        Returns:
            لیست دیکشنری‌های گزارش
        """
        try:
            params = {
                'search': '',
                'pageNumber': 0,
                'pageSize': limit,
                'sortType': 'date'
            }

            response = requests.get(
                self.base_url,
                params=params,
                headers=self.headers,
                timeout=10
            )

            if response.status_code != 200:
                print(f"❌ خطا: {response.status_code}")
                return []

            data = response.json()
            reports = []

            if 'items' in data:
                for item in data['items'][:limit]:
                    report = {
                        'ticker': item.get('symbol', ''),
                        'company': item.get('companyName', ''),
                        'report_date': item.get('publishDateTime', ''),
                        'report_id': item.get('id', ''),
                        'type': item.get('reportType', ''),
                        'url': f"https://codal.ir/report/{item.get('id', '')}"
                    }
                    reports.append(report)

            return reports

        except Exception as e:
            print(f"❌ خطا در دریافت: {str(e)}")
            return []

    def get_report_details(self, report_id: str) -> Dict:
        """
        جزئیات یک گزارش را دریافت می‌کند

        Args:
            report_id: ID گزارش

        Returns:
            دیکشنری جزئیات گزارش
        """
        try:
            url = f"https://codal.ir/api/report/{report_id}"
            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code != 200:
                return {}

            return response.json()

        except Exception as e:
            print(f"❌ خطا: {str(e)}")
            return {}
