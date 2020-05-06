import csv
import requests
import sys

import parseArgs

class Stocks:
   """
      Defines a class to interact with stocks.
   """

   baseUrl = 'https://fmpcloud.io/api/v3/'

   def __init__( self, userArgs=None ):
      """
         Initialization args.
      """

      if( parseArgs.argparse.Namespace is type( userArgs ) ):
         self.myArgs = userArgs
      else:
         self.myArgs = parseArgs.parseArgs( parseArgs.setupParser(), userArgs )

   def cleanup( self ):
      """
         Perform cleanup if required.
      """
      pass


# TODO Get my apikey out of here before using a public repo!!!


# TODO Should change to finnhub.  They have 60 API calls per minute...

# https://fmpcloud.io/api/v3/historical-price-full/AAPL?from=2018-03-12&to=2019-03-12&apikey=demo
# https://fmpcloud.io/api/v3/stock-screener?volumeMoreThan=1000&limit=100&apikey=demo
# https://fmpcloud.io/api/v3/stock-screener?volumeLowerThan=1000&limit=100&apikey=demo
# https://fmpcloud.io/api/v3/quote/AAPL,FB,MSFT?datatype=csv&apikey=demo

# Sector Screener
# https://fmpcloud.io/api/v3/stock-screener?datatype=csv&sector=tech&limit=100&apikey=demo

   def getDataJson(self, apikey='demo', symbol='AAPL'):
      """
         Initially, this is just going to generate a list of days that the
         Stock Market was open.
      """

      # import json lib
      import json

      url = 'https://fmpcloud.io/api/v3/historical-price-full/AAPL?from=2020-01-01&to=2020-04-30&apikey='
      url = url + apikey

      with requests.Session() as sess:
         download = sess.get(url)

         decoded_content = download.content.decode('utf-8')

         data = json.loads(decoded_content)

         #symbols = data['symbol']
         #print( 'symbols:' )
         #print(symbols)

         historicalList = data['historical']
         #print( 'historical list:' )
         #print( historicalList[0] )

         days = []
         for day in historicalList:
            days.append(day['date'])

         #print( days )

         return days



      pass

   def getData( self, url=None ):

      # This might be useful.
      # Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes.
      # To make it as easy as possible to interface with modules which implement the DB API, the value None is
      # written as the empty string. While this isn’t a reversible transformation, it makes it easier to dump 
      # SQL NULL data values to CSV files without preprocessing the data returned from a cursor.fetch* call. 
      # All other non-string data are stringified with str() before being written.

      with requests.Session() as s:
         download = s.get(url)

         decoded_content = download.content.decode('utf-8')

         cr = csv.reader(decoded_content.splitlines(), delimiter=',', quotechar='"')
         #cr = csv.reader(decoded_content.splitlines(), dialect='excel')
         with open('out.csv', 'w', newline='') as csvfile:
            cw = csv.writer(csvfile, delimiter=',', quotechar='"')
            #cw = csv.writer(csvfile, dialect='excel')
            for row in cr:
               cw.writerow(row)

      return 0

   def buildVolumeScreenUrl(self, volumeIn=10, lessThan=True, limit=200):
      url = Stocks.baseUrl + "stock-screener?datatype=csv&"

      if ( True == lessThan ):
         url = url + "volumeLowerThan="
      else:
         url = url + "volumeMoreThan="

      #print( "Volume: ")
      #print( volumeIn )
      url = url + str(10) + "&"
      url = url + "limit=" + str(limit) + "&"
      url = url + "apikey=" + self.myArgs.apiKey

      return url

   def test1(self):
      """
         First test.
      """

      self.getData( "https://fmpcloud.io/api/v3/quote/AAPL,FB,MSFT?datatype=csv&apikey=%s" % ( self.myArgs.apiKey ) )

   def sp1Sector( self ):
      """
         Gather stocks in the Tech sector.
      """

      self.getData( ("https://fmpcloud.io/api/v3/stock-screener?datatype=csv"
         "&sector=tech&limit=500&apikey=%s" ) % ( self.myArgs.apiKey ) )


   def volumeScreen(self):
      url = self.buildVolumeScreenUrl()

      print( url )
      self.getData( url )

      # TODO Finish this.

   def main( self, userArgs=None ):
      """
         Main code of the object.
      """

      self.sp1Sector()
      
      return 0

def execMain( userArgs=None ):
   """
      Main code of the object.
   """

   parser = parseArgs.setupParser()

   args = parseArgs.parseArgs( parser, userArgs )

   stocks = Stocks( args )

   exitValue = stocks.main()

   stocks.cleanup()

   return exitValue

if __name__ == '__main__':
    try:
        retVal = execMain()
    except KeyboardInterrupt:
        print('Received <Ctrl>+c')
        sys.exit(-1)

    sys.exit(retVal)