from CommandLine.command_line_input import CommandLineInput
from Commands.move_issue import MoveIssue
from Requests.IssueRequests.request import Request
from JiraInteractions.jira_command_manager import JiraCommandManager


class IssueMoveRequest(Request):
    def execute(self, jcm: JiraCommandManager, args: CommandLineInput) -> None:
        move_issue_command: MoveIssue = args.command
        jcm.move_issue(jcm.get_issue(args.id), move_issue_command.transition)

    def has_required_parameters(self, args: CommandLineInput) -> bool:
        return isinstance(args.command, MoveIssue)
