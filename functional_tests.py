from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Turner needs to create a list, so she goes to her favorite on-line
        # list app.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is prompted to enter a to-do item by default

        # She types 'Buy tuna' into a text box, because she enjoys tuna fish.

        # When she hits enter, the page updates, and now the page lists
        # "1. Buy tuna" as an item in a to-do list

        # There is still a text box ready for her to enter another item. She
        # enters "open tuna can"

        # The page updates again, and now shows both items on list

        # Turner wonders if the site saves the list. Then she notices a
        # unique URL has been generated automatically, and some text on the
        # page explains this.

        # Turner visits the unique URL and her to-do list is still there

        # Satisfied, she purrs and curls up into a ball


if __name__ == '__main__':
    unittest.main()
