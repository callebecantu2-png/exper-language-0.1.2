import re

def handle_list_append(self, line):
    m = re.fullmatch(r"(\w+)\.append\((.*)\)", line)
    if m:
        self.get_var(m.group(1)).append(self.eval_expr(m.group(2)))
        return True, True
    return False, None

def handle_list_pop(self, line):
    m = re.fullmatch(r"(\w+)\.pop\((.*)\)", line)
    if m:
        return True, self.get_var(m.group(1)).pop(self.eval_expr(m.group(2)))
    return False, None

def handle_list_remove(self, line):
    m = re.fullmatch(r"(\w+)\.remove\((.*)\)", line)
    if m:
        self.get_var(m.group(1)).remove(self.eval_expr(m.group(2)))
        return True, True
    return False, None

def handle_list_insert(self, line):
    m = re.fullmatch(r"(\w+)\.insert\((.*),(.*)\)", line)
    if m:
        self.get_var(m.group(1)).insert(
            self.eval_expr(m.group(2)),
            self.eval_expr(m.group(3))
        )
        return True, True
    return False, None
