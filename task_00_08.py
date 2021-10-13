def time_formatter(passed_minutes):
    minutes_in_an_hour = 60

    hours = passed_minutes // minutes_in_an_hour
    minutes = passed_minutes % minutes_in_an_hour

    hours_descriptor = 'hour' if hours == 1 else 'hours'
    minutes_descriptor = 'minute' if minutes == 1 else 'minutes'

    return f'{hours} {hours_descriptor}, {minutes} {minutes_descriptor}'
