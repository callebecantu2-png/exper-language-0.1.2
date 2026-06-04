import re

def handle_augmented_assignment(self, line):

    aug_ops = [
        (r"(\w+(?:\.\w+)*)\s*\+=\s*(.+)", lambda x, y: x + y),
        (r"(\w+(?:\.\w+)*)\s*-=\s*(.+)", lambda x, y: x - y),
        (r"(\w+(?:\.\w+)*)\s*\*\*=\s*(.+)", lambda x, y: x ** y),
        (r"(\w+(?:\.\w+)*)\s*\*=\s*(.+)", lambda x, y: x * y),
        (r"(\w+(?:\.\w+)*)\s*//=\s*(.+)", lambda x, y: x // y),
        (r"(\w+(?:\.\w+)*)\s*/=\s*(.+)", lambda x, y: x / y),
        (r"(\w+(?:\.\w+)*)\s*%=\s*(.+)", lambda x, y: x % y),
        (r"(\w+(?:\.\w+)*)\s*&=\s*(.+)", lambda x, y: x & y),
        (r"(\w+(?:\.\w+)*)\s*\|=\s*(.+)", lambda x, y: x | y),
        (r"(\w+(?:\.\w+)*)\s*\^=\s*(.+)", lambda x, y: x ^ y),
        (r"(\w+(?:\.\w+)*)\s*<<=\s*(.+)", lambda x, y: x << y),
        (r"(\w+(?:\.\w+)*)\s*>>=\s*(.+)", lambda x, y: x >> y),
    ]

    for regex, operation in aug_ops:

        match = re.match(regex, line)

        if not match:
            continue

        target = match.group(1)

        value = self.eval_expr(
            match.group(2)
        )

        current = self.get_target(target)

        result = operation(
            current,
            value
        )

        self.set_target(
            target,
            result
        )

        return True

    return False