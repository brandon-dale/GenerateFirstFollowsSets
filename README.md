# GenerateFirstFollowsSets
A brief python program which generates the firsts and follows sets for a context free grammar.

Reads in a grammar from either a JSON or txt file and generates the first and follows sets for
each non-terminal in the grammar.

Version 1.0

---
# Necessary Notation

All non-terminals must be of the form <name>. For example, for a non-terminal called program, it
must be formatted as <program>.

Any string name that is not of the form <name>, will be assumed to be a terminal symbol.

For example, the rule "A -> bC" where A and C are non-terminal symbols and b is a terminal symbol,
should be formatted as "<A> -> b <C>".

If a rule is an epsilon/lambda move, for example "A -> λ" then it should be formatted with nothing on
the right-hand side of the arrow ("<A> -> ").

---
# Usage Directions
To use, ensure that you are using a version of python >= 3.5.

The following libraries are necessary for use:
  json, os, and sys.

To run the program, provide a single command line argument which contains the filename for the given input file, and
run the main.py script.


Example:

`
python main.py input.ext
`

---
# Formatting Input Files

Currently, two input file types are suppported: txt and json. Below are the necessary formats for each file type.

Example input files can be found in the repo folder "examples"

### txt files

Each line in the text file must be of the form:

`
rule_number <nt> -> rhs
`

where:
- rule_number is a unique integer rule number
- <nt> is the non-terminal symbol on the left-hand side of the rule
- -> is an arbitrary symbol without any whitespace (is ignored, but necessary)
- rhs is any length series of non-terminal and terminal symbols separated by spaces

### json files

The file should contains a single list of objects, where each object contains the data for a single rule.

The file should be formatted as such:

```
[
  {
    "lhs": "<program>",
    "rhs": ["begin", "<stmt_list>", "end"],
    "number": 1
  },
  ...
]
```

where:
- lhs is the non-terminal symbol on the left-hand side of the rule
- rhs is any length list of strings of non-terminal and terminal symbols.
- number is a valid rule number

Additional information can be added, but will be ignored to help with human readability.











---
# Planned Future Additions
- Support additional input file types
- Send output to a file and not the console
- Support additional formatting for non-terminals and terminals
- Extend epsilon transition notation
