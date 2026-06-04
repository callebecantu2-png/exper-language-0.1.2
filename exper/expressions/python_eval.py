from .. import errors as er

def step_python_eval(self, expr):
    resolved = self.resolve_eval_ref(expr)
    if resolved is not None:
        return resolved

    try:
        if self._eval_refs:
            return eval(expr, {"__builtins__": __builtins__}, dict(self._eval_refs))
        return eval(expr)
    except Exception as e:
        raise er.ExperError(
            f"Erro na expressão: {expr}\nErro: {e}",
            self.current_line,
            self.current_code
        )
