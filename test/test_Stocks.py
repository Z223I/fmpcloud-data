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
      self.test_Stocks = Stocks()

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
      test_Stocks = Stocks()
      url = test_Stocks.buildVolumeScreenUrl(self)
      checkUrl = ( "https://fmpcloud.io/api/v3/stock-screener?"
         "datatype=csv&volumeLowerThan"
         "=1000&limit=200&apikey=demo" )
      print ( checkUrl )
      print ( url )
      self.assertEqual( checkUrl, url )


if __name__ == "__main__":

    unittest.main()
