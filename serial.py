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
        """initializes an instance with the starting number and counter"""
        self.start = start
        self.counter = 0

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next ={self.generate()}>"

    def generate(self):
        """returns the next sequential serial number"""
        self.counter += 1
        return (self.start - 1) + self.counter

    def reset(self):
        """reset the counter back to the original start number"""
        self.counter = 0
