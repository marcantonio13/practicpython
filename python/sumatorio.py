
def sumatorio(numero):
    if numero > 0:
        numero += sumatorio(numero -1)
        print(numero)
    return numero

sumatorio(3)

    