from CommandLineHandling.command_line_utilities import write_to_console
from termcolor import colored

class Issue:
    def __init__(self, jira_issue):
        self._issue = jira_issue

    def pprint(self):
        title = self._issue.fields.summary
        width = len(title) + 2
        ba = colored(" > ", 'blue')
        write_to_console("{:^80}".format(colored(title, 'green')))
        write_to_console("{:<80}".format(ba + self._issue.fields.issuetype.name + ba + ','.join(self._issue.fields.labels)))
        write_to_console("{:<80}".format("Estimation: %2.3f" % (float(self._issue.fields.timeestimate) / 60 / 60 / 7.5) + " days"))
