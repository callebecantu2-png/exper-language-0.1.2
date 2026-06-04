import re

def step_in_operations(self, expr):
        match = re.fullmatch(r"(\[.*\])\s+in\s+(.+)", expr)
        if match:
            left = self.eval_expr(match.group(1))
            right = self.eval_expr(match.group(2))
            return repr([item in right for item in left])

        match = re.fullmatch(r"(.+?)\s+in\s+(.+)", expr)
        if match:
            left = self.eval_expr(match.group(1))
            right = self.eval_expr(match.group(2))
            return repr(left in right)

        return expr

def step_replace_operators(self, expr):

    result = ""

    in_string = False
    quote = ""

    i = 0

    while i < len(expr):

        c = expr[i]

        # entrar/sair de string
        if c in ['"', "'"]:

            if not in_string:
                in_string = True
                quote = c

            elif quote == c:
                in_string = False

            result += c
            i += 1
            continue

        # dentro da string não mexe em nada
        if in_string:
            result += c
            i += 1
            continue

        # &&
        if expr[i:i+2] == "&&":
            result += " and "
            i += 2
            continue

        # ||
        if expr[i:i+2] == "||":
            result += " or "
            i += 2
            continue

        # !
        if c == "!" and (i + 1 >= len(expr) or expr[i+1] != "="):
            result += " not "
            i += 1
            continue

        result += c
        i += 1

    result = re.sub(r"\bxor\b", "^", result)

    return result

def step_length(self, expr):

    def repl(match):

        name = match.group(1)

        try:
            value = self.get_target(name)
            return str(len(value))
        except:
            return "0"

    return re.sub(
        r"([a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*)\.length",
        repl,
        expr
    )
