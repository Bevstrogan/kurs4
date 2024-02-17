import json
from typing import Any
from src.config import DATA
import requests
from src.Abstract import Abstract


class GetVacancies(Abstract):
    all = []

    def __init__(self, name_vacancy: str):
        self.name_vacancy: str = name_vacancy
        self.message = "Вакансии найдены"
        self.vacancy_all = self.get_vacancy_from_api()

    def __repr__(self):
        return f"{self.vacancy_all}"

    def get_vacancy_from_api(self) -> str | Any:
        """Получает вакансии по API"""

        if isinstance(self.name_vacancy, str):
            keys_response = {'text': f'NAME:{self.name_vacancy}', 'area': 113, 'per_page': 100, }
            info = requests.get(f'https://api.hh.ru/vacancies', keys_response)
            return json.loads(info.text)['items']
        else:
            self.message = "Вакансии не найдены"
            return self.message

    def save_info(self) -> str or list:
        """Создает json файл с вакансиями"""

        if len(self.vacancy_all) == 0:
            self.message = "Вакансии не найдены"
            return self.message
        else:
            with open(DATA, 'w', encoding='utf-8') as file:
                info = {}
                count = 1
                for vacancy in self.vacancy_all:
                    if vacancy['salary'] == None:
                        info[f'Вакансия №{count}'] = [{"Название вакансии": vacancy['name']},
                                                    {"Работодатель": vacancy['employer']['name']},
                                                    {"Описание вакансии": vacancy['snippet']['responsibility']},
                                                    {"Требования": vacancy['snippet']['requirement']},
                                                    {"Опыт работы": vacancy['experience']['name']},
                                                    {"Город": vacancy['area']['name']},
                                                    {"URL": f"{vacancy['alternate_url']}\n"}]
                        count += 1
                    else:
                        info[f'Вакансия №{count}'] = [{"Название вакансии": vacancy['name']},
                                                      {"Работодатель": vacancy['employer']['name']},
                                                      {"Описание вакансии": vacancy['snippet']['responsibility']},
                                                      {"Требования": vacancy['snippet']['requirement']},
                                                      {"Опыт работы": vacancy['experience']['name']},
                                                      {"Город": vacancy['area']['name']},
                                                      {"Зарплата от": vacancy['salary']['from']},
                                                      {"Зарплата до": vacancy['salary']['to']},
                                                      {"URL": f"{vacancy['alternate_url']}\n"}
                                                      ]
                        count += 1
                json.dump(info, file, ensure_ascii=False, indent=2)