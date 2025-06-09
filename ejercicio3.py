# Sumar los digitos del resultado de una potencia


def suma():
    digitos = ""
    while True:
        try:
            num = int(input("Número: "))
            
            if num < 0:
                print("No se permiten números negativos")
            else:
                break
            
        except ValueError:
            print("Ingresa un dato valido")
    
    while True:
        try:
            potencia = int(input("Ingresa su potencia: "))
            
            if potencia < 0:
                print("No se permiten numeros negativos.")
            
            else:
                break
            
        except ValueError:
            print("Ingrese un dato valido.")
            
    if potencia == 0:
        resultado = 1
    
    else:
        resultado = pow(num, potencia)
    
    suma = 0
    
    resultado = str(resultado)
    
    for i in resultado:
        digitos = f"{i}" + "+" + digitos
        suma += int(i)
    
    digitos = digitos.rstrip("+")
    
    print(f"{num}^{potencia} = {resultado}")
    print(f"{digitos} = {suma}")
    

def main():
    print("""
          Ingresa el numero y su potencia
          
          """)
    suma()

main()
   