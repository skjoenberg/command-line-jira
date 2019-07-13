from CommandLine.command_line_input import CommandLineInput
from Requests.request import Request
from Commands.LogWork import LogWork
from JiraInteractions.jira_command_manager import JiraCommandManager


class IssueLogWorkRequest(Request):
    def execute(self, jcm: JiraCommandManager, args: CommandLineInput) -> None:
        log_work_command: LogWork = args.command
        jcm.log_work(jcm.get_issue(args.id), log_work_command.minutes_spent)

    def has_required_parameters(self, args):
        return isinstance(args.command, LogWork)
