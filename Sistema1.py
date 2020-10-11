'''
Sistema que comprime frases.
    1. La frase debe contener de 25 a 100 caracteres.
    2. Se permiten signos de puntuación y cualquier otro caracter.
    3. Cuenta con 5 intentos para ingresar correctamente la frase.
'''
def comprime():
    i = 0
    while i < 5:
        print(":: Sistema compresor :: ")
        frase = input("-> Ingresa una frase de 25 a 100 caracteres:\n").lower()

        if len(frase) < 25:
            print("¡Ups! Frase muy corta, ingresa mas de 25 caracters.")
        elif len(frase) > 100:
            print("¡Ups! Frase muy larga, ingresa menos de 100 caracteres.")
        else:
            vocales = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ä', 'ë', 'ï', 'ö', 'ü', 'à', 'è', 'ì', 'ò', 'ù')
            for letra in vocales:
                frase = frase.replace(letra, "")
                frase = frase.replace(" ","")
            print("-> Tu frase comprimida es: ", frase, " con ", len(frase), " caracteres totales.")
            break
        i+=1
    if i == 5:
        print("¡Ups! Has sobrepasado el límite de intentos. ¡Bye!")

comprime()
