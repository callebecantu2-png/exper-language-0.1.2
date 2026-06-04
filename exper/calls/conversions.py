import re

def handle_conversions(self, line):
    for f in ["int", "float", "str"]:
        m = re.fullmatch(rf"{f}\((.*)\)", line)
        if m:
            val = self.eval_expr(m.group(1))
            # eval(f) is safe as f is controlled ["int","float","str"]
            return True, eval(f)(val)
    return False, None