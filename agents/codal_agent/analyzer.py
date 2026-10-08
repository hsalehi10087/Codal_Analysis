#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stock Analyzer
معیارهای سرمایه‌گذاری مختلف را امتیاز دهی می‌کند
"""

from typing import Dict, List

class StockAnalyzer:
    def __init__(self, stock_data: Dict):
        self.data = stock_data
        self.scores = {}

    def analyze(self) -> Dict:
        """
        تمام معیارها را تحلیل می‌کند
        """
        return {
            'can_slim': self.score_canslim(),
            'buffett': self.score_buffett(),
            'graham': self.score_graham(),
            'soros': self.score_soros(),
            'wood': self.score_wood(),
            'technical': self.score_technical(),
            'overall': self.calculate_overall()
        }

    def score_canslim(self) -> Dict:
        """
        CAN SLIM (O'Neil)
        C: Current Earnings (فروش و سود موجود)
        A: Annual Growth (رشد سالانه)
        N: New (محصولات جدید)
        S: Supply/Demand
        L: Leader (نخست در صنعت)
        I: Industry Trend
        M: Market Cap
        """
        score = 0
        details = []

        # C: فروش فعلی
        if self.data.get('sales_growth', 0) > 0:
            score += 25
            details.append('✅ فروش رو به افزایش')

        # A: رشد سالانه
        if self.data.get('annual_growth', 0) > 15:
            score += 25
            details.append('✅ رشد سالانه بالا (>15%)')

        # N: محصولات جدید
        if self.data.get('has_new_products', False):
            score += 15
            details.append('✅ محصولات جدید')

        # L: رهبر صنعت
        if self.data.get('market_position', 'low') == 'leader':
            score += 20
            details.append('✅ رهبر در صنعت')

        # M: Market Cap
        if self.data.get('market_cap', 0) > 1000000000:
            score += 15
            details.append('✅ Market Cap بالا')

        return {
            'score': min(score, 100),
            'details': details,
            'rating': 'STRONG' if score >= 75 else 'GOOD' if score >= 50 else 'WEAK'
        }

    def score_buffett(self) -> Dict:
        """
        Warren Buffett Value Investing
        - P/E کم
        - ROE بالا
        - Debt کم
        - Consistent Earnings
        """
        score = 0
        details = []

        # P/E < 15
        pe = self.data.get('pe_ratio', 999)
        if pe < 15 and pe > 0:
            score += 25
            details.append(f'✅ P/E پایین ({pe})')

        # ROE > 15%
        if self.data.get('roe', 0) > 15:
            score += 25
            details.append(f'✅ ROE بالا ({self.data["roe"]}%)')

        # Debt/Equity < 0.5
        if self.data.get('debt_equity', 999) < 0.5:
            score += 20
            details.append('✅ بدهی کم')

        # Current Ratio > 1.5
        if self.data.get('current_ratio', 0) > 1.5:
            score += 15
            details.append('✅ نقدینگی مناسب')

        # Earnings Stability
        if self.data.get('earnings_stable', False):
            score += 15
            details.append('✅ درآمد پایدار')

        return {
            'score': min(score, 100),
            'details': details,
            'rating': 'BUY' if score >= 70 else 'HOLD' if score >= 40 else 'SELL'
        }

    def score_graham(self) -> Dict:
        """
        Benjamin Graham Safety Margin
        """
        score = 0
        details = []

        # Price to Book < 1.5
        if self.data.get('pb_ratio', 999) < 1.5:
            score += 30
            details.append('✅ Price to Book مناسب')

        # Earnings Growth > 5%
        if self.data.get('earnings_growth', 0) > 5:
            score += 25
            details.append('✅ رشد درآمد')

        # Dividend Yield > 2%
        if self.data.get('dividend_yield', 0) > 2:
            score += 20
            details.append('✅ سود سهام خوب')

        return {
            'score': min(score, 100),
            'details': details,
            'rating': 'SAFE' if score >= 60 else 'RISKY'
        }

    def score_soros(self) -> Dict:
        """
        George Soros Macro + Momentum
        """
        score = 0
        details = []

        # Price Momentum
        if self.data.get('price_momentum', 0) > 10:
            score += 30
            details.append('✅ قیمت رو به افزایش')

        # Volume Trend
        if self.data.get('volume_trend', 0) > 0:
            score += 25
            details.append('✅ حجم معاملات بالا')

        # Sector Strength
        if self.data.get('sector_strength', 'weak') == 'strong':
            score += 25
            details.append('✅ صنعت قوی')

        # Volatility (higher can be good for traders)
        if self.data.get('volatility', 0) > 15:
            score += 20
            details.append('✅ نوسان‌پذیری بالا (فرصت)')

        return {
            'score': min(score, 100),
            'details': details,
            'rating': 'BUY' if score >= 70 else 'HOLD' if score >= 40 else 'SELL'
        }

    def score_wood(self) -> Dict:
        """
        Cathie Wood Growth + Disruption
        """
        score = 0
        details = []

        # Revenue Growth > 25%
        if self.data.get('revenue_growth', 0) > 25:
            score += 30
            details.append('✅ رشد فروش بالا (>25%)')

        # Innovation Score
        if self.data.get('innovation_score', 0) > 70:
            score += 25
            details.append('✅ نوآوری بالا')

        # Market Disruption Potential
        if self.data.get('disruption_potential', 'low') == 'high':
            score += 25
            details.append('✅ پتانسیل تحریک بازار')

        # Profit Margin Growth
        if self.data.get('margin_growth', 0) > 0:
            score += 20
            details.append('✅ حاشیهٔ سود بهتر')

        return {
            'score': min(score, 100),
            'details': details,
            'rating': 'STRONG' if score >= 70 else 'GOOD' if score >= 45 else 'WEAK'
        }

    def score_technical(self) -> Dict:
        """
        تحلیل تکنیکال
        """
        score = 0
        details = []

        # Trend
        if self.data.get('trend', 'down') == 'up':
            score += 30
            details.append('✅ روند صعودی')

        # RSI
        rsi = self.data.get('rsi', 50)
        if 40 < rsi < 70:
            score += 25
            details.append(f'✅ RSI مناسب ({rsi})')

        # MACD
        if self.data.get('macd_signal', False):
            score += 25
            details.append('✅ MACD مثبت')

        return {
            'score': min(score, 100),
            'details': details,
            'rating': 'BULLISH' if score >= 70 else 'NEUTRAL' if score >= 40 else 'BEARISH'
        }

    def calculate_overall(self) -> int:
        """
        امتیاز کل
        """
        scores = [
            self.score_canslim()['score'],
            self.score_buffett()['score'],
            self.score_graham()['score'],
            self.score_soros()['score'],
            self.score_wood()['score'],
            self.score_technical()['score']
        ]
        return int(sum(scores) / len(scores))

if __name__ == "__main__":
    # Test data
    test_data = {
        'sales_growth': 25,
        'annual_growth': 30,
        'has_new_products': True,
        'market_position': 'leader',
        'market_cap': 5000000000,
        'pe_ratio': 12,
        'roe': 20,
        'debt_equity': 0.3,
        'current_ratio': 2.0,
        'earnings_stable': True,
        'pb_ratio': 1.2,
        'earnings_growth': 15,
        'dividend_yield': 3.5,
        'price_momentum': 15,
        'volume_trend': 10,
        'sector_strength': 'strong',
        'volatility': 20,
        'revenue_growth': 35,
        'innovation_score': 75,
        'disruption_potential': 'high',
        'margin_growth': 5,
        'trend': 'up',
        'rsi': 55,
        'macd_signal': True
    }

    analyzer = StockAnalyzer(test_data)
    results = analyzer.analyze()

    print("📊 تحلیل نمونه:")
    for criterion, result in results.items():
        if isinstance(result, dict) and 'score' in result:
            print(f"{criterion}: {result['score']} ({result.get('rating', '')})")
