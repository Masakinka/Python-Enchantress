"""
Test case for main employee functions
"""

import unittest
# from unittest import mock
from unittest.mock import patch
# from homework.tests_simple_employee import *
from homework.tests_simple_employee import Employee


class SimpleEmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Vi', 'None', 50)

    def test_email(self):
        self.assertEqual(self.employee.email, 'Vi.None@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, 'Vi None')

    def apply_raise(self):
        self.assertEqual(self.employee.apply_raise, 52.5)

    def test_monthly_schedule_response_bad(self):
        with patch('homework.tests_simple_employee.requests.get') as rec:
            rec.return_value.ok = False
            self.assertEqual(self.employee.monthly_schedule('January'), 'Bad Response!')

    def test_monthly_schedule_response_ok(self):
        with patch('homework.tests_simple_employee.requests.get') as rec:
            rec.return_value.ok = True
            rec.return_value.text = 'Response!'
            self.assertEqual(self.employee.monthly_schedule('January'), 'Response!')


if __name__ == "__main__":
    unittest.main(verbosity=2)
