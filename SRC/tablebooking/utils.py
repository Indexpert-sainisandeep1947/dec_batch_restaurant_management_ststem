from datetime import datetime, timedelta

def time_diff(t1, t2):
    fmt = "%H:%M"
    t1 = datetime.strptime(t1, fmt)
    t2 = datetime.strptime(t2, fmt)
    diff = abs((t1 - t2).total_seconds()) / 3600
    return diff

def is_valid_date(date_str):
    try:
        booking_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        return today <= booking_date <= today + timedelta(days=30)
    except:
        return False
