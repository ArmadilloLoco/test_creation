'''В этом задании вы должны для каждого курса в отдельности подсчитать, 
сколько на нём встречается преподавателей-тёзок.
Вы должны вывести название курса и список преподавателей-тёзок 
(с именем и фамилией в алфавитном порядке), 
которые обучают студентов в рамках этого курса.'''

COURSES = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
MENTORS = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
DURATION = [14, 20, 12, 20]

def get_mentors_list(courses: list, mentors: list, durations: list) -> list:
    '''Создает список словарей с информацией о преподавателях'''
    mentors_list = list()
    for c, m, d in zip(courses, mentors, durations):
        for name in m:
            mentors_dict = {'course': c,
                            'name':name.split()[0],
                            'surname':name.split()[1],
                            'dur': d}
            mentors_list.append(mentors_dict)
    return mentors_list

def get_courses_dict(courses: list) -> dict:
    '''Создает словарь с курсами и пустыми списками'''
    courses_dict = dict()
    for index, val in enumerate(courses):
        courses_dict[val] = list()
    return courses_dict

def get_courses_mentors_dict(courses_dict: dict, mentors_list: list) -> dict:
    '''Создает словарь с курсами и списками преподавателей'''
    for mentor in mentors_list:
        for serch in mentors_list:
            if mentor['surname'] != serch['surname'] \
            and mentor['name'] == serch['name'] \
            and mentor['course'] == serch['course']:
                full_name = mentor['name'] + " " + mentor['surname']
                if full_name not in courses_dict[mentor['course']]:
                    courses_dict[mentor['course']].append(full_name)
    return courses_dict

def print_courses_mentors(courses_dict: dict):
    '''Выводит список преподавателей'''
    for key in courses_dict:
        names = ', '.join(sorted(courses_dict[key]))
        print(f'На курсе {key} есть тёзки: {names}')


if __name__ == '__main__':
    mentors_list = get_mentors_list(COURSES, MENTORS, DURATION)
    courses_dict = get_courses_dict(COURSES)
    courses_mentors_dict = get_courses_mentors_dict(courses_dict, mentors_list)
    print_courses_mentors(courses_mentors_dict)
