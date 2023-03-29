import datetime

__all__ = ['check_date']


def terminal_run():
    user_check = input('Please, enter a date: ')
    print(f'result: {check_date(user_check)}')


def check_date(date_: str):
    try:
        datetime.datetime.strptime(date_, '%Y.%m.%d')
        return True
    except:
        return False


def leap_year_check(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


if __name__ == '__main__':
    terminal_run()
