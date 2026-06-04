import re
from .. import utils

def step_object_property(self, expr):
    match = re.fullmatch(
        r"(\w+)\.(\w+)",
        expr
    )

    if not match:
        return None

    obj = match.group(1)
    field = match.group(2)

    if self.has_var(obj):

        value = self.get_var(obj)

        if isinstance(value, dict):

            if field in value:
                return value[field]

    return None

def step_properties(self, expr):
    return re.sub(
        r"\b([a-zA-Z_]\w*)\.([a-zA-Z_]\w*)\b",
        utils.replace_property(self),
        expr
    )
