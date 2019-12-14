import signal

class Signal:
    def __init__(self):
        self.kill = False
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)
    
    def shutdown(self, signum, frame):
        self.kill = True