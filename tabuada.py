inicio = int(input("Digite o número em que a tabuada inicia: "))
fim = int(input("Digite o número em que a tabuada termina: "))
comeco = 0

for tabuada in range(inicio, fim + 1):
    
    if comeco <= fim:        
        comeco +=1
        print("_________________________________________ \n")
        print(f"Iniciando a tabuada do número {comeco} \n")
        for numeros in range(1, 11):
            calculo = comeco*numeros
            print(f"{comeco} X {numeros} = {calculo}")
