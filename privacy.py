"""
Privacyverklaring voor Aurelius.
Wordt getoond via een knop in de zijbalk.
"""

import streamlit as st


PRIVACY_TEKST = """
# Privacyverklaring Aurelius

**Laatst bijgewerkt:** [datum]

## 1. Wie wij zijn

Aurelius is een filosofische coach-app. De app wordt beheerd door
[naam / bedrijfsnaam], hierna te noemen "wij" of "de beheerder".

Voor vragen over deze privacyverklaring kun je contact opnemen via
[e-mailadres].

## 2. Welke gegevens wij verwerken

Wij verwerken alleen gegevens die je zelf aan ons geeft:

- **Een gebruikersnaam** — zodat je gesprekken en voortgang bewaard blijven.
- **Een e-mailadres** — uitsluitend ter verificatie van je account.
- **De antwoorden die je invult tijdens de incheck** — zoals wat je
  bezighoudt, hoe je je voelt, en welke intentie je hebt.
- **De gesprekken die je met de filosofen voert** — de tekstberichten
  die je uitwisselt met de coach.
- **Gearchiveerde sessies** — maar alleen als je daar zelf voor kiest.

## 3. Wanneer wij gegevens opslaan

Wij slaan gegevens **alleen op als jij een account aanmaakt**.
Zonder account worden er geen persoonlijke gegevens bewaard.

Wanneer je een account aanmaakt, bewaren wij je gebruikersnaam en
e-mailadres, zodat je later verder kunt waar je gebleven was.

## 4. Gearchiveerde sessies

Aan het einde van een gesprek kun je ervoor kiezen om de sessie te
**archiveren**. Dat is een keuze, geen verplichting.

- **Als je archiveert**, wordt het gesprek opgeslagen in jouw
  persoonlijke archief.
- **Als je niet archiveert**, wordt het gesprek niet bewaard.

Gearchiveerde sessies zijn **uitsluitend voor jou**. Ze zijn alleen
voor jou zichtbaar in je eigen archief.

## 5. Wat wij nooit doen

Wij gebruiken gearchiveerde sessies **nooit en te nimmer** voor andere
doeleinden dan het voor jou beschikbaar stellen van je eigen gesprekken.

Concreet betekent dit:

- **Niemand** krijgt jouw sessies te lezen.
- Er wordt **geen informatie** uit jouw sessies gehaald.
- Jouw gesprekken worden **niet gebruikt** voor onderzoek, analyse,
  marketing, of welke andere doeleinden dan ook.
- Jouw gesprekken worden **niet gedeeld** met derden.
- Jouw e-mailadres wordt **nooit gedeeld** met anderen.

## 6. Jouw e-mailadres

Je e-mailadres gebruiken wij **uitsluitend ter verificatie van je
account**. Het wordt niet gebruikt voor nieuwsbrieven, niet voor
marketing, en niet voor andere communicatie dan strikt noodzakelijk
voor het functioneren van de app.

## 7. Jouw rechten

Je hebt het recht om:

- Je account te laten verwijderen.
- Je gearchiveerde sessies te laten verwijderen.
- Inzage te vragen in de gegevens die wij van je hebben.
- Je gegevens te laten corrigeren.

Neem hiervoor contact op via [e-mailadres].

## 8. Beveiliging

Wij nemen passende maatregelen om jouw gegevens te beschermen tegen
verlies, misbruik en ongeoorloofde toegang. Jouw gegevens worden
opgeslagen op beveiligde servers.

## 9. Bewaartermijn

Wij bewaren je gegevens zolang je een account hebt. Als je je account
verwijdert, worden je gegevens verwijderd.

## 10. Wijzigingen

Wij kunnen deze privacyverklaring aanpassen. De meest recente versie
staat altijd in de app.

## 11. Contact

Voor vragen over deze privacyverklaring of over je gegevens kun je
contact opnemen via [e-mailadres].
"""


def toon_privacy():
    """Toont de privacyverklaring in de app."""
    st.markdown(PRIVACY_TEKST)
