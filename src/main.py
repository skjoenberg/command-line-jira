from CommandLine.CommandLineArgument.command_line_argument_parser import parse_arguments
from Mappers.command_line_argument_mapper import Map
from containers import Controllers

Controllers.request_controller().execute_request(parse_arguments() | Map)


