from src.Iteractions import Interaction

def main():
    user_input = input("Пожалуйста напишите название вакансии которую вы ищите: ")

    while True:
        users_salary = input("Напишите желаемую зарплату: ")
        if users_salary.isdigit():
            break
        print("\nПожалуйста введите зарплату цифрами или нажмите enter:")

    user = Interaction(user_input)

    while True:
        users_city = input("Введите ваш город: ").capitalize()
        if users_city.isalpha():
            break
        print("\nРезультатов по данному городу не найдено.\n")



    user.sorted_salary(user.vacancy_all, int(users_salary), users_city)
    user.get_top_vacancies(user.sort_salary)

    user.make_info(user.top_salary)


    while True:
        number_vacancy = input("Введите номер вакансии в зависимости от зарплаты\n")

        if number_vacancy.isdigit():
            break


    user.save_info()

    print(user.last_info(user.vacancies_list, number_vacancy))

if __name__ == '__main__':
    main()