from CommandLineHandling.argument_parser import parse_arguments
from config_manager import ConfigManager
from jira_command_manager import JiraCommandManager
from jira_connection_manager import JiraConnectionHandler
from login_manager import LoginManager


class CommandController():
    def handle_arguments(self):
        config_manager = ConfigManager()
        login_handler = LoginManager(config_manager.get_username())
        jch = JiraConnectionHandler(login_handler)
        jcm = JiraCommandManager(config_manager, jch)

        args = parse_arguments()

        if args.type == 'issue':
            issue = jcm.get_issue(args.id)
            print(jcm.get_transitions(issue))
            if args.status:
                print(issue.get_status())
            else:
                issue.pprint()

