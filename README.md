# Keskustelusovellus

Sovellus jossa käyttäjä pystyy aloittamaan, sekä liittymään keskustelualueille, joissa on omat ketjunsa. Käyttäjärooleja on peruskäyttäjä ja ylläpitäjä.

- Peruskäyttäjä voi luoda tilin ja kirjautua sisään
- Keskustelualueet näkee kuka vain, sekä niiden sisällä olevia aloituksia pääsee katsomaan
- Vain ylläpitäjä voi luoda keskustelualueen
- Kirjautunut käyttäjä voi luoda uuden ketjun alueelle, ajankohta on näkyvissä
- Kirjautunut käyttäjä voi kommentoida muiden ketjuihin, ajankohta näkyvissä
- Ylläpitäjä voi poistaa keskustelualueen, ketjun, taikka kommentin
- Ylläpitäjällä kaikki tavan käyttäjän oikeudet
- Kuka vaan voi hakea postauksia, mutta vain kirjautunut käyttäjä pääsee hakutuloksista aukaisemaan postauksen ja näkemään kommentit
- Käyttäjä voi tallentaa postauksia, joita pääsee etusivulta katsomaan.

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

DATABASE_URL= tietokannan paikallinen osoite
SECRET_KEY= salainen avain

Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt

Käynnistä tietokanta komennolla
start-pg.sh

Luo itsellesi database komennolla
psql
CREATE DATABASE imriina
\q

Määritä vielä tietokannan skeema komennolla

psql < tables.sql

Nyt voit käynnistää sovelluksen komennolla

flask run

Hyvää kevättä <3