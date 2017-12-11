"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""
from urllib.request import urlopen
def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={0}&to={1}&amt={2}'.format(currency_from, currency_to, str(amount_from))
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    list1 = jstr.split(':')
    strj = ''
    str0 = ''
    for i in range(len(list1[-1])):
        stri = list1[-1]
        if stri[i] not in '}" ':
            strj = strj + stri[i]
    if strj == 'Exchangecurrencycodeisinvalid.':
        return 'Exchange currency code is invalid.'
    elif strj == 'Currencyamountisinvalid.':
        return 'Currency amount is invalid.'
    elif strj == 'Sourcecurrencycodeisinvalid.':
        return 'Source currency code is invalid.'
    else:
        for stri in list1:
            for i in range(len(stri)):
                if stri[i] in "1234567890.":
                    strj = strj + stri[i]
            if strj != '':
                str0 = strj
            strj = ''
        return str0
        
    
def test_get_from():
    """The first test about the 'exchange' function."""
    assert(float(exchange('USD', 'BBD', 1.0)) == 2)
    assert(float(exchange('BBD', 'USD', 1.0)) == 0.5)
    print('Test1 passed.')


def test_B():
    """The second test about the 'exchange' function."""
    assert(exchange('USD', 'LYD', 'string') == 'Currency amount is invalid.')
    print('Test2 passed.')
    


def test_C():
    """The last test about the 'exchange' function."""
    assert(exchange('123', 'LYD', 1.0) == 'Source currency code is invalid.')
    assert(exchange('USD', 'AAA', 1.0) == 'Exchange currency code is invalid.')
    print('Test3 passed.')

def testAll():
    """Test all cases."""
    test_get_from()
    test_B()
    test_C()
    print("All tests passed.")


def main():
    testAll()


if __name__ == '__main__':
    main()



    
