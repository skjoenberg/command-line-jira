from Requests.shared_request_checks import is_issue, has_status_flag
from Requests.request import Request
from jira_command_manager import JiraCommandManager


class IssueStatusRequest(Request):
    def execute(self, jcm: JiraCommandManager, args) -> str:
        issue = jcm.get_issue(args.id)
        jcm.get_transitions(issue)
        return str(jcm.get_transitions)

    def has_required_parameters(self, args):
        return is_issue(args) and has_status_flag(args)
