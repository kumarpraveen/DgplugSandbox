#!/usr/bin/env python

import urllib2
import sys

class Finance(object):
    """
    This class will create prototype for 
    share value object.
    """
    def __init__(self, symbol):
        self.symbol = symbol

    def sharevalue(self):
        try:
            url = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1" % (self.symbol)
            csv_file_object = urllib2.urlopen(url)
            value = csv_file_object.read()
            csv_file_object.close()
            return value

        except IOError:
            print """ 
                    Not able to open url, please check your network connection 
                    or may be you provided a wrong Company NASDAQ Symbol
                  """
            sys.exit(1)

def check_help():
    print """
            ./sharevalue.py <Company_Symbol> 
            Ex ./sharevalue.py YHOO

            Here Company NASDAQ Symbol is have exactly have 4 char
            Please Provide correct NASDAQ Symbol
          """

if __name__ == '__main__':
    #Check the require arguments
    if len(sys.argv) != 2:
        check_help()
    else:
        symbol = sys.argv[1]
        company = Finance(symbol)
        sharevalue = float(company.sharevalue())
        if sharevalue:
            print "Share value for %s is: %.2f" % (symbol, sharevalue)
        else:
            check_help()

    sys.exit(1)
