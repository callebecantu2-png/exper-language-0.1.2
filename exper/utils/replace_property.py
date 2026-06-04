def replace_property(self):
    def fn(match):
                
        obj = match.group(1)
        field = match.group(2)

        if self.has_var(obj):

            value = self.get_var(obj)

            if isinstance(value, dict):

                if field in value:

                    v = value[field]

                    if isinstance(v, str):
                        return repr(v)

                    if self.is_mutable(v):
                        return self.ref_key(v)

                    return str(v)

        return match.group(0)
    
    return fn
