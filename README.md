# Keskustelusovellus

Sovellus jossa käyttäjä pystyy aloittamaan, sekä liittymään keskustelualueille, joissa on omat ketjunsa. Käyttäjärooleja on peruskäyttäjä ja ylläpitäjä.

- Peruskäyttäjä voi luoda tilin ja kirjautua sisään
- Käyttäjä näkee eri keskustelualueet sekä ketjujen määrän
- Käyttäjä voi luoda uuden ketjun alueelle
- Käyttäjä voi kommentoida muiden ketjuihin
- Käyttäjä voi muokata laittamiaan/aloittamiaan viestejä, sekä poistaa ne
- Ylläpitäjällä samat oikeudet kuin käyttäjällä, sekä kyky poistaa ja luoda keskustelualueita
- Ylläpitäjä voi tehdä alueista salaisia ja päättää millä käyttäjillä pääsy
- Kirjautumattomalla käyttäjällä ei pääse osallistumaan keskusteluun

Nyt sovelluksessa pystyy luomaan käyttäjän jolla on rooli, kirjautumaan ulos, admin pystyy luomaan keskustelualustoja (jotka ei tosin vielä vie minnekkään). 

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

DATABASE_URL=postgresql:///imriina
SECRET_KEY=eef030a591621fa508712321ec0fd10f
Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
Määritä vielä tietokannan skeema komennolla

$ psql < schema.sql
Nyt voit käynnistää sovelluksen komennolla

$ flask run