print('Loja de tintas')
area = int(input('Quantos m deseja pintar'))
cobertura = area // 3
latas = (cobertura // 18)
valor = latas ** 80 
print(f'Para cobrir os {area}m que  deseja, você ira precisar de {cobertura} e irá custar rs {valor:.f}'.format(cobertura, latas, valor))

??
