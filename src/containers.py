from dependency_injector import containers, providers

from Config.config_manager import ConfigManager
from Requests.request_controller import RequestController
from JiraInteractions.jira_command_manager import JiraCommandManager
from JiraInteractions.jira_connection_manager import JiraConnectionHandler
from LoginManagement.login_manager import LoginManager


class Managers(containers.DeclarativeContainer):
    config_manager = providers.Singleton(ConfigManager)
    login_manager = providers.Singleton(LoginManager, config_manager)
    jira_connection_handler = providers.Singleton(JiraConnectionHandler, login_manager, config_manager)
    jira_command_manager = providers.Singleton(JiraCommandManager, config_manager, jira_connection_handler)


class Controllers(containers.DeclarativeContainer):
    request_controller = providers.Singleton(
        RequestController,
        Managers.jira_connection_handler,
        Managers.jira_command_manager)


