
import datetime
import time

class TimedEvent:
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime <= datetime.datetime.now()


class Timer:
    ''' simple simulator for calling events i.e. fxns. after a time lapse'''
    def __init__(self):
        self.events = []
        
    def call_after(self, delay, callback):
        ''' for scheduling execution of a call back function after a delay'''
        end_time = datetime.datetime.now() + \
                       datetime.timedelta(seconds = delay)

        self.events.append(TimedEvent(end_time, callback))
    
    def run(self):
        ''' Executing call back functions due for execution '''
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
                time.sleep(0.5)

def format_time(message, *args):
    now = datetime.datetime.now().strftime("%I:%M:S")
    print(message.format(*args, now = now))

def one(timer):
    format_time("{now}: Called One")

def two(timer):
    format_time("{now}: Called Two")

def three(timer):
    format_time("{now}: Called Three")

class Repeater:
    def __init__(self):
        self.count = 0

    def repeater(self, timer):
        format_time("{now}: repeat {0}", self.count)
        self.count += 1
        timer.call_after(5, self.repeater)
