"""
Contains the main driver code to read in a grammar and
generate the first and follows sets.
Author: Brandon Dale
File: main.py
Date: 11 November, 2023
"""


import Grammar
import sys


def main():
    # Validate Command Line Arguments and get input file
    assert len(sys.argv) >= 2, "ERROR - MUST PROVIDE ARGUMENT FOR INPUT FILE"
    input_file: str = sys.argv[1]

    # Generate the first and follows sets
    grammar = Grammar.Grammar(input_file)
    grammar.build_first_follows()
    grammar.print_sets()


if __name__ == '__main__':
    main()