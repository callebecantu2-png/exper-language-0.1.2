import re
from .. import errors as er

def handle_if(self, lines, i):

    executed = False

    while i < len(lines):

        line = lines[i].strip()

        if (
            line == "" or
            not line or
            line == " " or
            line.startswith("#")
        ):
            i += 1
            continue

        # termina se não for if/elif/else
        if not (line.startswith("if") or line.startswith("elif") or line.startswith("else")):
            break

        # IF / ELIF
        if line.startswith("if") or line.startswith("elif"):

            match = re.match(r"(if|elif)\s*\((.*)\)\s*{", line)
            if not match:
                raise er.ExperError("Erro de sintaxe no if", self.current_line, self.current_code)

            condition = match.group(2)

            block, i2 = self.get_block(lines, i)

            if not executed and self.eval_expr(condition):
                self.run("\n".join(block))
                executed = True

            i = i2 + 1
            continue

        # ELSE (IMPORTANTE: sempre faz parte do chain)
        if line.startswith("else"):

            block, i2 = self.get_block(lines, i)

            if not executed:
                self.run("\n".join(block))

            return i2 + 1

    return i