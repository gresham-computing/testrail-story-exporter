import unittest

from exporter.story import in_order_to, i_want, as_a, parse_user_story, acceptance_criteria


class TestStory(unittest.TestCase):
    example_story = """
    
In order to test this function
As a Software Engineer
I want to create test data

## Acceptance Criteria
* Must be formatted in markdown
* Must have a blank line at the start to confuse things
    """

    basic_story = """
In order to test this function
As a Software Engineer
I want to create test data
    """

    def test_in_order_to(self):
        self.assertEqual(in_order_to(self.example_story), 'test this function')

    def test_i_want(self):
        self.assertEqual(i_want(self.example_story), 'to create test data')

    def test_as_a(self):
        self.assertEqual(as_a(self.example_story), 'a Software Engineer')

    def test_acceptance_criteria(self):
        self.assertEqual(acceptance_criteria(self.example_story),
                         ['Must be formatted in markdown',
                          'Must have a blank line at the start to confuse things'])

    def test_acceptance_criteria_on_basic_story(self):
        """Test a user story without acceptance criteria"""
        self.assertEqual(acceptance_criteria(self.basic_story), [])

    def test_parse_valid_user_story(self):
        story = {
            'description': self.example_story,
            'name': 'My Story'
        }
        self.assertDictEqual(parse_user_story(story), {
            'in order to': 'test this function',
            'as': 'a Software Engineer',
            'I want': 'to create test data',
            'acceptance criteria': ['Must be formatted in markdown',
                                    'Must have a blank line at the start to confuse things'],
        })

    def test_parse_invalid_user_story(self):
        story = {
            'description': "No useful text",
            'name': 'My Story'
        }
        self.assertIsNone(parse_user_story(story))


if __name__ == '__main__':
    unittest.main()
