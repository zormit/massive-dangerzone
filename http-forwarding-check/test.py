#!/usr/bin/python3
import unittest
import csv
from urllib.request import urlopen
from http.client import HTTPConnection

class TestDomainForwarding(unittest.TestCase):
    ''' this script tests, whether certain webserver-redirections do actually work
        like expected '''

    def setUp(self):
        #http://www.diveintopython3.net/http-web-services.html#whats-on-the-wire
        #HTTPConnection.debuglevel=1
        self.data = csv.DictReader(open('data.csv'), delimiter=',', quotechar='"')

    def test_all(self):
        ''' all in one test. could be extended to more than one test via
            https://github.com/txels/ddt but I think its overkill for now '''
        for test in self.data:
            response = urlopen(test['url'])
            self.assertEqual(response.geturl(), test['forwarding'])
            self.assertTrue(test['containing'] in str(response.read()))

if __name__ == '__main__':
    unittest.main()
