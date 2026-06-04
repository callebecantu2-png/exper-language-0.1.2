import re
import os
import time

from . import handles as hds
from . import debug as dbg
from . import errors as er
from . import utils
from . import expressions as exps
from . import runtime as rt
from . import parser as prs
from . import calls

# ================= LINGUAGEM =================
class Exper:
    def __init__(self):
        self.scopes = [{}]
        self.functions = {}
        self.structs = {}
        self._eval_refs = {}

    push_scope = rt.push_scope
    pop_scope = rt.pop_scope
    find_scope = rt.find_scope
    get_var = rt.get_var
    set_var = rt.set_var
    assign_var = rt.assign_var
    del_var = rt.del_var
    has_var = rt.has_var
    get_target = rt.get_target
    set_target = rt.set_target
    is_mutable = rt.is_mutable
    clear_eval_refs = rt.clear_eval_refs
    ref_key = rt.ref_key
    resolve_eval_ref = rt.resolve_eval_ref
    log_ref_debug = rt.log_ref_debug

    handle_if = hds.handle_if
    handle_for = hds.handle_for
    handle_while = hds.handle_while
    handle_function = hds.handle_function
    handle_struct = hds.handle_struct
    get_block = prs.get_block

    call_user_function = exps.call_user_function
    
    # -------- EXPRESSÕES --------
    def eval_expr(self, expr):
        expr = expr.strip()
        dbg.debug("Evaluating:", expr)
        self.clear_eval_refs()

        expr = exps.step_strings(self, expr)
        if not isinstance(expr, str):
            return expr

        result = exps.step_short_vars(self, expr)
        if self.has_var(expr):
            return result

        expr = result

        result = exps.step_builtin_calls(self, expr)
        if result is not None:
            return result

        result = exps.step_object_property(self, expr)
        if result is not None:
            return result

        expr = exps.step_in_operations(self, expr)
        if not isinstance(expr, str):
            return expr

        expr = utils.safe_replace(self, expr)

        expr = exps.step_replace_operators(self, expr)
        expr = exps.step_length(self, expr)

        expr = exps.step_functions(self, expr)
        if not isinstance(expr, str):
            return expr

        result = exps.step_index(self, expr)
        if result is not None:
            return result

        expr = exps.step_string_methods(self, expr)
        if not isinstance(expr, str):
            return expr

        expr = exps.step_structs(self, expr)
        if not isinstance(expr, str):
            return expr

        expr = exps.step_properties(self, expr)
        return exps.step_python_eval(self, expr)

    # -------- FUNÇÕES --------
    def call_function(self, line):
        # Organiza as tentativas de chamadas em funções auxiliares para separar responsabilidades.
        # Cada handler retorna (found, result)
        for handler in [
            calls.handle_any,
            calls.handle_all,
            calls.handle_console_log,
            calls.handle_console_clear,
            calls.handle_console_input,
            calls.handle_sleep,
            calls.handle_conversions,
            calls.handle_list_append,
            calls.handle_list_pop,
            calls.handle_list_remove,
            calls.handle_list_insert,
        ]:
            found, result = handler(self, line)
            if found:
                return result
        return False

    # -------- RUN --------
    def run(self, code):
        lines = code.split("\n")
        lines = rt.preprocess(lines)
        i = 0

        while i < len(lines):
            
            line = lines[i].strip()

            self.current_line = i
            self.current_code = line

            if line == "":
                i += 1
                continue

            dbg.debug(f"Linha {i} -> {repr(line)}")

            if not line or line.startswith("#"):
                i += 1
                continue

            # Delete variable or function
            if rt.handle_delete(self, line):
                i += 1
                continue

            # ++
            if rt.handle_increment(self, line):
                i += 1
                continue

            # --
            if rt.handle_decrement(self, line):
                i += 1
                continue

            # Control flow
            flow_i = rt.handle_control_flow(self, line, lines, i)
            if flow_i is not None:
                i = flow_i
                continue

            # Augmented assignment
            if rt.handle_augmented_assignment(self, line):
                i += 1
                continue

            # Assignment (list, field, plain =, multiline)
            assign_i = rt.handle_assignment(self, line, lines, i)
            if assign_i is not None:
                i = assign_i
                continue

            # Method call
            if rt.handle_method_call(self, line):
                i += 1
                continue

            # call_function (console.log, sleep, etc)
            if self.call_function(line):
                i += 1
                continue

            # Bare function call (e.g. foo(123))
            if rt.handle_bare_function_call(self, line):
                i += 1
                continue

            raise er.ExperError(
                f"Erro de sintaxe: {line}",
                self.current_line,
                self.current_code
            )