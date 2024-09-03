slownik = {
    'LOL' : 'odpowiedź na coś zabawnego',
    'CRINGE' : 'coś dziwnego lub wstydliwego',
    'ROFL' : 'odpowiedź na żart',
    'SHEESH' : 'lekka dezaprobata',
    'CREEPY' : 'straszny, złowieszczy',
    'AGGRO' : 'stać się agresywnym/zły'
}

slowo = input('Napisz słowo, którego nie rozumiesz: ')

if slowo in slownik.keys():
    print(slownik[slowo])
else:
    print('Nie znaleziono słowa!')

print(slownik)
