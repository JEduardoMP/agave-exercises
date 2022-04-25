import unittest
import requests


class AddTest(unittest.TestCase):

  API_URL = "http://localhost:5000"
  RECIEPT_URL = '{}/api/shopping-statistics'.format(API_URL)
  RECIEPT_BY_CATEGORY_URL = '{}/api/shopping-statistics/Food'.format(API_URL)
  RECIEPT_SPENT_BY_CATEGORY_URL = '{}/api/shopping-statistics/category/Food'.format(API_URL)
  
  def test1(self):
    r = requests.get(AddTest.RECIEPT_URL)
    self.assertEqual(r.status_code, 200)

  def test2(self):
    r = requests.get(AddTest.RECIEPT_BY_CATEGORY_URL)
    self.assertEqual(r.status_code, 200)
  
  def test3(self):
    r = requests.get(AddTest.RECIEPT_SPENT_BY_CATEGORY_URL)
    self.assertEqual(r.status_code, 200)
