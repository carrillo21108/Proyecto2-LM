from algorithms.bruteForce import brute_force
from algorithms.dpll import dpll

def procesar_cadena(cadena):
    letras = ["p", "q", "r", "s"]
    resultado = ""
    i = 0

    while i < len(cadena):
        if cadena[i] == "-":
            for letra in letras:
                if i + len(letra) + 1 < len(cadena) and cadena[i + 1:i + len(letra) + 1] == letra:
                    resultado += f'("{cadena[i+1:i+len(letra)+1]}", False)'
                    i += len(letra) + 1
                    break

            resultado += cadena[i]
            i += 1
        else:
            for letra in letras:
                if cadena[i:i + len(letra)] == letra:
                    resultado += f'("{cadena[i:i+len(letra)]}", True)'
                    i += len(letra)
                    break

            resultado += cadena[i]
            i += 1

    return resultado

def main():
    cadena = input("Ingrese la forma clausal de expresiones en el formato: ")
    cadena = procesar_cadena(cadena[1:-1])
    converted = eval(f'[{cadena}]')
    print("\nSeleccione el algoritmo de resolución:")
    print("1. Fuerza Bruta")
    print("2. DPLL")
    choice = input()

    if choice == "1":
        res = brute_force(converted)
        print(res)
    elif choice == "2":
        res = dpll(converted)
        print(res)
    else:
        print("Selección no válida")
        return


if __name__ == "__main__":
    main()