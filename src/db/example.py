from .utils import *


def rebuild_tables():
    exec_sql_file('res/db/schema.sql')


def list_examples():
    """This is an example. Please remove from your code before REST1 deadline.
    DB layer call for listing all rows of our example.
    """
    return exec_get_all('SELECT id, foo FROM example_table')
