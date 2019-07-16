from CommandLine.command_line_input import CommandLineInput
from CommandLine.command_line_utilities import write_to_console
from Commands.sprint_issues import SprintIssues
from JiraInteractions.JiraDataObjects.issue import Issue
from Requests.IssueRequests.request import Request
from JiraInteractions.jira_command_manager import JiraCommandManager
from Requests.shared_request_checks import is_board


class SprintPrintIssues(Request):
    def execute(self, jcm: JiraCommandManager, args: CommandLineInput) -> None:
        board = jcm.get_board(args.id)
        sprint = jcm.get_active_sprint(board)
        [write_to_console(Issue(issue).pprint_oneline()) for issue in jcm.get_issues_in_sprint(sprint)]


    def has_required_parameters(self, args: CommandLineInput) -> bool:
        return is_board(args) and isinstance(args.command, SprintIssues)
