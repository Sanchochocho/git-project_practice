import unittest
import os
from unittest.mock import patch
from utils import create_task, change_task, delete_task


class TestTasks(unittest.TestCase):

    def setUp(self):
        self.file_name = 'tasks.txt'
        with open(self.file_name, 'w', encoding='utf-8') as f:
            f.write("Задача 1\nЗадача 2\n")

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    @patch('builtins.input', return_value="Новая задача")
    def test_create_task(self, mock_input):
        create_task()

        with open(self.file_name, 'r', encoding='utf-8') as f:
            tasks = f.readlines()

        self.assertIn("Новая задача\n", tasks)

    @patch('builtins.input', side_effect=["1", "Измененная задача"])
    def test_change_task(self, mock_input):
        change_task()

        with open(self.file_name, 'r', encoding='utf-8') as f:
            tasks = f.readlines()

        self.assertEqual(tasks[0], "Измененная задача\n")

    @patch('builtins.input', return_value="1")
    def test_delete_task(self, mock_input):
        delete_task()

        with open(self.file_name, 'r', encoding='utf-8') as f:
            tasks = f.readlines()

        self.assertEqual(len(tasks), 1)
        self.assertNotIn("Задача 1\n", tasks)


if __name__ == '__main__':
    unittest.main()