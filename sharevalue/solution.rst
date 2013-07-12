----------
Assignment
----------

Using liburl2 module, find out what is the share value of a company using it's NASDAQ symbol.

Script Use
~~~~~~~~~~

::
    
    ./sharevalue.py <Company_NASDAQ_Symbol>

    Ex: ./sharevalue.py GOOG


Sample Output
~~~~~~~~~~~~~

::

    Share value for <Company_NASDAQ_Symbol> is : xxx.xx

Solution
~~~~~~~~

.. code:: python
   :number-lines:
    
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
             """

    def check_symbol():
        
        print """
                Please provide Company NASDAQ Symbol correctly
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
            print "\nShare value for %s is: %.2f\n" % (symbol, sharevalue)
        
        else:
            check_symbol()    

        sys.exit(0)
