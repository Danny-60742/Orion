from datetime import datetime

def get_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time
