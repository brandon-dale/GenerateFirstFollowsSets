"""
Contains the declaration and implementation of the Symbol Class
Author: Brandon Dale
File: Symbol.py
Date: 11 November, 2023
"""


class Symbol:
    """
    Contains the information about a single symbol in the grammar.
    """

    def __init__(self, name: str):
        """
        Initializes a Symbol Object.
        :param name: a string name to initialize the object with.
                     If empty, will be considered to be lambda (terminal)
        """
        self.name: str = name
        self.terminal: bool = False if (len(name) > 0 and name[0] == "<") else True

    def __str__(self):
        """
        Returns a string representation of the symbol.
        :return: self.name if not empty string, else "lambda"
        """
        return self.name if len(self.name) > 0 else "lambda"
