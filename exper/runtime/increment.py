import re

def handle_increment(self, line):
    m = re.match(r"(\w+)\+\+$", line)
    if m:
        name = m.group(1)
        self.assign_var(name, self.get_var(name) + 1)
        return True
    return False

def handle_decrement(self, line):
    m = re.match(r"(\w+)--$", line)
    if m:
        name = m.group(1)
        self.assign_var(name, self.get_var(name) - 1)
        return True
    return False
