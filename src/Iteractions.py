from collections import defaultdict
from src.CompareVacancies import CompareVacancies
from src.Abstract import Abstract

class Interaction(CompareVacancies):
    def __init__(self, vacancy_name):
        super().__init__(vacancy_name)
        self.get_vacancy_from_api()
        self.vacancies_list = defaultdict(list)

    def __str__(self):
        self.message = "Вакансии не найдены" if len(self.vacancy_all) == 0 else self.message
        return (f"Название вакансии для поиска: {self.vacancy_name}\n"
                f"Количество вакансий: {len(self.vacancy_all)}\n"
                f"Состояние: {self.message}")

    def make_info(self, top_salary: dict) -> list:
        """Создает информация об вакансии"""
        print(f"Список самых высокооплачиваемых вакансий:")

        count = 1
        for top, vacancies in top_salary.items():

            print(f"{count}. Вакансии с зарплатой {top} - найдено {len(vacancies)}", end='\n')

            for value in vacancies:
                self.vacancies_list[count].extend([{"Название вакансии": value['name']},
                                                   {"Работодатель": value['employer']['name']},
                                                   {"Описание вакансии": value['snippet']['responsibility']},
                                                   {"Требования": value['snippet']['requirement']},
                                                   {"Опыт работы": value['experience']['name']},
                                                   {"Зарплата от": value['salary']['from']},
                                                   {"Зарплата до": value['salary']['to']},
                                                   {"Город": value['area']['name']},
                                                   {"URL": f"{value['alternate_url']}\n"}])
            count += 1

    @staticmethod
    def last_info(top_salary: dict, number_of_vacancies: int):
        """Выводит информацию об выбранной высокооплачиваемой вакансии"""
        print()
        info = []
        for params_vacancy in top_salary[int(number_of_vacancies)]:
            for key, val in params_vacancy.items():
                info.append("{0}: {1}".format(key, val))
        return '\n'.join(info)