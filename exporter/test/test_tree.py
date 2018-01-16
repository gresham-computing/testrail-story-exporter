import unittest

from exporter.tree import extract_stories


class TestTree(unittest.TestCase):
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
                'I want': 'to bar',
                'acceptance criteria': [],
            },
            {
                'theme': 'My Theme',
                'epic': 'Epic Two',
                'as': 'a Software Tester',
                'in order to': 'fizz',
                'I want': 'to buzz',
                'acceptance criteria': [],
            }
        ])


if __name__ == '__main__':
    unittest.main()
