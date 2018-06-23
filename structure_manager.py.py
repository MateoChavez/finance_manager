#!/usr/bin/env python3

import argparse
from colorama import Fore, init, Style
import shelve

parser = argparse.ArgumentParser(description='Manage the structure and integrity of the database.')
parser.add_argument('-v', '--verbose', help='Increase the output verbosity', action='store_true')

args = parser.parse_args()


if args.verbose:
    init()
    print(Fore.GREEN + 'Verbosity turned on.\n')
    print(Style.RESET_ALL)

class Data:
    '''
    Manages the information contained in the database
    '''
    def __init__(self):
        # TODO

    def backup(self):
        '''
        Creates a backup of the information before any change is made
        '''
        # TODO: will create a backup of all files before any action in the program

    def check(self):
        '''
        Checks that the database has the proper structure
        '''
        # TODO

    def input(self, year, month, day, tags, value, description):
        '''
        tags:        Categories to which the expense belongs to
        value:       Amount of money spent, in NOK
        description: Small description of the purchase made
        '''

    def delete(self, year, month=None, day=None):
        '''
        Deletes a dictionary from the database. A backup will always be created before a deletion
        year:  select a year to delete
        month: select a month to delete, if None all months are deleted
        day:   select
        '''




class DataPrint:
    '''
    Handles all printouts to terminal of the Data object
    '''

    def __init__(self, data_obj):
        self.data = data_obj

    def range(self, day_obj):
        '''
        Prints all the financial information in an specified time
        '''

    def month(self, month_obj):
        '''
        Prints all information contained in a month object
        '''