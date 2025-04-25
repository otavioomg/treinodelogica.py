while True:

    num1 = int(input("digite um número: "))
    print("A contagem é:")
    for i in range(num1,-1,-1):
        
        print(i)
        
    print("FIM")
    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break
print("Programa encerrado.")