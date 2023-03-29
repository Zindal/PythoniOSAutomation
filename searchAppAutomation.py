import unittest
import os
from appium import webdriver
from time import sleep
 
class TableSearchTest(unittest.TestCase):
 
    def setUp(self):
        # Set up appium
        app = os.path.join(os.path.dirname(__file__),
                           'TableSearchwithUISearchController/Swift',
                           'Search.swift.app')
        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '16.0',
                'deviceName': 'iPhone 14',
                'bundleId':'com.zindal.searchApp'
            })
 
 
    def test_search_field(self):
        self.driver.find_element_by_name("Search").click()
 
 
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TableSearchTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

