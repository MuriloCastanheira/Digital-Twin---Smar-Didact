lista = [0, 1, 0, 1, 0, 1, 0, 1]
tam = len(lista)
PWL = ""
x = 0
while x < tam:
    if x == 0:
        PWL = PWL + "( {}n {} {}n {}".format(x, lista[x], x + 1, lista[x])
    elif x == tam - 1:
        PWL = PWL + " {}.1n {} {}n {} )".format(x, lista[x], x + 1, lista[x])
    else:
        PWL = PWL + " {}.1n {} {}n {}".format(x, lista[x], x + 1, lista[x])
    x += 1
print(PWL)


