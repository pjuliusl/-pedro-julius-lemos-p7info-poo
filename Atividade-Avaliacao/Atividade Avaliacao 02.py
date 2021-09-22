text = 0
separator = "-"
while True:
    frase = input("Digite a frase desejada(Digite 0 caso deseje se retirar.): ").split()
    tamanho = []
    
    for i in frase:
        tamanho.append(str(len(i)))
        if len(i) >= text:
            text = len(i)
            maiorPalavra = i
    print(separator.join(tamanho))

    end = str(input("Digite 0 caso deseje finalizar o programa, caso deseje continuar pressione ENTER:"))
    if end == "0":
        break

print()
print("A maior palavra é: %s" % maiorPalavra)