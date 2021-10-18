pPescados = input('Digito o numero de peixes pescados: ')

if pPescados > 50:
    pExedidos = pPescados - 50
    multa = pExedidos * 4.00
    print 'Você exedeu',pExedidos,'do numero permitido de peixes\n    O valor de sua multa é de R$',multa #não coube na linha
else:
    print'Você não execeu o limite de peixes pescados, ;D'