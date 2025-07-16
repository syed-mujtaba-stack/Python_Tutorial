# Day 4 Script: Advanced OOP Demo
from abc import ABC, abstractmethod

class LoggerMixin:
    def log(self, message):
        print(f'[LOG] {message}')

class Service(LoggerMixin):
    def process(self):
        self.log('Processing started')
        # ...
        self.log('Processing finished')

svc = Service()
svc.process()
