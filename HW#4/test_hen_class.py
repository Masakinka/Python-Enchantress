import unittest
from unittest.mock import patch
from tests.hen_house.hen_class import HenHouse, ErrorTimesOfYear


class TestHenHouse(unittest.TestCase):

    def setUp(self):
        self.henhouse = HenHouse(10)

    def test_init_with_less_than_min(self):
        with self.assertRaises(ValueError) as error:
            self.henhouse = HenHouse(4)

    def test_season(self):
        with patch('tests.hen_house.hen_class.datetime.datetime') as moc:
            moc.today().month = 3
            self.assertEqual(self.henhouse.season, 'spring')

            moc.today().month = 1
            self.assertEqual(self.henhouse.season, 'winter')

            moc.today().month = 6
            self.assertEqual(self.henhouse.season, 'summer')

            moc.today().month = 11
            self.assertEqual(self.henhouse.season, 'autumn')

    @patch('tests.hen_house.hen_class.HenHouse.season', 'summer')
    def test_productivity_index(self):
        self.assertEqual(self.henhouse._productivity_index(), 1)

    @patch('tests.hen_house.hen_class.HenHouse.season', 'r')
    def test_productivity_index_incorrect_season(self):
        with self.assertRaises(ErrorTimesOfYear):
            self.henhouse._productivity_index()

    @patch('tests.hen_house.hen_class.HenHouse._productivity_index', return_value=0.25)
    def test_get_eggs_daily_in_winter(self, productivity):
        self.assertEqual(self.henhouse.get_eggs_daily(10), 2)

    @patch('tests.hen_house.hen_class.HenHouse.season', 'summer')
    def test_get_max_count_for_soup(self):
        self.assertEqual(self.henhouse.get_max_count_for_soup(2), 8)

    @patch('tests.hen_house.hen_class.HenHouse.season', 'summer')
    def test_get_max_count_for_soup_returns_zero(self):
        self.henhouse.get_max_count_for_soup(40)

    def test_food_price(self):
        with patch('tests.hen_house.hen_class.requests.get') as mock:
            mock.return_value.status_code = 200
            self.assertTrue(self.henhouse.food_price(), int)
        pass

    def test_food_price_connection_error(self):
        with patch('tests.hen_house.hen_class.requests.get') as mock:
            mock.return_value.status_code = 500
            with self.assertRaises(ConnectionError):
                self.henhouse.food_price()


if __name__ == '__main__':
    unittest.main()
