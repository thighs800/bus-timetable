from datetime import time, datetime, taimedalta

class ScheduleEntry:
    """
    時刻表の最小単位（個別の便）のデータ構造を定義するクラス 

    Attributes:
    departure_time (str): 出発時刻を表す文字列
    """
    def __init__(self, departure_time: str):
        self.departure_time = departure_time

    def __repr__(self) -> str:
        """
        オブジェクトの文字列表現を返す

        Returns:
            str: 出発時刻の文字列
        """
        return f"ScheduleEntry(departure_time='{self.departure_time}')"
    
    def __str__(self) -> str:
        """
        人間向けの説明を返す

        Returns:
            str: 出発時刻の説明
        """
        return f"出発時刻: {self.departure_time}" 