# unittest_overview
import unittest  # class-based

from main import add, subtract


class TestMain(unittest.TestCase):  # !unittest.TestCase
    #@classmethod
    # def setUpClass(cls) -> None:
    #     before all tests in this class

    # def setUp(self) -> None:
    #     every time before every test
    #
    # def tearDown(self) -> None:
    #     every time after every test

    def test_can_add_2_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_can_sub_2_numbers(self):
        self.assertEqual(subtract(3, 5), -2)

# if __name__ == '__main__':
#    unittest.main()
