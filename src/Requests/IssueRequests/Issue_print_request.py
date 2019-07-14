from Requests.IssueRequests.request import Request
from Requests.shared_request_checks import is_issue
from JiraInteractions.jira_command_manager import JiraCommandManager


class IssuePrintRequest(Request):
    def execute(self, jcm: JiraCommandManager, args) -> str:
        issue = jcm.get_issue(args.id)
        return str(issue.pprint())

    def has_required_parameters(self, args):
        return is_issue(args)
