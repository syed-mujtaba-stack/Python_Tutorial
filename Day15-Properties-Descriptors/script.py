# Day 15 Script: Properties & Descriptors Demo

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError('Temperature below absolute zero!')
        self._temperature = value

c = Celsius(25)
c.temperature = 30
print('Celsius:', c.temperature)
