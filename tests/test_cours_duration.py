import sys
sys.path.append("..")
import cours_duration as cd # custom module
import unittest
from itertools import chain

class TestCoursDuration(unittest.TestCase):
    def test_get_courses_list(self):
        """Тест создания списка курсов с индексами и количеством преподавателей"""
        courses_list = cd.get_courses_list(cd.COURSES, cd.MENTORS, cd.DURATION)
        self.assertEqual(len(courses_list), len(cd.COURSES))
        index = 0
        for course in courses_list:
            self.assertIn(course["title"], cd.COURSES)
            self.assertIn(course["mentors"], cd.MENTORS)
            self.assertIn(course["duration"], cd.DURATION)
            self.assertEqual(course["index"], index)
            index += 1

    def test_get_mentor_count(self):
        """Тест подсчёта количества преподавателей"""
        mentor_count = cd.get_mentor_count(cd.MENTORS)
        i = 0
        for count in mentor_count:
            self.assertEqual(count, len(cd.MENTORS[i]))
            i += 1

    def test_get_indexes(self):
        """Тест получения индексов, отсортированных по длительности и количеству преподавателей"""
        courses = ["Курс A", "Курс B", "Курс C"]
        mentors = [
            ["Анна", "Иван", "Мария"],  
            ["Петр", "Сергей"],        
            ["Елена", "Ольга", "Алексей", "Дмитрий"]  
        ]
        durations = [20, 10, 15]
        courses_list = cd.get_courses_list(courses, mentors, durations)
        mentor_count = cd.get_mentor_count(mentors)
        indx_dur, indx_ment = cd.get_indexes(courses_list, mentor_count, durations)

        self.assertEqual(indx_dur, [1, 2, 0])
        self.assertEqual(indx_ment, [1, 0, 2])

    def test_analyze_correlation(self):
        """Тест анализа корреляции с параметризацией"""
        test_cases = [
            ([0, 1, 2], [0, 1, 2], "Связь есть"),
            ([1, 0, 2], [1, 0, 2], "Связь есть"),
            ([0, 1, 2], [2, 1, 0], "Связи нет"),
            ([1, 2, 0], [1, 0, 2], "Связи нет"),
        ]

        for dur, ment, expected_corr in test_cases:
            with self.subTest(dur=dur, ment=ment):
                result = cd.analyze_correlation(dur, ment)
                self.assertEqual(result["correlation"], expected_corr)
                self.assertEqual(result["order_by_duration"], dur)
                self.assertEqual(result["order_by_mentors"], ment)
            

if __name__ == '__main__':
    unittest.main()