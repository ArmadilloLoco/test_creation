'''Вам нужно проверить, зависят ли друг от друга продолжительность курса 
и количество преподавателей на этом курсе.
Если отсортировать курсы по продолжительности 
и по количеству преподавателей и окажется, 
что курсы идут в одном и том же порядке, значит связь есть. 
Если порядок будет разный – значит связи нет.'''


COURSES = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
MENTORS = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
DURATION = [14, 20, 12, 20]


def get_courses_list(courses: list, mentors: list, durations: list) -> list:
    '''Создает список словарей с информацией о преподавателях'''
    courses_list = []
    index = 0
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, 
                       "mentors":mentor, 
                       "duration":duration, 
                       "index":index, 
                       "count":len(mentor)}
        courses_list.append(course_dict)
        index += 1
    return courses_list

def get_mentor_count(mentors: list) -> list:
    mentor_count = list()
    for m in mentors:
        mentor_count.append(len(m))
    return mentor_count

def get_indexes(courses_list: list, mentor_count: list, durations: list) -> tuple[list, list]:
    ment_sorted = sorted(mentor_count)
    indx_ment = list()
    dur_sorted = sorted(durations)
    indx_dur = list()
    for d, m in zip(sorted(durations), sorted(mentor_count)):
        for c in courses_list:
            if d == c['duration'] and c['index'] not in indx_dur:
                indx_dur.append(c['index'])
            if m == c["count"] and c['index'] not in indx_ment:
                indx_ment.append(c['index'])
    return indx_dur, indx_ment

def print_result(indx_dur: list, indx_ment: list):
    print("Связь есть" if indx_dur == indx_ment else "Связи нет")
    print(f"Порядок курсов по длительности: {indx_dur}")
    print(f"Порядок курсов по количеству преподавателей: {indx_ment}")


if __name__ == '__main__':
    courses_list = get_courses_list(COURSES, MENTORS, DURATION)
    mentor_count = get_mentor_count(MENTORS)
    indx_dur, indx_ment = get_indexes(courses_list, mentor_count, DURATION)
    print_result(indx_dur, indx_ment)