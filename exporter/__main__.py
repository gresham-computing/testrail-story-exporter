import configparser
import csv
import sys

import requests

from exporter.tree import extract_stories


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
    keys = stories[0].keys()
    filename = 'stories.csv'
    with open(filename, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(stories)
    print("CSV file of {} stories written to {}".format(len(stories), filename))


if __name__ == '__main__':
    main()
