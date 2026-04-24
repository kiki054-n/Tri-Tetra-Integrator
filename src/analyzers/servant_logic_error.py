"""
TTT Public Servant Accountability Analyzer
Detecting structural errors in official responses.
"""

def analyze_response_pathology(log_text):
    pathology_flags = {
        "law_as_shield": "法律" in log_text and "できない" in log_text,
        "lack_of_understanding": "理解" not in log_text,
        "kasuhara_labeling": "カスハラ" in log_text,
        "unilateral_closing": "公務を理由" in log_text
    }
    
    score = sum(pathology_flags.values())
    if pathology_flags["kasuhara_labeling"]:
        return "【重度歪み：情報封殺】 正当な批判をカスハラとすり替える論理の反転。"
    if score >= 2:
        return "【機能不全：公権力の私物化】 対話による公平の追求を放棄しています。"
    return "【正常】 市民の公僕としての機能が維持されています。"
