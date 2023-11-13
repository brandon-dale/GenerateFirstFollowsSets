"""
Contains the declaration and implementation of the FirstFollowsSet Class
Author: Brandon Dale
File: FirstFollowsSet.py
Date: 11 November, 2023
"""


class FirstFollowsSets:
    """
    Container for the firsts and follows set for a non-terminal symbol
    """

    def __init__(self):
        """
        Initialize a FirstFollowsSets Object - Sets initially empty
        """
        self.firsts = {}
        self.follows = {}

    def add_firsts(self, insert_data) -> bool:
        """
        Adds the insertData into the firsts set without overwriting data.
        :param insert_data: Either a dictionary of the form
                            {terminal_symbol_name : rule_num}
                           or a tuple of the form
                            (terminal_symbol_name,  rule_num)
        :return: True if any symbol inserted. False if symbol already existed in set
        """
        # Insertion on dictionary
        if type(insert_data) is dict:
            res: bool = False
            for terminal in insert_data:
                # Update results variable if necessary
                if terminal not in self.firsts:
                    self.firsts[terminal] = insert_data[terminal]
                    res = True
            return res

        # Insertion on tuple
        if type(insert_data) is tuple:
            terminal, rule_num = insert_data
            res: bool = False
            if terminal not in self.firsts:
                res = True
                self.firsts[terminal] = rule_num
            return res

        raise TypeError

    def add_follows(self, insert_data) -> bool:
        """
        Adds the insertData into the follows set without overwriting data.
        :param insert_data: Either a dictionary of the form
                            {terminal_symbol_name : rule_num}
                           or a tuple of the form
                            (terminal_symbol_name, rule_num)
        :return: True if any symbol inserted. False if symbol already existed in set
        """
        # Insertion on dictionary
        if type(insert_data) is dict:
            res: bool = False
            for terminal in insert_data:
                # Update results variable if necessary
                if terminal not in self.follows:
                    self.follows[terminal] = insert_data[terminal]
                    res = True
            return res

        # Insertion on tuple
        if type(insert_data) is tuple:
            terminal, rule_num = insert_data
            res: bool = False
            if terminal not in self.follows:
                res = True
                self.follows[terminal] = rule_num
            return res

        raise TypeError

    def __str__(self):
        """
        Returns a string representation of the pair of sets
        :return: A formatted string version of the pair of sets
        """
        res: str = f"Firsts:\n"
        res += self.__stringify_dict(self.firsts)
        res += "Follows:\n"
        res += self.__stringify_dict(self.follows)
        res += "\n"
        return res

    def __stringify_dict(self, d):
        """
        Convert the dictionary d into a formatted string version
        :return:
        """
        if len(d) == 0:
            return "{}"

        res: str = "{\n"
        for key in d:
            res += f"\t{key:15} ({d[key]})\n"

        res += "}\n"
        return res
