from jira_connection_manager import JiraConnectionHandler
from login_manager import LoginManager
from config_manager import ConfigManager

config_manager = ConfigManager()
loginHandler = LoginManager(config_manager.get_username())
jch = JiraConnectionHandler(loginHandler)
jch.get_issue()