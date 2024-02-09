import requests
from datetime import datetime
import json
from abc import ABC, abstractmethod


class ApiManager(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class Vacancy:
    def __init__(self, name, page, top_N):
        self.name = name
        self.page = page
        self.top_n = top_N

    def __repr__(self):
        return f"{self.name}"


class HeadHunter(Vacancy, ApiManager):
    def __init__(self, name, page, top_N):
        super().__init__(name, page, top_N)
        self.url = 'https://api.hh.ru'

    def get_vacancies(self):
        data = requests.get(f"{self.url}/vacancies",
                            params={'text': self.name, 'page': self.page, 'per_page': self.top_n}).json()
        return data

    def load_vacancy(self):
        data = self.get_vacancies()
        vacancies = []
        for vacancy in data.get('items', []):
            published_at_str = vacancy['published_at']
            published_at_date = datetime.strptime(published_at_str,"%Y-%m-%dT%H:%M:%S%z").date()
            vacancy_info = {
                "id": vacancy['id'],
                "name": vacancy['name'],
                "salary_from": vacancy['salary']['from']
                if vacancy.get('salary') else None,
                "salary_to": vacancy['salary']['to']
                if vacancy.get('salary') else None,
                "responsibility": vacancy['snippet']
                ['responsibility'],
                "date": published_at_date.strftime("%d.%m.%Y")
            }
            vacancies.append(vacancy_info)

        return vacancies

def find_vacancy():

    name = input('Введите вакансию: ')
    top_n = input('Введите кол-во вакансий: ')
    page = int(input('Введите страницу: '))
    results = HeadHunter(name, page, top_n)
    vacancies_dict = {'HeadHunter': results.load_vacancy()}

    with open('Found_Vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(vacancies_dict, file, ensure_ascii=False, indent=2)

        results.page = page
        hh_data = results.load_vacancy()

        vacancies_dict['HH'] = hh_data

        for hh in vacancies_dict['HH']:
            print(
                f"\nid - {hh['id']}\n"
                f"Должность - {hh['name']}\n"
                f"З.п от - {hh['salary_from']}\n"
                f"З.п до - {hh['salary_to']}\n"
                f"Описание - {hh['responsibility']}\n"
                f"Дата - {hh['date']}\n")

find_vacancy()