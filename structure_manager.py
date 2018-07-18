#!/usr/bin/env python3

import argparse
import shelve

from datetime import datetime
from colorama import Fore, init, Style
from pprint import pprint


class Data:
    '''
    Manages the information contained in the database
    '''
    def __init__(self):
        
        self.database = shelve.open('database')
        print(list(self.database.keys()))

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

    def input(self, year, month, day, tag, groups, value, description):
        '''
        tags:        Categories to which the expense belongs to
        groups:      Ways of grouping within the tag
        value:       Amount of money spent, in NOK
        description: Small description of the purchase made
        '''

        info = {
            'tag':         tag,
            'group':       group,
            'value':       value,
            'description': description,
        }

        year_dic = self.database.get(year, None)
        if year_dic is None:  # Check if a dictionary for the year already exists. 
            year_dic = {
                month: {
                    day: [info]
                }
            }
        else:
            month_dic = year_dic.get(month, None)    
            if month_dic is None:  # Check if a dictionary for the month already exists.
                year_dic[month] =  {
                    day: [info]
                }
            else:
                day_dic = month_dic.get(day, None)
                if day_dic is None:  # Check if a dicitonary for the day already exists. 
                    year_dic[month][day] =  [info]
                else:
                    year_dic[month][day].append(info)
        
    self.database[year] = year_dic  # Save the information onto the shelve file. 


    def delete(self, year=None, month=None, day=None):
        '''
        Deletes a dictionary from the database. A backup will always be created before a deletion
        year:  select a year to delete
        month: select a month to delete, if None all months are deleted
        day:   select
        '''
        for key in self.database.keys():
            del self.database[key]



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


def main():
    parser = argparse.ArgumentParser(description='Manage your finances.')
    parser.add_argument('-inp', '--input', help='Added an item to the finance database')
    parser.add_argument('-v', '--verbose', help='Increase the output verbosity', action='store_true')

    args = parser.parse_args()


    if args.verbose:
        init()
        print(Fore.GREEN + 'Verbosity turned on.\n')
        print(Style.RESET_ALL)

        database = Data()
        #database.delete('2018')
        database.input('2018', '4', '1', 'income', 'salary', 10000, 'Early pay')

if __name__ == '__main__':
    main()
