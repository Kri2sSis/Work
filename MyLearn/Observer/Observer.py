from abc import ABC, abstractclassmethod


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribe = set()

    def subscribe(self, subscribe):
        self.__subscribe.add(subscribe)

    def unsubscribe(self, subscribe):
        self.__subscribe.remove(subscribe)

    def notify(self, message):
        for subscribe in self.__subscribe:
            subscribe.update(message)


class AbstractObserver(ABC):
    @abstractclassmethod
    def update(cls, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achive:dict):
        self.achievements.add(achive['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, achive:dict):
        if achive not in self.achievements:
            self.achievements.append(achive)

