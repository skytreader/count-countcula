class Counter(object):
    
    def __init__(self):
        self.counter = 0

    def incr(self):
        self.counter += 1

    def reset(self):
        self.counter = 0
