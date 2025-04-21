import random

from english_words import get_english_words_set


# Vai mostrando as letras.
def replace(word, letra, word_hidden):
    i = 0
    for x in word:
        i = i + 1
        if (x == letra):
            word_hidden[i - 1] = letra


# O estado init_state=1 habilita as mensagens de debug e teste() confirma que deu
def teste():
    print(teste)


def jogo():
    print("  ____  _____  ___  _____    ____    __      ____  _____  ____   ___    __   ")
    print(" (_  _)(  _  )/ __)(  _  )  (  _ \\  /__\\    ( ___)(  _  )(  _ \\ / __)  /__\\  ")
    print(".-_)(   )(_)(( (_-. )(_)(    )(_) )/(__)\\    )__)  )(_)(  )   /( (__  /(__)\\ ")
    print("\\____) (_____)\\___/(_____)  (____/(__)(__)  (__)  (_____)(_)\\_) \\___)(__)(__)")
    word = random.choice(list(get_english_words_set(['web2'], alpha=True, lower=True)))
    word_hidden = list("_" * len(word))
    Nerro = 5
    while (Nerro):
        print("A palavra é:\n", ''.join(word_hidden))
        if (init_state == '1'):
            print(word, "\n")
        print('Número de vidas:', Nerro, '\n')
        second_state = input(
            "Para tentar uma letra digite [1]\npara tentar uma palavra, digite [2]\npara ver a palavra digite [3]")
        if (second_state == '1'):
            letra = input("letra:")
            if (letra in word):
                replace(word, letra, word_hidden)
            else:
                Nerro = Nerro - 1
        elif (second_state == '2'):
            palavra = input("palavra:")
            if (palavra in word && len(palavra) == len(word)):
                print("Parabéns !!!!!!!!!1!!!!")
                exit(1)
            else:
                Nerro == Nerro - 1
        elif (second_state == '3'):
            print(word)
            exit(69420)

        else:
            print("(╯°□°）╯︵ ┻━┻")
    print("Perdeu! A palavra era:", word)


if (__name__ == '__main__'):
    while (True):
        init_state = input("[1] para teste e [2] para jogo:")
        if (init_state == '1'):
            teste()
            jogo()
            exit(0)
        elif (init_state == '2'):
            jogo()
            exit(0)
        else:
            print("(ಥ﹏ಥ)")
        
