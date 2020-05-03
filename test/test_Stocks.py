try:
    from builtins import object
except ImportError:
    pass

import unittest
from unittest.mock import patch

import sys
sys.path.append('C:\\venv\\DL\\fmpcloud-data\\code')
#print(sys.path)

from Stocks import Stocks

class TestStocks(unittest.TestCase):
   """
   """

   def setUp(self):
      self.test_Stocks = Stocks( '-k demo')

   def tearDown(self):
      pass

   def test_class_constants(self):
      pass

   def test_class_variables(self):
      pass


   def test_buildVolumeScreenUrl(self):
      """
         test_buildVolumeScreenUrl
      """
      
      url = Stocks.buildVolumeScreenUrl(self)
      self.assertEqual(("https://fmpcloud.io/api/v3/stock-screener?volumeLowerThan"
                     "=1000&limit=200&apikey=demo"), url)


if __name__ == "__main__":

    unittest.main()
