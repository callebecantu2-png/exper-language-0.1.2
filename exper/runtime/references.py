MUTABLE_TYPES = (dict, list)

def is_mutable(self, value):
    return isinstance(value, MUTABLE_TYPES)

def clear_eval_refs(self):
    # self._eval_refs = {}
    ...

def ref_key(self, obj):
    key = f"__exper_ref_{len(self._eval_refs)}__"
    self._eval_refs[key] = obj
    return key

def resolve_eval_ref(self, expr):
    if isinstance(expr, str) and expr in self._eval_refs:
        return self._eval_refs[expr]
    return None

def log_ref_debug(self, label, obj):
    from .. import debug as dbg
    if dbg.REF_DEBUG and is_mutable(obj):
        dbg.debug(f"[REF] {label}: id={id(obj)} type={type(obj).__name__}")
