from CommandLine.CommandLineArgument.command_line_argument_parser import parse_arguments
from Requests.request_controller import RequestController

request_controller = RequestController()

arguments = parse_arguments()
request_controller.execute_request(arguments)


