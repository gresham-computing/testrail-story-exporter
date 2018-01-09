import requests
import configparser
import re
import csv


def _sections(testrail_config):
    url = "https://{0}/index.php?/api/v2/get_sections/{1}".format(testrail_config['server'], testrail_config['suiteid'])
    r = requests.get(url, auth=(testrail_config['username'], testrail_config['apikey']), headers={'Content-Type': 'application/json'})
    return r.json()


def _match_line(prefix, story):
    return re.search("^{0}(.*)$".format(prefix), story, re.MULTILINE).group(1).strip()


def in_order_to(story):
    return _match_line("In order to", story)


def i_want(story):
    return _match_line("I want", story)


def as_a(story):
    return _match_line("As", story)


def parse_user_story(node):
    story = node['description']
    try:
        return {
            'in order to': in_order_to(story),
            'as': as_a(story),
            'I want': i_want(story),
        }
    except (TypeError, AttributeError):
        print("Unable to parse story {}".format(node['name']))
        return None


def parse_tree(sections):
    for section in sections:
        section['children'] = []

    for section in sections:
        if section['parent_id'] is not None:
            # Find parent
            parent = next(parent for parent in sections if parent['id'] == section['parent_id'])
            parent['children'].append(section)

    return [section for section in sections if section['parent_id'] is None]


def _give_story_context(story, context):
    story['theme'] = context.get('theme')
    story['epic'] = context.get('epic')


def _update_context(section_header, context):
    context = context.copy()
    if 'Epic' in section_header:
        context['epic'] = re.search("Epic - (.*)", section_header).group(1).strip()
    elif 'Theme' in section_header:
        context['theme'] = re.search("Theme - (.*)", section_header).group(1).strip()
    return context


def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def walk_nodes(context, nodes):
    return flatten(walk_tree(context, n) for n in nodes)


def walk_tree(context, node):
    if not node['children']:
        # leaf node, this is a user story
        story = parse_user_story(node)
        if story is not None:
            _give_story_context(story, context)
        return [story]
    else:
        # this is a grouping of stories
        context = _update_context(node['name'], context)
        return walk_nodes(context, node['children'])


def extract_stories(sections):
    return [story for story in walk_nodes({}, parse_tree(sections)) if story is not None]


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('testrail.ini')
    stories = extract_stories(_sections(config['testrail']))
    keys = stories[0].keys()
    filename = 'stories.csv'
    with open(filename, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(stories)
    print("CSV file of {} stories written to {}".format(len(stories), filename))
