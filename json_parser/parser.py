#!/usr/bin/env python3

import json
import sys

from json_parser import config
from json_parser import printer


def load_json_file(file_path):
    try:
        with open(file_path) as f:
            return [json.loads(line) for line in f]
    except Exception as e:
        _printer.log_error("Error while loading json file %s; "
                           "Error: %s" % (file_path, e))
        sys.exit(1)


def main():
    args = config.get_config_parser()
    global _printer
    _printer = printer.get_printer(args)

    json_data = load_json_file(args.log_file)
    if args.only_columns:
        _printer.print_columns_names(json_data)
    else:
        _printer.print_data(json_data)
