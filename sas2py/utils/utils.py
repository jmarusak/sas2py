import difflib

def get_diff(a, b):
    a_lines = a.strip().splitlines(keepends=True)
    b_lines = b.strip().splitlines(keepends=True)
    diff = difflib.unified_diff(a_lines, b_lines, fromfile="Previous", tofile="Current", n=0, lineterm="\n")
    return "".join(diff)
