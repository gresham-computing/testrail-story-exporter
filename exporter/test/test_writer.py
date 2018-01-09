import csv
import tempfile
import unittest

from exporter.writer import write_to_csv


class TestWriter(unittest.TestCase):
    def test_write_to_csv(self):
        data = [
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
        ]

        filename = tempfile.NamedTemporaryFile().name

        r = write_to_csv(filename, data)

        # Check the CSV file for validity
        with open(filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for index, row in enumerate(reader):
                self.assertDictEqual(row, data[index])

        # Check return details from method
        self.assertEqual(r['num_records'], 2)
        self.assertEqual(r['output_filename'], filename)


if __name__ == '__main__':
    unittest.main()
