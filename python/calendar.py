from datetime import datetime
import sys

#特定の年月の日数と1日の曜日を管理
class DateManager:
    def __init__(self, month: int, year: int):
        self.month = month
        self.year = year

    @property
    def current_month_start(self) -> datetime:
        return datetime(self.year, self.month, 1)
    
    @property
    def next_month_start(self) -> datetime:
        return datetime(self.year + 1, 1, 1) if self.month == 12 else datetime(self.year, self.month + 1, 1)
    
    @property
    def days(self) -> int:
        return (self.next_month_start - self.current_month_start).days

    @property
    def first_weekday(self) -> int:
        return self.current_month_start.weekday()

class Calendar:
    def __init__(self, month: int, year: int):
        dateManager = DateManager(month, year)
        self.title = f'{dateManager.month}月 {dateManager.year}'.center(20) 
        self.week = ' '.join(['月', '火', '水', '木', '金', '土', '日'])
        self.first_weekday = dateManager.first_weekday
        self.days = dateManager.days
    
    def create(self) -> str:
        week_days = [' '*2] * self.first_weekday
        days_str = ''
        for day in range(1, self.days + 1):
            week_days.append(f"{day:2}")
            if len(week_days) == 7:
                days_str +=  ('\n' + ' '.join(week_days))
                week_days = []
        if week_days:
            days_str +=  ('\n' + ' '.join(week_days))

        return self.title + '\n' + self.week + days_str
        

def view_calendar(month: int, year: int):
    calendar = Calendar(month, year).create()
    print(calendar)

def parse_arguments():
    if len(sys.argv) not in [1, 3]:
        print("使用方法: python calendar.py -m <月>")
        sys.exit(1)
    year = datetime.now().year
    if len(sys.argv) == 1:
        month = datetime.now().month
        return view_calendar(month, year)
    if len(sys.argv) == 3 and sys.argv[1] == '-m':
        try: 
            month = int(sys.argv[2])
            if not 1 <= month <= 12:
                raise ValueError(f'{month} is neither a month number (1..12) nor a name')
        except ValueError as e:
            print(f"{e}")
            sys.exit(1)
        return view_calendar(month, year)
    else:
        print("使用方法: python calendar.py -m <月>")
        sys.exit(1)

if __name__ == '__main__':
    parse_arguments()
