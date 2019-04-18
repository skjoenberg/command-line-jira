from commandLineHandler import WriteToConsole, ReadFromConsole
from termcolor import colored

class Issue:
    def __init__(self, jira_issue):
        self._issue = jira_issue

    def pprint(self):
        title = self._issue.fields.summary
        width = len(title) + 2
        #WriteToConsole("+" + "-" * width + "+")
        ba = colored(" > ", 'blue')
        WriteToConsole("{:^80}".format(colored(title, 'green')))
        WriteToConsole("{:<80}".format(ba + self._issue.fields.issuetype.name + ba + ','.join(self._issue.fields.labels)))
        WriteToConsole("{:<80}".format("Estimation: %2.3f" % (float(self._issue.fields.timeestimate)/60/60/7.5) + " days"))
