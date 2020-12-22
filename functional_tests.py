from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import requests
class NewVistorTest(unittest.TestCase):

    def setUp(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless=True
        #simply choose the desired head option
        self.browser = webdriver.Firefox(options=fireFoxOptions)
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Terry heard about an online Zork like game
        # He goes to the website.
        self.browser.get('http://localhost:8000')

        # He notices the Title and heading
        self.assertIn('Merlin\'s Adventure', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Merlin\'s Adventure', header_text)    

        # He sees a box inviting him to enter an action
        inputbox = self.browser.find_element_by_id('id_action')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a response'
        )
        subBtn = self.browser.find_element_by_id('id_subBtn')

        #It asks him to enter the character's name
        inputbox.send_keys('Terry')
        subBtn.click()
        time.sleep(1)

        # The game tells him about his surroundings
        # Terry is able to preform an action
        inputbox.send_keys('Obtain eye of newt')
        subBtn.click()
        time.sleep(1)

        # He presses enter
        #inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)

        # #table = self.browser.find_element_by_id('id_result_table')
        #tableBody = self.browser.find_element_by_tag_name("tbody")
        rows = self.browser.find_elements_by_tag_name('tr')
        # # self.assertTrue(
        # #     any(row.text == 'Terry obtained eye of newt from the shelf.' for row in rows),
        # #     "Nothing obtained!"
        # # )

        self.assertFalse(
            any(print(row.text) for row in rows),
            "Nothing no welcome?!"
        )

        self.assertTrue(
            any(row.text == 'WELCOME TO MERLIN\'S ADVENTURE' for row in rows),
            "Nothing no welcome?!"
        )

        

        # He sees the webpage update with the text above
        # 
        self.fail('Finish the test!')

        # 

        # 
        # 

        # 

        # 

# if __name__ == '__main__':
#     unittest.main(warnings='ignore')
if __name__ == '__main__':
    unittest.main()
