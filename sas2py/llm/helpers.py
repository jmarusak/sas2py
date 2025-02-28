import json

def replace_names(code, names):
    names = json.loads(names)
    for source, target in names.items():
        code = code.replace(source, target)
    return code
