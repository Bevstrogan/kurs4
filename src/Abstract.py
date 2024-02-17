from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def get_vacancy_from_api(self):
        pass

    @abstractmethod
    def save_info(self):
        pass