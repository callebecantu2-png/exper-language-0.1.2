import re
import os

def handle_console_log(self, line):
    m = re.fullmatch(r"console\.log\((.*)\)", line)
    if m:
        val = self.eval_expr(m.group(1))
        print(val)
        return True, True
    return False, None

def handle_console_clear(self, line):
    if line == "console.clear()":
        os.system("cls" if os.name == "nt" else "clear")
        return True, True
    return False, None

def handle_console_input(self, line):
    m = re.fullmatch(r'console\.input\((.*)?\)', line)
    if m:
        prompt = self.eval_expr(m.group(1))
        return True, input(prompt)
    return False, None