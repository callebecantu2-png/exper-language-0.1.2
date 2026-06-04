import re
import time

def handle_sleep(self, line):
    m = re.fullmatch(r"sleep\((.*)\)", line)
    if m:
        ms = self.eval_expr(m.group(1))
        time.sleep(ms / 1000)
        return True, True
    return False, None

def handle_any(self, line):
    match = re.fullmatch(r"any\((.*)\)", line)
    if match:
        val = self.eval_expr(match.group(1))
        return True, any(val)
    return False, None

def handle_all(self, line):
    match = re.fullmatch(r"all\((.*)\)", line)
    if match:
        val = self.eval_expr(match.group(1))
        return True, all(val)
    return False, None
