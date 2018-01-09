# TestRail User Story Exporter

Exports user stories from TestRail into a CSV. It expects a structure of directories named "Theme - $themeName" and
"Epic - $epicName" to work correctly.

Acceptance criteria, BDD, and other comments aren't handled. This assumes that any section that doesn't have any
children is supposed to be a story, and sections that do have children are groupings of stories and not stories
themselves.

## Configuration

You need a `testrail.ini` file in this directory that looks like this:

```ini
[testrail]
Username = MyTestrailUsername
ApiKey = MYTESTRAILAPIKEY
Server = myserver.testrail.net
SuiteId = 13
```

It's added to the `.gitignore` for security purposes (so you don't accidentally submit API credentials to a git repo).

See the [TestRail Documentation](http://docs.gurock.com/testrail-api2/accessing#username_and_api_key) for information
about generating API keys.

## Usage

Invoke as a python module

```bash
python3 -m exporter
```

You'll get some output explaining any stories that couldn't be parsed. In this directory you'll get a `stories.csv` file
as output.
