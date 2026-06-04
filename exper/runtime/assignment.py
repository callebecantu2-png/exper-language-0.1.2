import re

def handle_assignment(self, line, lines, i):
    """
    Trata atribuições. Retorna novo valor de i se for atribuição, ou None.
    """
    # Atribuição lista
    if re.match(r"\w+\[.*\]\s*=", line):
        var, val = line.split("=", 1)
        name = var[:var.index("[")]
        idx = self.eval_expr(var[var.index("[")+1:var.index("]")])
        self.get_var(name)[idx] = self.eval_expr(val)
        return i+1

    # -------- OBJ.FIELD = --------
    match = re.match(
        r"(\w+)\.(\w+)\s*=\s*(.+)",
        line
    )
    if match:
        obj = match.group(1)
        field = match.group(2)
        value = match.group(3)
        if not self.has_var(obj):
            raise Exception(
                f"Objeto '{obj}' não existe"
            )
        self.get_var(obj)[field] = self.eval_expr(value)
        return i+1

    # Atribuição normal =
    assign_index = -1
    depth = 0
    in_string = False
    quote = ""

    for idx, c in enumerate(line):
        if c in ['"', "'"]:
            if not in_string:
                in_string = True
                quote = c
            elif quote == c:
                in_string = False
        if in_string:
            continue
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif (c == "=" and depth == 0 and not (idx > 0 and line[idx-1] in "!<>=")):
            assign_index = idx
            break

    if assign_index != -1:
        var = line[:assign_index].strip()
        val = line[assign_index+1:].strip()

        # ===== MULTILINHA =====
        if val == "{" or val == "[" or val == "(":
            open_char = val
            close_char = {"{": "}", "[": "]", "(": ")"}[open_char]
            full_value = val + "\n"
            count = 1
            j = i + 1
            while j < len(lines):
                current = lines[j]
                count += current.count(open_char)
                count -= current.count(close_char)
                full_value += current + "\n"
                if count == 0:
                    break
                j += 1
            val = full_value.strip()
            i = j

        evaluated = self.eval_expr(val)

        if re.search(r"\b" + re.escape(var) + r"\b", val):
            self.assign_var(var, evaluated)
        else:
            self.set_var(var, evaluated)

        return i + 1
    return None
