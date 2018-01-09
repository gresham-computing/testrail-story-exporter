import configparser
import sys

import requests

from exporter.tree import extract_stories
from exporter.writer import write_to_csv


def _sections(testrail_config):
    url = "https://{0}/index.php?/api/v2/get_sections/{1}".format(testrail_config['server'], testrail_config['suiteid'])
    r = requests.get(url, auth=(testrail_config['username'], testrail_config['apikey']), headers={'Content-Type': 'application/json'})
    return r.json()


def load_config():
    config_parser = configparser.ConfigParser()
    config_parser.read('testrail.ini')
    return config_parser['testrail']


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    stories = extract_stories(_sections(load_config()))
    csv_data = write_to_csv('stories.csv', stories)
    print("CSV file of {} stories written to {}".format(csv_data['num_records'], csv_data['output_filename']))


if __name__ == '__main__':
    main()
