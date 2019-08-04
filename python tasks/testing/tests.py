from name_function import get_formated_name
import unittest

class test(unittest.TestCase):
    
    def test_first_last_name(self):
        formated_name = get_formated_name("jenis", "joplin")
        self.assertEqual(formated_name, "Jenis Joplin")


unittest.main()
