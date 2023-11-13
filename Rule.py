"""
Contains the declaration and implementation of the Rule Class
Author: Brandon Dale
File: Rule.py
Date: 11 November, 2023
"""

import Symbol


class Rule:
    """
    Container for a single rule in a CFG.
    """

    def __init__(self, lhs: Symbol, rhs: list, rule_num: int):
        """
        Initialize a Rule object.
        :param lhs: The name of a single non-terminal symbol in the CGF
        :param rhs: An ordered list of Symbols (non-terminal and terminal) for the rule
        :param rule_num: The rule number to use in references
        """
        # Set values
        self.lhs: Symbol.Symbol = lhs
        self.rhs: list = [Symbol.Symbol(s) for s in rhs]
        self.rule_num: int = rule_num

        # Error checking
        assert not lhs.terminal, \
            "ERROR - LHS OF A RULE MUST BE A NON-TERMINAL SYMBOL"

    def form_a(self) -> tuple:
        """
        Returns a list of tuples of the form (<nt>, T, int) if the rule is of
        the following form:
            <nt_i> --> T_k ...
        :return: If the rule is of this form, returns (lhs, rhs[0], rule_num).
                 Else, returns (None, None, None)
        """
        if (len(self.rhs) > 0) and self.rhs[0].terminal:
            return self.lhs.name, self.rhs[0].name, self.rule_num
        else:
            return None, None, None

    def form_b(self) -> tuple:
        """
        Returns a tuple containing the name of the first non-terminal on the rhs
        of the rule, if one exists and the rule_num. Else None, None
        :return: (self.rhs[0], self.rule_num) if that element exists
                 and is a non-terminal. Else (None, None)
        """
        if len(self.rhs) == 0 or self.rhs[0].terminal:
            return None, None
        else:
            return self.rhs[0].name, self.rule_num

    def form_c(self) -> tuple:
        """
        Returns a tuple containing the name of the lhs non-terminal and the
        rule_num if the rhs is empty (lambda)
        :return: (lhs.name, rule_num) if rhs is empty. Else (None, None)
        """
        return (None, None) if len(self.rhs) > 0 else (self.lhs.name, self.rule_num)

    def form_d(self) -> tuple:
        """
        Returns a tuple with the rule_num and a list of tuples containing
        pairs of non-terminals and terminals of the form:
            <> --> ... <nt_i> T_k ...
        :return: If any part of the rule satisfies the above condition:
                 ( [(<nt_i>, T_k), ...], rule_num). Else (None, None)
        """
        arr = []
        for i in range(len(self.rhs) - 1):
            if (not self.rhs[i].terminal) and self.rhs[i + 1].terminal:
                arr.append((self.rhs[i].name, self.rhs[i+1].name))

        return (arr, self.rule_num) if len(arr) > 0 else (None, None)

    def form_e(self) -> tuple:
        """
        Returns a tuple with the rule_num and a list of tuples containing
        pairs of non-terminals and terminals of the form:
            <> --> ... <nt_i> <nt_j> ...
        :return: If any part of the rule satisfies the above condition:
                 ( [(<nt_i>, <nt_j>), ...], rule_num). Else (None, None)
        """
        arr = []
        for i in range(len(self.rhs) - 1):
            if (not self.rhs[i].terminal) and (not self.rhs[i + 1].terminal):
                arr.append((self.rhs[i].name, self.rhs[i+1].name))

        return (arr, self.rule_num) if len(arr) > 0 else (None, None)

    def form_f(self) -> tuple:
        """
        Returns a typle with the rule_num and the last non-terminal in rhs
        if the rule follows the following form:
            <nt_i> -> ... <nt_j>
        :return: If the rule matches the above form, it returns the tuple
                 (<nt_j>, rule_num). Else (None, None)
        """
        if (len(self.rhs) > 0) and (not self.rhs[-1].terminal):
            return self.rhs[-1].name, self.rule_num
        else:
            return None, None

    def __str__(self):
        """
        Returns a string representation of the rule
        :return: A string version of the rule in the form lhs -> rhs
        """
        res: str = str(self.lhs)
        res += " --> "
        res += " ".join(map(str, self.rhs)) if len(self.rhs) > 0 else "λ"
        return res
