import string
from textwrap import wrap, fill

from jira import Issue
from termcolor import colored


class Issue:
    def __init__(self, jira_issue: Issue):
        self._issue = jira_issue

    @property
    def status(self) -> string:
        return str(self._issue.fields.status)

    @property
    def summary(self) -> string:
        return str(self._issue.fields.summary)

    @property
    def issue_type(self) -> string:
        return str(self._issue.fields.issuetype.name)

    @property
    def labels(self) -> [string]:
        return self._issue.fields.labels

    @property
    def description(self) -> string:
        return self._issue.fields.description

    @property
    def remaining_estimate(self) -> float:
        try:
            return float(self._issue.fields.aggregatetimeestimate) / 60 / 60 / 6
        except:
            return None

    def pprint(self):
        title_line = "{:80}".format(colored(self.summary + " [" + self.status + "]", 'green'))

        ba = colored(" \ ", 'blue')
        general_info_line = "{:80}".format(
            ba.join([self.issue_type, ','.join(self.labels), 'Remaining: ' + str(self.remaining_estimate)]))

        description_line = "\n".join([fill(line, width=80) for line in self.description.split("\n")])

        return "\n".join([title_line, general_info_line, "\n", description_line])
