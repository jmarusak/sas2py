def get_sas_code():
    with open("sas2py/sas/data_step.sas", "r") as f:
        code = f.read()
        return code

def get_names_mapping():
    with open("sas2py/sas/stm_simple.json", "r") as f:
        names = f.read() 
        return names
