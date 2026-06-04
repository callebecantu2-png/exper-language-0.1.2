from .. import errors as er

def handle_delete(self, line):
    # del variável
    if line.startswith("del "):
        name = line[4:].strip()
        if self.has_var(name):
            self.del_var(name)
        else:
            raise er.ExperError(
                f"Variável '{name}' não existe",
                self.current_line,
                self.current_code
            )
        return True
    # delete função
    if line.startswith("delete "):
        name = line[7:].strip()
        if name in self.functions:
            del self.functions[name]
        else:
            raise er.ExperError(
                f"Função '{name}' não existe",
                self.current_line,
                self.current_code
            )
        return True
    return False
