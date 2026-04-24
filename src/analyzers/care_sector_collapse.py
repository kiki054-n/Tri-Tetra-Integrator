"""
TTT Care Sector Distortion Analyzer
Logic by Naoyuki Kawakami
"""

class CareIntegrator:
    def __init__(self, budget_change, inflation, labor_intensity, real_wage):
        self.real_flow = budget_change - inflation  # 実質予算還流率
        self.strain = labor_intensity               # 現場の負荷(X+)
        self.satisfaction = real_wage               # 現場への還元(X-)

    def diagnose(self):
        # 宇宙の公理に基づき、歪み係数(DF)を算出
        df = (self.strain / self.satisfaction) - self.real_flow
        
        if df > 1.5:
            return f"【判定：臨界点】 歪み係数 {df:.2f}。現場の生命エネルギーが搾取されています。"
        return f"【判定：健全】 歪み係数 {df:.2f}。系は安定しています。"
