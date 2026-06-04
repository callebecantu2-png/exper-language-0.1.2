import re

def handle_bare_function_call(self, line):
    if re.fullmatch(r"\w+\(.*\)", line):
        self.eval_expr(line)
        return True
    return False