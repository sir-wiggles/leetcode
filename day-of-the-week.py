class Solution:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def isLeapYear(self, year: int) -> bool:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def daysSinceStart(self, day:int, month:int, year:int) -> int:
        days = 0
        for y in range(1970, year):
            days += 365
            if self.isLeapYear(y):
                days += 1

        days += sum(self.days_in_month[:month-1])
        if self.isLeapYear(year) and month > 2:
            days += 1

        days += day 
        return days

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date = self.daysSinceStart(day, month, year)
        return self.days_of_week[(date - 4) % 7]

import unittest
class Test(unittest.TestCase):

    def test1(self):
        day = 12
        month = 3
        year = 2020
        self.assertEqual(Solution().dayOfTheWeek(day, month, year), "Thursday")
    def test2(self):
        day = 15
        month = 6
        year = 1985
        self.assertEqual(Solution().dayOfTheWeek(day, month, year), "Saturday")


unittest.main(exit=False)
