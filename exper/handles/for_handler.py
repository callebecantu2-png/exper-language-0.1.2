import re
from .. import errors as er

def handle_for(self, lines, i):
    line = lines[i].strip()

    # ===== FOR K:V IN DICT =====
    m = re.match(
        r"for\s*\(\s*(\w+)\s*:\s*(\w+)\s+in\s+(.+?)\s*\)\s*{",
        line
    )

    if m:
        key_var = m.group(1)
        value_var = m.group(2)

        data = self.eval_expr(m.group(3))

        if not isinstance(data, dict):
            raise er.ExperError(
                "for k:v exige um dicionário",
                self.current_line,
                self.current_code
            )

        block, i2 = self.get_block(lines, i)

        for k, v in data.items():

            self.set_var(key_var, k)
            self.set_var(value_var, v)

            try:
                self.run("\n".join(block))

            except er.ContinueException:
                continue

            except er.BreakException:
                break

        return i2 + 1

    # ===== FOR ITEM IN =====
    m = re.match(
        r"for\s*\(\s*(\w+)\s+in\s+(.+?)\s*\)\s*{",
        line
    )

    if m:
        var_name = m.group(1)

        iterable = self.eval_expr(m.group(2))

        block, i2 = self.get_block(lines, i)

        for item in iterable:

            self.set_var(var_name, item)

            try:
                self.run("\n".join(block))

            except er.ContinueException:
                continue

            except er.BreakException:
                break

        return i2 + 1

    # ===== FOR CLÁSSICO =====
    m = re.match(r"for\s*\((.*)\)\s*{", line)
    if m:
        parts = m.group(1).split(";")

        if len(parts) != 3:
            raise er.ExperError(
                "Erro de sintaxe no for",
                self.current_line,
                self.current_code
            )

        init, cond, inc = parts

        self.run(init.strip())
        block, i2 = self.get_block(lines, i)

        while self.eval_expr(cond.strip()):

            try:
                self.run("\n".join(block))

            except er.ContinueException:
                self.run(inc.strip())
                continue

            except er.BreakException:
                break

            self.run(inc.strip())

        return i2 + 1
