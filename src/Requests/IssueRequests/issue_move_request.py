from CommandLine.command_line_input import CommandLineInput
from Commands.move_issue import MoveIssue
from Requests.IssueRequests.request import Request
from JiraInteractions.jira_command_manager import JiraCommandManager
from Requests.shared_request_checks import is_issue


class IssueMoveRequest(Request):
    def execute(self, jcm: JiraCommandManager, args: CommandLineInput) -> None:
        move_issue_command: MoveIssue = args.command
        jcm.move_issue(jcm.get_issue(args.id), move_issue_command.transition)

    def has_required_parameters(self, args: CommandLineInput) -> bool:
        return is_issue(args) and isinstance(args.command, MoveIssue)
