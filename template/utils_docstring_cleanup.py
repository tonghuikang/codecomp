# https://gist.github.com/phpdude/1ae6f19de213d66286c8183e9e3b9ec1

# because usually there are limits to the amount of code you can submit

# usage
# python3 utils_docstring_cleanup.py template_networkx_raw.py > template_networkx.py

import sys
import ast
import astor  # read more at https://astor.readthedocs.io/en/latest/

if __name__ == "__main__":

    source = sys.argv[1]
    parsed = ast.parse(open(source).read())

    for node in ast.walk(parsed):
        # let's work only on functions & classes definitions
        if not isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            continue

        if not len(node.body):
            continue

        if not isinstance(node.body[0], ast.Expr):
            continue

        if not hasattr(node.body[0], 'value') or not isinstance(node.body[0].value, ast.Str):
            continue

        # Uncomment lines below if you want print what and where we are removing
        # print(node)
        # print(node.body[0].value.s)

        node.body = node.body[1:]

    print("# ***** Processed with utils_docstring_cleanup.py ******")
    print(astor.to_source(parsed))