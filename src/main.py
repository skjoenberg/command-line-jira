from jiraConnectionHandler import JiraConnectionHandler
from loginHandler import LoginHandler

loginHandler = LoginHandler("")
jch = JiraConnectionHandler(loginHandler) 
jch.getIssue()