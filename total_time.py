def total_time_calculate(n: int) -> str:
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
    for i in range(n):
        video_time: int = int(input(f'Video #{i+1:03d}: '))
        s: int = video_time % 100
        video_time //= 100
        m: int = video_time % 100
        h: int = video_time // 100
        seconds += s
        minutes += seconds // 60
        seconds %= 60
        minutes += m
        hours += minutes // 60
        minutes %= 60
        hours += h
        days += hours // 24
        hours %= 24
    total: str = f'{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}'
    return total
