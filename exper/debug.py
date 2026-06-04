# ================= DEBUG =================
DEBUG = False
REF_DEBUG = False

def debug(*args):
    if DEBUG or REF_DEBUG:
        print("[DEBUG]:", *args)