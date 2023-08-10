"""Python serial number generator."""

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
    #initializes the generator at 100 and starts
    def __init__(self, start=100):
        self.start = start
        self.current = current
    # sets the serial number based what it is and increments by 1
    def generate(self):
        serial_number = self.current
        self.current += 1
        return serial_number
    # resets back to the start
    def reset(self):
        self.current = self.start

