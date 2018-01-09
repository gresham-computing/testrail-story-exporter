import re


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
