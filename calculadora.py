def calculadora(num_1, num_2, operacion):
    if operacion == "+":
        return num_1 + num_2
    elif operacion == "-":
        return num_1 - num_2
    elif operacion == "*":
        return num_1 * num_2
    elif operacion == "/":
        return num_1 / num_2 if num_2 != 0 else "Error: No divisible entre 0"
    else:
        return "Operación no válida"

# --- Aquí pedimos los datos al usuario (Nota de tu instrucción) ---
print("======== Mi Super Calculadora ==========")
n1 = float(input("Escriba el valor del primer numero: "))
n2 = float(input("Escriba el valor del segundo numero: "))
op = input("¿Cual operacion deseas hacer? +, -, *, / -> ")

# Llamamos a la función y mostramos el resultado
resultado = calculadora(n1, n2, op)
print(f"El resultado es: {resultado}") 