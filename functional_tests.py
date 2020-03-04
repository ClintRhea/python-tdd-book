from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Turner needs to create a list, so she goes to her favorite on-line
        # list app.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is prompted to enter a to-do item by default
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types 'Buy tuna' into a text box, because she enjoys tuna fish.
        inputbox.send_keys('Buy tuna')

        # When she hits enter, the page updates, and now the page lists
        # "1. Buy tuna" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy tuna')

        # There is still a text box ready for her to enter another item. She
        # enters "open tuna can"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('open tuna can')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on list
        self.check_for_row_in_list_table('1: Buy tuna')
        self.check_for_row_in_list_table('2: open tuna can')

        # Turner wonders if the site saves the list. Then she notices a
        # unique URL has been generated automatically, and some text on the
        # page explains this.
        self.fail('Finish the test!')

        # Turner visits the unique URL and her to-do list is still there

        # Satisfied, she purrs and curls up into a ball


if __name__ == '__main__':
    unittest.main()
