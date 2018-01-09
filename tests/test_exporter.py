import unittest

from exporter import in_order_to, i_want, as_a


class TestExporter(unittest.TestCase):

    example_story = """
    
In order to test this function
As a Software Engineer
I want to create test data

## Acceptance Criteria
* Must be formatted in markdown
* Must have a blank line at the start to confuse things
    """

    def test_in_order_to(self):
        self.assertEqual(in_order_to(self.example_story), 'test this function')

    def test_i_want(self):
        self.assertEqual(i_want(self.example_story), 'to create test data')

    def test_as_a(self):
        self.assertEqual(as_a(self.example_story), 'a Software Engineer')


if __name__ == '__main__':
    unittest.main()
