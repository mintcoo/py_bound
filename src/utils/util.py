from src.utils.constants import ONE_SECOND_IN_MILLISECONDS


def format_time(milliseconds):
    minutes_string = str((milliseconds // ONE_SECOND_IN_MILLISECONDS) // (60)).zfill(2)
    seconds_string = str((milliseconds // ONE_SECOND_IN_MILLISECONDS) % (60)).zfill(2)
    milliseconds_string = str(milliseconds % ONE_SECOND_IN_MILLISECONDS // 10).zfill(2)
    time = f"{minutes_string} : {seconds_string} : {milliseconds_string}"
    return str(time)
