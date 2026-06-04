import re
from .. import utils
from .. import errors as er

def step_functions(self, expr):
    while True:
        found = False

        for name in self.functions:
            search = f"{name}("
            start = expr.find(search)

            if start == -1:
                continue

            pos = start + len(search)
            depth = 1
            args_raw = ""

            while pos < len(expr):
                c = expr[pos]

                if c == "(":
                    depth += 1
                elif c == ")":
                    depth -= 1
                    if depth == 0:
                        break

                args_raw += c
                pos += 1

            full_call = expr[start:pos+1]

            value = self.call_user_function(name, args_raw)

            if expr.strip() == full_call.strip():
                return value

            if self.is_mutable(value):
                replacement = self.ref_key(value)
            else:
                replacement = repr(value)

            expr = expr.replace(full_call, replacement, 1)

            found = True
            break

        if not found:
            break

    return expr

def step_builtin_calls(self, expr):

    if expr.startswith("console.input("):
        return self.call_function(expr)

    if expr.startswith("int("):
        return self.call_function(expr)

    if expr.startswith("float("):
        return self.call_function(expr)

    if expr.startswith("str("):
        return self.call_function(expr)

    m = re.fullmatch(r"any\((.*)\)", expr)

    if m:
        return any(
            self.eval_expr(
                m.group(1)
            )
        )

    m = re.fullmatch(r"all\((.*)\)", expr)

    if m:
        return all(
            self.eval_expr(
                m.group(1)
            )
        )

    return None
    
def call_user_function(self, name, args_raw):
    func = self.functions[name]

    raw_args = []
    if args_raw.strip():
        raw_args = utils.split_args(args_raw)

    positional = []
    named = {}

    for arg in raw_args:
        if "=" in arg:
            k, v = arg.split("=", 1)
            named[k.strip()] = self.eval_expr(v)
        else:
            positional.append(self.eval_expr(arg))

    pos = 0
    bound_args = {}

    self.push_scope()
    try:
        for p in func["params"]:
            if p in named:
                arg_value = named[p]
            elif pos < len(positional):
                arg_value = positional[pos]
                pos += 1
            elif p in func["defaults"]:
                arg_value = self.eval_expr(
                    func["defaults"][p]
                )
            else:
                raise er.ExperError(
                    f"Parâmetro obrigatório faltando: {p}",
                    self.current_line,
                    self.current_code
                )

            bound_args[p] = arg_value

            if self.is_mutable(arg_value):
                self.log_ref_debug(
                    f"call {name}({p}) before function",
                    arg_value
                )

            self.set_var(p, arg_value)

            if self.is_mutable(arg_value):
                self.log_ref_debug(
                    f"call {name}({p}) inside function",
                    self.get_var(p)
                )

        try:
            self.run("\n".join(func["block"]))
        except er.ReturnException as r:
            return r.value

        return None
    finally:
        for p, arg_value in bound_args.items():
            if self.is_mutable(arg_value):
                self.log_ref_debug(
                    f"call {name}({p}) after function",
                    arg_value
                )
        self.pop_scope()
