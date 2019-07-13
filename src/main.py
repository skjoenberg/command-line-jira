from CommandLine.CommandLineArgument.command_line_argument_parser import parse_arguments
from Mappers.command_line_argument_mapper import Map
from Requests.request_controller import RequestController

request_controller = RequestController()

bla = parse_arguments() | Map
RequestController().execute_request(bla)


