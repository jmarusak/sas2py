def get_sas_code():
    with open("sas2py/sas/data_step.sas", "r") as f:
        code = f.read()
        return code
