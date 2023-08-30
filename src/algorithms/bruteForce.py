import itertools

def brute_force(cnf):
    literales = set(literal[0] for clausula in cnf for literal in clausula)
    n = len(literales)

    for combinacion in itertools.product([True, False], repeat=n):
        solucion = set(zip(literales, combinacion))
        if all([bool(clausula.intersection(solucion)) for clausula in cnf]):
            return True, solucion

    return False, None