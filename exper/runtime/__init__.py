from .assignment import handle_assignment
from .augmented_assignment import handle_augmented_assignment
from .delete import handle_delete
from .increment import handle_increment, handle_decrement
from .control_flow import handle_control_flow
from .function_call import handle_bare_function_call
from .preprocess import preprocess
from .call_methods import handle_method_call
from .scopes import (
    push_scope,
    pop_scope,
    find_scope,
    get_var,
    set_var,
    assign_var,
    del_var,
    has_var,
    get_target,
    set_target,
)
from .references import (
    is_mutable,
    clear_eval_refs,
    ref_key,
    resolve_eval_ref,
    log_ref_debug,
)