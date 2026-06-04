from .. import errors as er

def handle_control_flow(self, line, lines, i):
    """Lida com for, while, fn, struct, if, return, break, continue"""
    # return
    if line.startswith("return"):
        expr = line[len("return"):].strip()
        value = self.eval_expr(expr) if expr else None
        raise er.ReturnException(value)
    # for
    if line.startswith("for"):
        return self.handle_for(lines, i)
    # while
    if line.startswith("while"):
        return self.handle_while(lines, i)
    # fn
    if line.startswith("fn"):
        return self.handle_function(lines, i)
    # struct
    if line.startswith("struct"):
        return self.handle_struct(lines, i)
    # if/elif/else
    if line.startswith("if"):
        return self.handle_if(lines, i)

    # break
    if line == "break":
        raise er.BreakException()
    # continue
    if line == "continue":
        raise er.ContinueException()
    return None