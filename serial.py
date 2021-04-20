class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        """the starting number"""
        self.start = start
        self.counter = 0

    def generate(self):
        """returns the next sequential number"""
        self.counter += 1
        return (self.start - 1) + self.counter

    def reset(self):
        """reset the number back to the original start"""
        self.counter = 0

