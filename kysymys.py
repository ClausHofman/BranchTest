# MODULI ERITYYPPISILLE KYSYMYKSILLE
# Kysytään käyttäjältä tietoja ja tarkistetaan tietojen oikeellisuus

def kysy_liukuluku(kysymys):
    """Kysyy käyttäjältä liukuluvun ja tarkistaa oikeellisuuden

    Args:
        kysymys (string): Kuvaruudulle tulostuva kysymys

    Returns:
        float: Käyttäjän syöttämä arvo liukuluvuksi muutettuna
    """
    # FIXME korjaa kysymyksestä puuttuva väli
    korjattu_kysymys = kysymys.strip() + ": "
    vastaus = input(korjattu_kysymys)
    try:
        arvo = float(vastaus)

    except:
        arvo = 0
        print("Syöttämäsi arvo ei ole luku")
    
    finally : 
        return arvo

