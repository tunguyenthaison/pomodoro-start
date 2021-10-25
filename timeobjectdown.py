import time

def get_current():
    return time.time()

class TimeObjectDown:
    def __init__(self, init):
        self.max = init * 60
        self.start = time.time()
        self.remain = self.max - self.start

    def reset_time(self):
        self.start = time.time()
        self.remain = self.max - self.start

    def get_timelapse(self):
        return self.max - int(get_current() - self.start)

    def get_minutes(self):
        return int(self.get_timelapse() // 60)

    def get_seconds(self):
        return int(self.get_timelapse()) - self.get_minutes() * 60

    def get_text(self):
        seconds = self.get_seconds()
        minutes = self.get_minutes()
        if minutes < 10:
            minutes = '%02d' % minutes
        else:
            minutes = str(minutes)

        if seconds < 10:
            seconds = '%02d' % seconds
        else:
            seconds = str(seconds)

        time_text = f"{minutes}:{seconds}"
        return time_text
