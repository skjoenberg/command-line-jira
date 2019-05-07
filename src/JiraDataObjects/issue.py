from jira import Issue

from CommandLineHandling.command_line_utilities import write_to_console
from termcolor import colored


class Issue:
    def __init__(self, jira_issue: Issue):
        self.issue = jira_issue

    def get_status(self):
        return str(self.issue.fields.status)

    def get_remaining_estimate(self):
        try:
            return float(self.issue.fields.aggregatetimeestimate) / 60 / 60 / 6
        except:
            return None

    def pprint(self):
        title = self.issue.fields.summary
        ba = colored(" > ", 'blue')
        write_to_console("{:^80}".format(colored(title, 'green')))
        write_to_console(
            "{:^80}".format(self.issue.fields.issuetype.name + ba + self.get_status() + ba + ','.join(self.issue.fields.labels)))
        write_to_console("{:^80}".format('Remaining: ' + str(self.get_remaining_estimate())))
