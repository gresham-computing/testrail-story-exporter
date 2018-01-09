import unittest

from exporter import in_order_to


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


if __name__ == '__main__':
    unittest.main()
