import threading
import time

class SleepyWorker(threading.Thread):
    def __init__(self,n,**kwargs):
        self._seconds = n
        super(SleepyWorker,self).__init__(**kwargs)
        self.start()

    

    def _sleep_a_little(self):
        time.sleep(self._seconds)


    def run(self):
        self._sleep_a_little() 