import os
from time import sleep

import unittest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_find_elements(self):
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Google")')
            el.click()
        except Exception as e:
            pass
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Always")')
            el.click()
        except Exception as e:
            pass
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("OK")')
            el.click()
        except Exception as e:
            pass
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Yes")')
            el.click()
        except Exception as e:
            pass
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("OK")')
            el.click()
        except Exception as e:
            pass
        self.driver.press_keycode(82)
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Download")')
            el.click()
        except Exception as e:
            pass

        sleep(10)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
