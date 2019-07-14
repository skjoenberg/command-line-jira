from CommandLine.command_line_input import CommandLineInput
from Requests.shared_request_checks import is_issue, is_status_command
from Requests.IssueRequests.request import Request
from JiraInteractions.jira_command_manager import JiraCommandManager


class IssueStatusRequest(Request):
    def execute(self, jcm: JiraCommandManager, command_line_input:  CommandLineInput) -> str:
        issue = jcm.get_issue(command_line_input.id)
        jcm.get_transitions(issue)
        return str(jcm.get_transitions)

    def has_required_parameters(self, command_line_input: CommandLineInput):
        return is_issue(command_line_input) and is_status_command(command_line_input)
