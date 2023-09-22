cube = lambda x:x**3

def cubo () :
    base = input("Ingrese la base a elevar al cubo: ")
    resultado = int (base)**3
    resultado = str (resultado)
    
    print("\n"+base+" elevado al cubo es: "+resultado+"\n")
    
def res_cuadr ():
    a = input("Ingrese el coeficiente de x^2: ")
    b = input("Ingrese el coeficiente de x: ")
    c = input("Ingrese el termino independiente: ")
    
    if int(a)==0:
        print("La ecuacion no es cuadratica")
        
    else:
        resultado1 = (-int(b)+(((int(b)**2)-(4*int(a)*int(c)))**0.5))/(2*int(a))
        resultado2 = (-int(b)-(((int(b)**2)-(4*int(a)*int(c)))**0.5))/(2*int(a))
    
        resultado1 = str(resultado1)
        resultado2 = str(resultado2)
        
        print("Las racies de "+a+"x^2+"+b+"x+"+c+" son: ")
        print(resultado1+" y "+resultado2)
    
sol1_cuad = lambda a,b,c: ((-b + ((b**2 - 4*a*c)**0.5)) / (2*a)) if a != 0 else None

sol2_cuad = lambda a,b,c: ((-b - ((b**2 - 4*a*c)**0.5)) / (2*a)) if a != 0 else None
    

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
    
    if opcion=="1":
        res_cuadr();
        
    elif opcion=="2":
        a=input("Ingrese el coeficiente de x^2: ")
        b=input("Ingrese el coeficiente de x: ")
        c=input("Ingrese el termino independiente: ")
        raiz1 = sol1_cuad(int(a),int(b),int(c))
        raiz2 = sol2_cuad(int(a),int(b),int(c))
        
        print("Las soluciones para "+a+"x^2+"+b+"x+"+c+" son: ")
        print(str(raiz1)+" y "+str(raiz2))
        
    elif opcion=="3":
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