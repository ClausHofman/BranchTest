class Ostolista:
    # Konstruktori eli olionmuodostin
    def __init__(self, numero, kauppa, ostokset):
        self.numero = numero
        self.kauppa = kauppa
        self.ostokset = ostokset

    # Funktio, jolla lasketaan olion ostosten määrä -> metodi
    def nimikkeita(self):
        maara = len(self.ostokset)
        print(maara)
        
# Luodaan ostoslista1-objekti
ostoslista1 = Ostolista(1, 'X-market', ['Maksalaatikkoa', 'Pullaa', 'Keksejä'])

# Kutsutaan ostoslista1:n nimikkeita()-metodia
if __name__ == "__main__":
    ostoslista1.nimikkeita()

#     x = lambda a, b, c : a - b + c
# print(x(3, 5, 1))

# While-silmukka ja kierroslaskuri
# Silmukkaa voidaan käyttää halutun toistomäärän saavuttamiseksi

# 10 kierroksen While laskuri, kierrokset 0-9
laskuri = 0
if __name__ == "__main__":
    while laskuri < 10:
        print('nyt on menossa kierros', laskuri)
        laskuri += 1

# Laskurin ehto on täynnä jo ennen silmukkaa, silmukkaa ei suoriteta
laskuri = 10
if __name__ == "__main__":
    while laskuri < 10:
        print('nyt on menossa kierros', laskuri)
        laskuri += 1

# Silmukka, jota toistetaan kunnes käyttäjä ei enää halua jatkaa
jatketaan = 'K'
if __name__ == "__main__":
    while jatketaan == 'K':
        print('hippopotamus')
        jatketaan = input('Paina K, jos haluat jatkaa :').upper()

# Silmukka, johon on sijoitettu erillinen poistumismekanismi (tyhjä vastaus)
arvattava_nimi = 'Iines'
arvaus =  'x'
arvausten_maara = 0
if __name__ == "__main__":
    while arvaus != arvattava_nimi:
        arvaus = input('Arvaa mikä mun nimi on? ').capitalize()
        arvausten_maara += 1
        if arvaus != arvattava_nimi:
            print('Väärin')
        else:
            print('Arvasit oikein')
        
        # Jos vastaus on tyhjä merkkijono, poistutaan silmukasta
        if arvaus == '':
            break
    print('Arvasit', arvausten_maara, 'kertaa')

# Täytetään listaa kunnens käyttäjä syöttää tyhjän arvon
kauppalista = []
if __name__ == "__main__":
    while True:
        ostos = input('Mitä pitää tuoda kaupasta? ')
        if ostos == '':
            break
        kauppalista.append(ostos)

    print('Ja tuo kaupasta:', kauppalista)
if __name__ == "__main__":
    for merkinta in kauppalista:
        print('Osta', merkinta )