def juros_compostos(capital, taxa, tempo):

    capital = capital * (1 + (taxa/100))**tempo
    if tempo == 0:
        return capital
    return juros_compostos(capital, 0, tempo-1)


print(juros_compostos(100, 10, 5))

