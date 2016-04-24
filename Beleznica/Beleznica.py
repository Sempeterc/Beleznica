class Kontakt:
    def __init__(self,ime,priimek,email,telefon,naslov):
        self.ime = ime
        self.priimek = priimek
        self.email = email
        self.telefon = telefon
        self.naslov = naslov

belezka = []

while True:
    vnos = raw_input("ali zelite dodati kontakt (da/ne):")

    if vnos == "da":
        nov_kontakt = Kontakt (
        ime = raw_input("vnesite ime kontakta:"),
        priimek = raw_input("vnesite primek kontakta:"),
        email = raw_input("vnesite email kontakta :"),
        telefon = raw_input("vnesite telefon kontakta:"),
        naslov = raw_input("vnesite naslov kontakta:"))

        belezka.append(nov_kontakt)

    elif vnos == "ne":
        print belezka
        break

    else:
        print "vnos je lahko samo da ali ne"



