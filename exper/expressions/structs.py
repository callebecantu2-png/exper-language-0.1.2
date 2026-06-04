import re

def step_structs(self, expr):
    match = re.fullmatch(r"(\w+)\(\)", expr)

    if match:
        name = match.group(1)

        if name in self.structs:
            obj = {"__struct__": name}

            for field in self.structs[name]["fields"]:
                if field in self.structs[name]["defaults"]:
                    obj[field] = self.eval_expr(
                        self.structs[name]["defaults"][field]
                    )
                else:
                    obj[field] = None

            return obj

    return expr
