def push_scope(self):
    self.scopes.append({})

def pop_scope(self):
    if len(self.scopes) > 1:
        self.scopes.pop()

def find_scope(self, name):
    for scope in reversed(self.scopes):
        if name in scope:
            return scope
    return None

def get_var(self, name):
    scope = self.find_scope(name)
    if scope is None:
        raise KeyError(name)
    value = scope[name]

    return value

def set_var(self, name, value):
    self.scopes[-1][name] = value

def assign_var(self, name, value):
    scope = self.find_scope(name)
    if scope is not None:
        scope[name] = value
    else:
        self.set_var(name, value)

def del_var(self, name):
    scope = self.find_scope(name)
    if scope is not None:
        del scope[name]

def has_var(self, name):
    return self.find_scope(name) is not None

def get_target(self, name):
    parts = name.split(".")

    value = self.get_var(parts[0])

    for part in parts[1:]:
        value = value[part]

    return value

def set_target(self, name, value):
    parts = name.split(".")

    if len(parts) == 1:
        self.assign_var(name, value)
        return

    obj = self.get_var(parts[0])

    for part in parts[1:-1]:
        obj = obj[part]

    obj[parts[-1]] = value
