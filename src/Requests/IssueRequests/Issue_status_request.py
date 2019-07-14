from CommandLine.command_line_input import CommandLineInput
from JiraInteractions.JiraDataObjects.issue import Issue
from Requests.shared_request_checks import is_issue, is_status_command
from Requests.IssueRequests.request import Request
from JiraInteractions.jira_command_manager import JiraCommandManager


class IssueStatusRequest(Request):
    def execute(self, jcm: JiraCommandManager, command_line_input:  CommandLineInput) -> str:
        issue: Issue = jcm.get_issue(command_line_input.id)
        jcm.get_transitions(issue)
        return str(jcm.get_transitions)

    def has_required_parameters(self, args: CommandLineInput) -> bool:
        return is_issue(args) and is_status_command(args)
