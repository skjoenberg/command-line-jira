from jira_connection_manager import JiraConnectionHandler
from jira_command_manager import JiraCommandManager
from login_manager import LoginManager
from config_manager import ConfigManager

config_manager = ConfigManager()
login_handler = LoginManager(config_manager.get_username())
jch = JiraConnectionHandler(login_handler)
jcm = JiraCommandManager(config_manager, jch)
board = jcm.get_board()
active_sprint = jcm.get_active_sprint(board)
print(jcm.estimated_work_left_in_sprint(active_sprint))

#jcm.print_issue("APD-1638")
