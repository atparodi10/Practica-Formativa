# Factorial de un número

def factorial(num):
    factorial = 1
    
    if num == 0 or num == 1:
        return 1
    
    else:
        for i in range(1, num+1):
            anterior = factorial
            factorial *= i
            print(f"{i} * {anterior} = {factorial}")
        
        return factorial


def main():
    
    print("""
          
          -----> Calcular el Factorial de un número
          -----> Ingrese el número
          ↓
          
          """)
    
    while True:
        try:
            num = int(input(">>> "))
    
            if num < 0:
                print("No se permiten numeros negativos. Intente Nuevamente.")
        
            else:
                print(f"{num}! = {factorial(num)}")
                break
                
        
        except ValueError:
            print("ERROR. Ingrese un dato valido.")

main()
        
    