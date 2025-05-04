from palavraforca import palavra
letras_usuario = []
tentativas = 6

while tentativas > 0:
    print("\n")
    if tentativas == 6:
        print(" _____\n |    |\n |    \n |    \n |    \n |")
    elif tentativas == 5:
        print(" _____\n |    |\n |    O\n |    \n |    \n |")
    elif tentativas == 4:
        print(" _____\n |    |\n |    O\n |    |\n |    \n |")
    elif tentativas == 3:
        print(" _____\n |    |\n |    O\n |   /|\n |    \n |")
    elif tentativas == 2:
        print(" _____\n |    |\n |    O\n |   /|\\\n |    \n |")
    elif tentativas == 1:
        print(" _____\n |    |\n |    O\n |   /|\\\n |   / \n |")
    elif tentativas == 0:
        print(" _____\n |    |\n |    O\n |   /|\\\n |   / \\\n |")

    exibir = ""
    for letra in palavra:
        if letra in letras_usuario:
            exibir += letra + ""
        else:
            exibir += "_"
    print("palavra:", exibir, end="")

    if "_" not in exibir:
        print(f"\nparabens! você ganhou! a palavra era {palavra}")
        break

    chute = input("digite uma letra para advinhar: ").lower()
    if chute in letras_usuario:
        print("voce ja tentou essa letra.")
    else:
        letras_usuario.append(chute)
        if chute not in palavra:
            tentativas -= 1
            print(f"letra errada! tentativas restantes {tentativas}")

else:
    print(f"você perdeu! A palavra era {palavra} ")