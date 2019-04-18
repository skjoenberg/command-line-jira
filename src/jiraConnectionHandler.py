from jira import JIRA 
from issue import Issue

class JiraConnectionHandler:
    def __init__(self, loginHandler):
        self._loginHandler = loginHandler 
        self._jira = self._establishConnection()

    def _establishConnection(self):
        options = {
            "server": "",
        }
        return JIRA(auth=self._loginHandler.getAuthentication(), options=options)

    def getIssue(self):
        Issue(self._jira.issue("APD-1638")).pprint()