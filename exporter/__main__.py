import configparser
import sys

from exporter.api import TestRailApi
from exporter.tree import extract_stories
from exporter.writer import write_to_csv


def load_config():
    config_parser = configparser.ConfigParser()
    config_parser.read('testrail.ini')
    return config_parser['testrail']


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    config = load_config()
    api = TestRailApi(config)
    stories = extract_stories(api.get_sections(config['suiteid']))
    csv_data = write_to_csv('stories.csv', stories)
    print('CSV file of %s stories written to %s' %
          (csv_data['num_records'],
           csv_data['output_filename']))


if __name__ == '__main__':
    main()
