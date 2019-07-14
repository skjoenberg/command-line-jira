from CommandLine.command_line_input import CommandLineInput
from CommandLine.command_line_utilities import write_to_console
from Requests.IssueRequests.Issue_print_request import IssuePrintRequest
from Requests.IssueRequests.Issue_status_request import IssueStatusRequest
from Requests.IssueRequests.Issue_log_work_request import IssueLogWorkRequest
from JiraInteractions.jira_command_manager import JiraCommandManager
from Requests.IssueRequests.issue_move_request import IssueMoveRequest


class RequestController:
    def __init__(self, jira_connection_handler: JiraCommandManager, jira_command_manager: JiraCommandManager):
        self._jch = jira_connection_handler
        self._jcm = jira_command_manager
        self._request_types = []

        self.initialize_request_types()

    def initialize_request_types(self):
        self._request_types.append(IssueStatusRequest())
        self._request_types.append(IssueLogWorkRequest())
        self._request_types.append(IssueMoveRequest())
        self._request_types.append(IssuePrintRequest())

    def execute_request(self, command_line_input: CommandLineInput):
        for request_type in self._request_types:
            if request_type.has_required_parameters(command_line_input):
                output = request_type.execute(self._jcm, command_line_input)
                if output:
                    write_to_console(output)
                break
