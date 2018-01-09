import re

from exporter.story import parse_user_story


def _parse_tree(sections):
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


def _flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def _walk_nodes(context, nodes):
    return _flatten(_walk_tree(context, n) for n in nodes)


def _walk_tree(context, node):
    if not node['children']:
        # leaf node, this is a user story
        story = parse_user_story(node)
        if story is not None:
            _give_story_context(story, context)
        return [story]
    else:
        # this is a grouping of stories
        context = _update_context(node['name'], context)
        return _walk_nodes(context, node['children'])


def extract_stories(sections):
    return [story for story in _walk_nodes({}, _parse_tree(sections)) if story is not None]
