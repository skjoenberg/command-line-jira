from abc import ABC, abstractmethod
from typing import Optional

from jira_command_manager import JiraCommandManager


class Request(ABC):
    @abstractmethod
    def execute(self, jcm: JiraCommandManager, args) -> Optional[str]:
        pass

    @abstractmethod
    def has_required_parameters(self, args):
        pass
