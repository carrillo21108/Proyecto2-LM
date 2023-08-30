def select_literal(cnf):
    for clausula in cnf:
        for literal in clausula:
            return literal[0]


def dpll(cnf, asignaciones={}):
    if len(cnf) == 0:
        return True, asignaciones

    if any([len(clausula) == 0 for clausula in cnf]):
        return False, None

    l = select_literal(cnf)

    new_cnf = [clausula for clausula in cnf if (l, True) not in clausula]
    new_cnf = [clausula.difference({(l, False)}) for clausula in new_cnf]
    sat, vals = dpll(new_cnf, asignaciones|{l: True})
    if sat:
        return sat, vals

    new_cnf = [clausula for clausula in cnf if (l, False) not in clausula]
    new_cnf = [clausula.difference({(l, True)}) for clausula in new_cnf]
    sat, vals = dpll(new_cnf, asignaciones|{l: False})
    if sat:
        return sat, vals

    return False, None