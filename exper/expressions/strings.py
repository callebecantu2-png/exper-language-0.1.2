import re

def step_strings(self, expr):
    if (expr.startswith('"') and expr.endswith('"')) or \
    (expr.startswith("'") and expr.endswith("'")):

        string = expr[1:-1]

        def replace_var(match):
            inner = match.group(1)
            try:
                return str(self.eval_expr(inner))
            except:
                return match.group(0)

        while True:
            new_string = re.sub(r"\{([^{}]+)\}", replace_var, string)
            if new_string == string:
                break
            string = new_string

        return repr(string)

    return expr

def step_string_methods(self, expr):
    patterns = [
        (r"(.+)\.trim\(\)", lambda v: str(v).strip()),
        (r"(.+)\.upper\(\)", lambda v: str(v).upper()),
        (r"(.+)\.lower\(\)", lambda v: str(v).lower()),
        (r"(.+)\.capitalize\(\)", lambda v: str(v).capitalize()),
    ]

    for pattern, fn in patterns:
        m = re.fullmatch(pattern, expr)
        if m:
            return repr(fn(self.eval_expr(m.group(1))))

    return expr
