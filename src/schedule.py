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

    def time_until(self, current_datetime: datetime) -> timedelta:
        """
        現在時刻からの出発までの時間差を計算する

        Args:
            current_datetime (datetime): 現在の日時

        Returns:
            timedelta: 出発までの時間差
        """
        # 出発時刻をtimeオブジェクトに変換
        dep_time = datetime.strptime(self.departure_time, "%H:%M").time()
        
        # 現在の日付と出発時刻を組み合わせてdatetimeオブジェクトを作成
        dep_datetime = datetime.combine(current_datetime.date(), dep_time)
        
        # 出発時刻が過ぎている場合は翌日に設定
        if dep_datetime < current_datetime:
            dep_datetime += timedelta(days=1)
        
        return dep_datetime - current_datetime