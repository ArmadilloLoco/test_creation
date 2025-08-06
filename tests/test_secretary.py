import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import secretary as sec # custom module
import unittest

class TestDocumentFunctions(unittest.TestCase):
    def test_get_name(self):
        """Параметризованный тест для get_name"""
        cases = [
            ("2207 876234", "Василий Гупкин"),
            ("11-2", "Геннадий Покемонов"),
            ("10006", "Аристарх Павлов"),
            ("5455 028765", "Василий Иванов"),
            ("101", "Документ не найден"),
            ("", "Документ не найден"),
            ("999", "Документ не найден"),
        ]
        for number, expected in cases:
            with self.subTest(number=number, expected=expected):
                result = sec.get_name(number)
                self.assertEqual(result, expected)

    def test_get_directory(self):
        """Параметризованный тест для get_directory"""
        cases = [
            ("2207 876234", "1"),
            ("11-2", "1"),
            ("5455 028765", "1"),
            ("10006", "2"),
            ("999", "Полки с таким документом не найдено"),
            ("", "Полки с таким документом не найдено"),
        ]
        for number, expected in cases:
            with self.subTest(number=number, expected=expected):
                result = sec.get_directory(number)
                self.assertEqual(result, expected)

    def test_add(self):
        """Тест: добавление документа на существующую полку"""
        result = sec.add('international passport', '311 020203', 'Александр Пушкин', 3)
        self.assertTrue(result)
        self.assertIn('311 020203', sec.DIRS['3'])

    def test_add_no_self(self):
        """Тест: попытка добавить документ на несуществующую полку"""
        result = sec.add('passport', '123', 'Иван Иванов', 999)
        self.assertFalse(result)
        self.assertNotIn('999', sec.DIRS)


if __name__ == '__main__':
    unittest.main()