import sys

from prettytable import PrettyTable

PRINTER = None


def get_printer(config):
    global PRINTER
    if PRINTER is None:
        PRINTER = Printer(config)
    return PRINTER


class Printer(object):

    def __init__(self, config):
        self.config = config

    def print_msg(self, msg):
        print(msg)

    def log_error(self, msg):
        self.print_msg(msg)

    def log_debug(self, msg):
        if self.config.verbose:
            self.print_msg(msg)

    @staticmethod
    def _get_table():
        table = PrettyTable()
        table.align = "l"
        return table

    def _column_should_be_displayed(self, column_name):
        return not self.config.columns or column_name in self.config.columns

    def _get_columns(self, data):
        columns = []
        for row in data:
            for column_name in row.keys():
                if (self._column_should_be_displayed(column_name) and
                        column_name not in columns):
                    columns.append(column_name)
        return columns

    def _prepare_table_to_print(self, data):
        table = self._get_table()
        table.field_names = self._get_columns(data)
        for row in data:
            row_data_to_display = []
            for row_key, row_value in row.items():
                if self._column_should_be_displayed(row_key):
                    row_data_to_display.append(row_value)
            table.add_row(row_data_to_display)
        return table

    def print_columns_names(self, data):
        self.print_msg(self._get_columns(data))

    def print_data(self, data):
        if self.config.format == 'table':
            self.print_data_as_table(data)
        elif self.config.format == 'html':
            self.print_data_as_html(data)
        else:
            self.print_data_with_custom_format(data)

    def print_data_as_table(self, data):
        table = self._prepare_table_to_print(data)
        self.print_msg(table.get_string())

    def print_data_as_html(self, data):
        table = self._prepare_table_to_print(data)
        self.print_msg(table.get_html_string())

    def print_data_with_custom_format(self, data):
        try:
            data_to_print = ""
            for row in data:
                data_to_print += self.config.format % row
                data_to_print += "\n"
            self.print_msg(data_to_print)
        except ValueError as e:
            self.log_error("Wrong custom format. Error message: %s" % e)
            sys.exit(2)
