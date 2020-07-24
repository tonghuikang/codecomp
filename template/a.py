from datetime import date

class NextOlympics:
    def countDays(self, date_string):
        dest = date(2021, 7, 23)
        today = date(int(date_string[:4]), int(date_string[5:7]), int(date_string[-2:]))
        return int((dest - today).days)