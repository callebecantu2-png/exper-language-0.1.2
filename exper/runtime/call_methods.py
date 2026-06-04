import re

def handle_method_call(self, line):

    match = re.fullmatch(
        r"(\w+)\.(\w+)\.(\w+)\((.*)\)",
        line
    )

    if not match:
        return False

    obj_name = match.group(1)
    field_name = match.group(2)
    method_name = match.group(3)
    arg_expr = match.group(4)

    if not self.has_var(obj_name):
        return False

    obj = self.get_var(obj_name)

    if not isinstance(obj, dict):
        return False

    if field_name not in obj:
        return False

    target = obj[field_name]

    args = []

    if arg_expr.strip():
        args.append(self.eval_expr(arg_expr))

    if method_name == "append":

        if not isinstance(target, list):
            raise Exception(
                f"{obj_name}.{field_name} não é uma lista"
            )

        target.append(*args)
        return True

    return False
