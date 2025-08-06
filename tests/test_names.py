import sys
sys.path.append("..")
import names as n # custom module
import unittest
from itertools import chain


class TestNames(unittest.TestCase):
    def test_get_mentors_list(self):
        mentors_list = n.get_mentors_list(n.COURSES, n.MENTORS, n.DURATION)
        for mentor in mentors_list:
            self.assertIn('course', mentors_list[0])
            self.assertIn('name', mentors_list[0])
            self.assertIn('surname', mentors_list[0])

    def test_get_courses_dict(self):
        """Тест создания словаря курсов"""
        courses_dict = n.get_courses_dict(n.COURSES)
        for course in courses_dict:
            self.assertEqual(courses_dict[course], [])
    
    def test_get_courses_mentors_dict(self):
        """Тест создания словаря курсов и менторов"""
        if not n.COURSES:
            self.skipTest("Список курсов пуст")
        if not n.MENTORS:
            self.skipTest("Список менторов пуст")
        mentors_list = n.get_mentors_list(n.COURSES, n.MENTORS, n.DURATION)
        courses_dict = n.get_courses_dict(n.COURSES)
        filled_dict = n.get_courses_mentors_dict(courses_dict, mentors_list)
        for course in filled_dict:
            self.assertIn(course, n.COURSES)
            for mentor in filled_dict[course]:
                self.assertIn(mentor, chain(*n.MENTORS))

    def test_get_result(self):
        """Тест форматирования результата"""
        input_dict = {
            "Java-разработчик": ["Иван Иванов", "Анна Петрова"],
            "Python-разработчик": []
        }
        result = n.get_result(input_dict)
        expected = ["На курсе Java-разработчик есть тёзки: Анна Петрова, Иван Иванов"]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()