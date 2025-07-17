# Day 39 Script: Design Patterns Demo

# 1. Singleton with Metaclass
class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonType):
    def __init__(self):
        print('Initializing database...')

# 2. Observer Pattern
class NewsAgency:
    def __init__(self):
        self._subscribers = []
    
    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)
    
    def publish_news(self, news):
        for subscriber in self._subscribers:
            subscriber(news)

def email_subscriber(news):
    print(f"Email: {news}")

def sms_subscriber(news):
    print(f"SMS: {news}")

# Demo
print("Singleton Pattern:")
db1 = Database()
db2 = Database()
print(f"Same instance? {db1 is db2}")

print("\nObserver Pattern:")
agency = NewsAgency()
agency.subscribe(email_subscriber)
agency.subscribe(sms_subscriber)
agency.publish_news("Python 3.12 released!")
