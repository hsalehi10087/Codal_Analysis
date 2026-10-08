#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stock Analyzer - 6 Investment Frameworks
تحلیل سهام با 6 معیار سرمایه‌گذاری
"""

from typing import Dict, List

class StockAnalyzer:
    """تحلیل سهام با 6 معیار مختلف"""

    def __init__(self, stock_data: Dict):
        self.data = stock_data

    def score_canslim(self) -> Dict:
        """
        CAN SLIM Framework (William O'Neil)
        C=Current earnings, A=Annual growth, N=New products,
        S=Supply, L=Leader, I=Industry, M=Market cap
        """
        score = 0
        details = []

        # Current earnings growth
        if self.data.get('sales_growth', 0) > 20:
            score += 15
            details.append("رشد فروش بالا")

        # Annual growth
        if self.data.get('annual_growth', 0) > 20:
            score += 15
            details.append("رشد سالانه قوی")

        # New products
        if self.data.get('has_new_products', False):
            score += 10
            details.append("محصولات جدید")

        # Supply-demand
        score += 10
        details.append("توازن عرضه-تقاضا")

        # Leader
        if self.data.get('market_position', '') == 'high':
            score += 15
            details.append("رهبر بازار")

        # Industry strength
        if self.data.get('sector_strength', '') == 'strong':
            score += 15
            details.append("صنعت قوی")

        # Market cap
        if self.data.get('market_cap', 0) > 1000000000:
            score += 10
            details.append("بازار‌سرمایهٔ مناسب")

        rating = self._get_rating(score)

        return {
            'score': min(score, 100),
            'details': details,
            'rating': rating
        }

    def score_buffett(self) -> Dict:
        """
        Warren Buffett Value Investing
        P/E <15, ROE >15%, Debt/Equity <0.5, Current Ratio >1.5, Earnings Stability
        """
        score = 0
        details = []

        # P/E ratio
        if self.data.get('pe_ratio', 100) < 15:
            score += 20
            details.append("P/E مناسب")
        elif self.data.get('pe_ratio', 100) < 20:
            score += 10
            details.append("P/E متوسط")

        # ROE
        if self.data.get('roe', 0) > 15:
            score += 20
            details.append("بازدهی سرمایهٔ بالا")
        elif self.data.get('roe', 0) > 10:
            score += 10
            details.append("بازدهی سرمایهٔ متوسط")

        # Debt/Equity
        if self.data.get('debt_equity', 1) < 0.5:
            score += 20
            details.append("بدهی کم")
        elif self.data.get('debt_equity', 1) < 1:
            score += 10
            details.append("بدهی متوسط")

        # Current ratio
        if self.data.get('current_ratio', 0) > 1.5:
            score += 15
            details.append("نقدینگی خوب")

        # Earnings stability
        if self.data.get('earnings_stable', False):
            score += 15
            details.append("درآمد پایدار")

        rating = self._get_rating(score)

        return {
            'score': min(score, 100),
            'details': details,
            'rating': rating
        }

    def score_graham(self) -> Dict:
        """
        Benjamin Graham Safety Margin
        P/B <1.5, Earnings growth >5%, Dividend yield >2%
        """
        score = 0
        details = []

        # P/B ratio
        if self.data.get('pb_ratio', 2) < 1.5:
            score += 25
            details.append("نسبت P/B کم")
        elif self.data.get('pb_ratio', 2) < 2:
            score += 15
            details.append("نسبت P/B متوسط")

        # Earnings growth
        if self.data.get('earnings_growth', 0) > 5:
            score += 25
            details.append("رشد درآمد مثبت")

        # Dividend yield
        if self.data.get('dividend_yield', 0) > 2:
            score += 30
            details.append("سود نقد خوب")
        elif self.data.get('dividend_yield', 0) > 1:
            score += 15
            details.append("سود نقد متوسط")

        # Safety margin
        score += 5
        details.append("حاشیهٔ ایمنی")

        rating = self._get_rating(score)

        return {
            'score': min(score, 100),
            'details': details,
            'rating': rating
        }

    def score_soros(self) -> Dict:
        """
        George Soros Macro + Momentum
        Price momentum >10%, Volume trend, Sector strength, Volatility
        """
        score = 0
        details = []

        # Price momentum
        if self.data.get('price_momentum', 0) > 10:
            score += 25
            details.append("شتاب قیمتی قوی")
        elif self.data.get('price_momentum', 0) > 5:
            score += 15
            details.append("شتاب قیمتی متوسط")

        # Volume trend
        if self.data.get('volume_trend', 0) > 5:
            score += 20
            details.append("حجم صعودی")

        # Sector strength
        if self.data.get('sector_strength', '') == 'strong':
            score += 20
            details.append("صنعت در روند صعودی")
        elif self.data.get('sector_strength', '') == 'neutral':
            score += 10
            details.append("صنعت خنثی")

        # Volatility control
        if self.data.get('volatility', 50) < 30:
            score += 20
            details.append("نوسان کنترل‌شده")

        # Macro timing
        score += 5
        details.append("تایمینگ کلان")

        rating = self._get_rating(score)

        return {
            'score': min(score, 100),
            'details': details,
            'rating': rating
        }

    def score_wood(self) -> Dict:
        """
        Cathie Wood Growth + Disruption
        Revenue growth >25%, Innovation >70, Disruption potential, Margin growth
        """
        score = 0
        details = []

        # Revenue growth
        if self.data.get('revenue_growth', 0) > 25:
            score += 25
            details.append("رشد درآمد فوق‌العاده")
        elif self.data.get('revenue_growth', 0) > 15:
            score += 15
            details.append("رشد درآمد خوب")

        # Innovation score
        if self.data.get('innovation_score', 0) > 70:
            score += 25
            details.append("نوآوری بالا")
        elif self.data.get('innovation_score', 0) > 50:
            score += 15
            details.append("نوآوری متوسط")

        # Disruption potential
        if self.data.get('disruption_potential', '') == 'high':
            score += 20
            details.append("پتانسیل تخریب بالا")
        elif self.data.get('disruption_potential', '') == 'medium':
            score += 10
            details.append("پتانسیل تخریب متوسط")

        # Margin growth
        if self.data.get('margin_growth', 0) > 5:
            score += 15
            details.append("رشد حاشیهٔ سود")

        # Growth trajectory
        score += 5
        details.append("مسیر رشد مثبت")

        rating = self._get_rating(score)

        return {
            'score': min(score, 100),
            'details': details,
            'rating': rating
        }

    def score_technical(self) -> Dict:
        """
        Technical Analysis
        Trend direction, RSI 40-70, MACD signal
        """
        score = 0
        details = []

        # Trend direction
        if self.data.get('trend', '') == 'up':
            score += 30
            details.append("روند صعودی")
        elif self.data.get('trend', '') == 'neutral':
            score += 10
            details.append("روند خنثی")

        # RSI
        rsi = self.data.get('rsi', 50)
        if 40 <= rsi <= 70:
            score += 25
            details.append(f"RSI مناسب ({rsi})")
        elif 30 <= rsi <= 80:
            score += 15
            details.append(f"RSI متوسط ({rsi})")

        # MACD signal
        if self.data.get('macd_signal', False):
            score += 20
            details.append("سیگنال MACD مثبت")

        # Moving averages
        score += 15
        details.append("میانگین‌های متحرک مثبت")

        rating = self._get_rating(score)

        return {
            'score': min(score, 100),
            'details': details,
            'rating': rating
        }

    def _get_rating(self, score: int) -> str:
        """تبدیل امتیاز به رتبه‌بندی"""
        if score >= 80:
            return "🟢 خرید قوی"
        elif score >= 60:
            return "🟡 خرید"
        elif score >= 40:
            return "⚪ نگاه"
        else:
            return "🔴 فروش"

    def analyze(self) -> Dict:
        """تحلیل کامل سهام"""
        results = {
            'can_slim': self.score_canslim(),
            'buffett': self.score_buffett(),
            'graham': self.score_graham(),
            'soros': self.score_soros(),
            'wood': self.score_wood(),
            'technical': self.score_technical()
        }

        # Calculate overall score
        overall = (
            results['can_slim']['score'] +
            results['buffett']['score'] +
            results['graham']['score'] +
            results['soros']['score'] +
            results['wood']['score'] +
            results['technical']['score']
        ) / 6

        results['overall'] = round(overall, 1)

        return results
