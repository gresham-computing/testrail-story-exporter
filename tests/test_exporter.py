import unittest

from exporter import in_order_to, i_want, as_a, parse_user_story, extract_stories


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

    def test_parse_valid_user_story(self):
        story = {
            'description': self.example_story,
            'name': 'My Story'
        }
        self.assertDictEqual(parse_user_story(story), {
            'in order to': 'test this function',
            'as': 'a Software Engineer',
            'I want': 'to create test data'
        })

    def test_parse_invalid_user_story(self):
        story = {
            'description': "No useful text",
            'name': 'My Story'
        }
        self.assertIsNone(parse_user_story(story))

    def test_extract_stories(self):
        sections = [
            {
                'id': 0,
                'name': 'Theme - My Theme',
                'parent_id': None
            },
            {
                'id': 1,
                'name': 'Epic - Epic One',
                'parent_id': 0
            },
            {
                'id': 2,
                'name': 'My First Story',
                'parent_id': 1,
                'description': """
In order to foo
As a Software Engineer
I want to bar"""
            },
            {
                'id': 3,
                'name': 'Epic - Epic Two',
                'parent_id': 0
            },
            {
                'id': 4,
                'name': 'My Second Story',
                'parent_id': 3,
                'description': """
In order to fizz
As a Software Tester
I want to buzz"""
            },
        ]

        self.assertSequenceEqual(extract_stories(sections), [
            {
                'theme': 'My Theme',
                'epic': 'Epic One',
                'as': 'a Software Engineer',
                'in order to': 'foo',
                'I want': 'to bar'
            },
            {
                'theme': 'My Theme',
                'epic': 'Epic Two',
                'as': 'a Software Tester',
                'in order to': 'fizz',
                'I want': 'to buzz'
            }
        ])


if __name__ == '__main__':
    unittest.main()
