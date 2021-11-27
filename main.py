#! /usr/bin/env python3

from package.birthdays import return_birthday
import argparse

parser=argparse.ArgumentParser(description="printing the birthday of a person")
parser.add_argument("name" ,type=str, help="insert a valid name",
 choices = ['Albert Einstein',
'Benjamin Franklin',
'Ada Lovelace',
'Donald Trump',
'Rowan Atkinson'])
parser.add_argument("-v",help="being more verbose", action="store_true")
args=parser.parse_args()


# I think I have to put a new parser for every function. so, parser_find_book, 
# parser_find_writer, parser_add_info and put add_argument for every argument that is needed.
# 

return_birthday(args.name,args.v)
