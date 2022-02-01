# PÄÄOHJELMA - Selitys: mitä ohjelma tekee?

# KIRJASTOJEN JA MODULIEN LATAUS (sisäiset ja ulkoiset kirjastot)

# Otetaan käyttöön Windows-äänikirjasto (pythonin sisäänrakennettu kirjasto)
import winsound

# Otetaan käyttöön oma funktiomoduli
import funktiot_moduli

# Varsinainen pääohjelma alkaa tästä

# Lista mittaustuloksista, tyhjä ennen silmukkaa

mittaustulokset = []

# Ikuinen silmukka

while True:
    # Tätä toistetaan kunnes käyttäjä sulkee ohjelman
    
    seina1 = float(input("Anna ensimmäisen seinän pituus: "))
    seina2 = float(input("Anna toisen seinän pituus: "))
    lavistaja = float(input("Anna ristimitta: "))
    
    # Lisätään listaan arvoja
    mittaustulokset.append(seina1)
    mittaustulokset.append(seina2)
    mittaustulokset.append(lavistaja)
    
    # Kerrotaan onko tila suorakulmainen 
    print("Nurkka suorakulmainen", funktiot_moduli.suorakulma(seina1, seina2, lavistaja))

    # Kysytään käyttäjältä haluaako jatkaa
    lopetetaan = input("Paina L, jos haluat lopettaa ").upper()

    if lopetetaan == "L":
        break

# Ohjelman suoritus päättyy
mittauksia = len(mittaustulokset)
print("Kiitos tästä päivästä, teit", mittauksia, 'mittausta')

# Tulostetaan ruudulle kaikki mittaustulokset for:n avulla
print('Päivän mittaukset alla:')
for mittaus in mittaustulokset:
    print(mittaus)
    # print(mittaus, '\n')































# seina1 = 60
# seina2 = 80
# lavistaja = 100

# tulos = funktiot_moduli.suorakulma(seina1, seina2, lavistaja)
# print("nurkka suora?", tulos)