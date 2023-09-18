cube = lambda x:x**3

def cubo () :
    base = input("Ingrese la base a elevar al cubo: ")
    resultado = int (base)**3
    resultado = str (resultado)
    
    print("\n"+base+" elevado al cubo es: "+resultado+"\n")
    


def mostrar_menu():
    print("1. Convierte cadena a Mayusculas (lambda)")
    print("2. Convierte cadena a Mayusculas")
    print("3. Calcular el cubo de un numero (lambda)")
    print("4. Calcular el cubo de un numero")
    print("5. Resuelve ecuacion de segundo grado (lambda)")
    print("6. Resuelve ecuacion de segundo grado")
    print("7. Salir")
    
while True:
    mostrar_menu()
    opcion=input("Selecciona una opcion: ")
    
    if opcion=="3":
        numero = input("Ingrese el numero del que desea calcular el cubo: ")
        resultado = cube(int (numero))
        numero = str(numero)
        resultado = str(resultado)
        print("\n" + numero + "elevado al cubo es: " + resultado)
        
    elif opcion=="4":
        cubo()
        
    elif opcion=="7":
        print("Saliendo del programa")
        break
        
    else:
        print("Opcion Invalida")