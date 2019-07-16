import string
from textwrap import wrap, fill

from jira import Issue
from termcolor import colored


class Issue:
    def __init__(self, jira_issue: Issue):
        self._issue = jira_issue

    @property
    def issue(self) -> Issue:
        return self._issue

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

    @property
    def name(self) -> string:
        return self._issue.key

    @property
    def assignee(self) -> string:
        try:
            return self._issue.fields.assignee.displayName
        except:
            return "Not assigned"
    @property
    def remaining_time(self) -> string:
        try:
            return '{:2.2f} days'.format(self.remaining_estimate)
        except:
            return "No time estimate"

    def pprint(self):
        title_line = "{:80}".format(colored(self.summary + " [" + self.status + "]", 'green'))

        ba = colored(" \ ", 'blue')
        general_info_line = "{:80}".format(
            ba.join([self.issue_type, ','.join(self.labels), 'Remaining: ' + self.remaining_time])) + "\n"

        description_line = "[No description]"
        if self.description:
            description_line = "\n".join([fill(line, width=80) for line in self.description.split("\n")])

        return "\n".join([title_line, general_info_line, description_line])

    def pprint_oneline(self):
        return self.name + " [" + self.assignee + "]: " + self.status + " (" + self.remaining_time + ")"
