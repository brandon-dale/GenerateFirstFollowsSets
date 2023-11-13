"""
Contains the declaration and implementation of the Grammar Class
Author: Brandon Dale
File: Grammar.py
Date: 11 November, 2023
"""


import Rule
import FirstFollowsSet
import Symbol
import json
import os


class Grammar:
    """
    Represents a CFG to process for firsts and follows sets.
    """

    def __init__(self, file_name: str):
        """
        Initializes a Grammar Object reads in the rules from the
        given json file.
        :param file_name: A json file containing the rules of the grammar
        """
        # Initialize Member Variables
        self.file_name: str = file_name
        self.rules: list = []
        self.sets: dict = {}  # dict mapping nt_name -> FirstFollowsSets

        # Read in the inputfile
        ext: str = os.path.splitext(self.file_name)[-1]
        if ext == '.txt':
            self.__read_txt_file()
        elif ext == '.json':
            self.__read_json_file()
        else:
            raise

    def build_first_follows(self) -> None:
        """
        Builds the first and follows sets for the existing rules in the grammar
        :return: None
        """
        # Repeatedly apply rule forms
        changed: bool = True
        while changed:
            # Temp value to track the set of changes
            changed = False

            # Apply Form A
            for rule in self.rules:
                nt_name, t_name, rule_num = rule.form_a()
                if nt_name:
                    self.sets[nt_name].add_firsts((t_name, rule_num))

            # Apply Form B
            for rule in self.rules:
                nt_i = rule.lhs.name
                nt_j, rule_num = rule.form_b()
                if nt_j is not None:
                    update_data: dict = {nt: rule_num for nt in self.sets[nt_j].firsts}
                    changed = self.sets[nt_i].add_firsts(update_data) or changed

            # Apply Form D
            for rule in self.rules:
                arr, rule_num = rule.form_d()
                if arr is None:
                    continue
                for nt, t in arr:
                    changed = self.sets[nt].add_follows((t, rule_num)) or changed

            # Apply Form E
            for rule in self.rules:
                arr, rule_num = rule.form_e()
                if arr is None:
                    continue
                for nt_i, nt_j in arr:
                    # first of j -> follows of i
                    update_data: dict = {t: rule_num for t in self.sets[nt_j].firsts}
                    changed = self.sets[nt_i].add_follows(update_data) or changed

            # Apply Form F
            for rule in self.rules:
                nt_j, rule_num = rule.form_f()
                if nt_j is None:
                    continue
                # follows(<nt_j>) += follows(<nt_i>)
                nt_i: str = rule.lhs.name
                update_data: dict = {t: rule_num for t in self.sets[nt_i].follows}
                changed = self.sets[nt_j].add_follows(update_data) or changed

            # Apply Form C
            for rule in self.rules:
                nt_i, rule_num = rule.form_c()
                if nt_i is not None:
                    update_data: dict = {nt: rule_num for nt in self.sets[nt_i].follows}
                    changed = self.sets[nt_i].add_firsts(update_data) or changed

    def print_sets(self) -> None:
        """
        Prints out the firsts and follows sets for each non-terminal
        :return: None
        """
        print("-" * 25)
        for name in self.sets:
            print(name)
            print(self.sets[name], end="\n\n")
            print("-" * 25)

    def print_rules(self) -> None:
        """
        Prints out the rules in the grammar
        :return: None
        """
        for rule in self.rules:
            print(f"({rule.rule_num:2}) ", end="")
            print(rule)

    def __read_txt_file(self) -> None:
        """
        Read in a set of rules from a text file.
        Each line must be in the form
            rule_num <nt> -> ...
        :return: None
        """
        in_file = open(self.file_name)
        lines = in_file.readlines()

        # Process each line
        for line in lines:
            # Extract the data from the rule
            split_list: list = line.split()
            rule_num: int = int(split_list[0])
            lhs: Symbol = Symbol.Symbol(split_list[1])
            rhs: list = split_list[3:]

            # Save the rule
            new_rule: Rule = Rule.Rule(lhs, rhs, rule_num)
            self.rules.append(new_rule)

            # Save the non-terminal if it has not yet been saved
            if (not lhs.terminal) and (lhs.name not in self.sets):
                self.sets[lhs.name] = FirstFollowsSet.FirstFollowsSets()

        in_file.close()

    def __read_json_file(self) -> None:
        """
        Read in a set of rules from a JSON file
        :return: None
        """
        # Load the JSON File
        f = open(self.file_name)
        data = json.load(f)

        # Read in each rule
        for rule_data in data:
            # Extract data and make rule object
            lhs = Symbol.Symbol(rule_data['lhs'])
            rhs = rule_data['rhs']
            rule_num = rule_data['number']
            # Add the rule to the list of rules
            new_rule: Rule = Rule.Rule(lhs, rhs, rule_num)
            self.rules.append(new_rule)

            # Save the non-terminal if it has not yet been saved
            if (not lhs.terminal) and (lhs.name not in self.sets):
                self.sets[lhs.name] = FirstFollowsSet.FirstFollowsSets()

        f.close()
