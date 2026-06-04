import re

def step_short_vars(self, expr):
    if self.has_var(expr):
        value = self.get_var(expr)

        return value

    return expr

def step_index(self, expr):

    match = re.fullmatch(
        r"(\w+)\[(.*)\]",
        expr
    )

    if match:

        var = match.group(1)

        index = self.eval_expr(
            match.group(2)
        )

        return self.get_var(var)[index]

    return None
