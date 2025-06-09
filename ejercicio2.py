# Entero a binario

def binario(num):
    binario = ""
    
    if num == 0:
        return "0"
    
    while num > 0:
        residuo = num % 2
        binario = str(residuo) + binario
        num = num // 2
        
    return binario

def main():
    print("""
          
          =====Ingrese un número para mostrar su valor en binario====
          ↓
          """)
    
    while True:
        try:
            numero = int(input(">>> "))
        
            if numero < 0:
                print("Ingrese números positivos.")
        
            else:
                print(f"----> {binario(numero)}")
                break
        
        except ValueError:
            print("ERROR. Dato invalido.")
main()        