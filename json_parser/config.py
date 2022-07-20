import argparse


config_parser = None

def get_config_parser():
    global config_parser
    if config_parser is None:
        config_parser = argparse.ArgumentParser(
            description='This is super great json parser tool ;)')
        config_parser.add_argument(
            'log_file',
            help='Json log file to parse')
        config_parser.add_argument(
            '--sort-by',
            default=None,
            help='Column on which parsed log should be sorted '
                 '(not implemented yet)')
        config_parser.add_argument(
            '--column',
            action='append',
            dest="columns",
            help='Columns to display')
        config_parser.add_argument(
            '--only-columns',
            action='store_true',
            help='With this option, only columns names will be displayed.')
        config_parser.add_argument(
            '--format',
            default='table',
            help='Format of the output. It can be "html", "table" or '
                 'custom string. If custom string is specified, "column" '
                 'option is not checked.')
        config_parser.add_argument(
            '--verbose',
            action='store_true',
            help='Be more verbose.')
    return config_parser.parse_args()
