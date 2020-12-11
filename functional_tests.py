from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVistorTest(unittest.TestCase):

    def setUp(self):
        #self.browser = webdriver.Firefox()
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless=True
        self.browser = webdriver.Firefox(options=fireFoxOptions)
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Terry heard about an online Zork like game
        # He goes to the website.
        self.browser.get('http://localhost:8000/home.html')

        # He notices the Title and heading
        self.assertIn('Merlin\'s', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Merlin\'s Adventure', header_text)    

        # He sees a box inviting him to enter an action
        inputbox = self.browser.find_element_by_id('id_action')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '>'
        )

        #It asks him to enter the character's name
        inputbox.send_keys('Terry')

        # The game tells him about his surroundings
        # Terry is able to preform an action
        inputbox.send_keys('Obtain eye of newt')

        # He presses enter
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_result_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'Terry obtained eye of newt from the shelf.' for row in rows),
            "Nothing obtained!"
        )

        # He sees the webpage update with the text above
        # 
        self.fail('Finish the test!')

        # 

        # 
        # 

        # 

        # 

if __name__ == '__main__':
    unittest.main(warnings='ignore')
