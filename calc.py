
def mostrar_alerta(resultado):
    print(f"Resultado: {resultado}")

while True:
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número (diferente de 0): "))
        if num2 != 0:
            break
        else:
            print("El segundo número no puede ser 0. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa números válidos.")

print("Elige la operación que deseas realizar:")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación (*)")
print("4. División (/)")
operacion = input("Ingresa el número o símbolo de la operación: ")

if operacion in ['1', '+']:
    resultado = num1 + num2
elif operacion in ['2', '-']:
    resultado = num1 - num2
elif operacion in ['3', '*']:
    resultado = num1 * num2
elif operacion in ['4', '/']:
    resultado = num1 / num2
else:
    print("Operación no válida.")
    resultado = None
    
if resultado is not None:
    mostrar_alerta(resultado)
