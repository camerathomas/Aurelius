"""
Algemene voorwaarden voor Aurelius.
Wordt getoond via een knop in de zijbalk.
"""

import streamlit as st


VOORWAARDEN_TEKST = """
# Algemene voorwaarden Aurelius

**Laatst bijgewerkt:** [datum]

## 1. Wie wij zijn

Aurelius is een filosofische coach-app. De app wordt beheerd door
[naam / bedrijfsnaam], hierna te noemen "wij" of "de aanbieder".

**Contactgegevens:**
- E-mail: [e-mailadres]
- Adres: [vestigingsadres]

## 2. Toepasselijkheid

Deze algemene voorwaarden zijn van toepassing op alle overeenkomsten
tussen jou (de consument) en ons (de aanbieder) met betrekking tot het
gebruik van de Aurelius-app.

Door een account aan te maken of de app te gebruiken, ga je akkoord
met deze voorwaarden.

## 3. De dienst

Aurelius is een filosofische coach-app. De app biedt:

- Gesprekken met AI-gestuurde filosofen
- Gepersonaliseerde coaching-sessies
- Een archief van eerdere sessies (optioneel)

Wij doen ons uiterste best om de dienst beschikbaar en functioneel te
houden, maar wij garanderen geen ononderbroken beschikbaarheid.

## 4. Accounts en registratie

Je maakt een account aan met een gebruikersnaam en e-mailadres.
Je bent zelf verantwoordelijk voor:

- De juistheid van je gegevens
- Het geheimhouden van je inloggegevens
- Alle activiteiten die via jouw account plaatsvinden

## 5. Prijzen en betaling

Wij bieden de volgende opties:

- **Losse sessie:** €2,50 per gesprek
- **Basic abonnement:** €5,00 per maand
- **Gold abonnement:** €15,00 per maand

Alle prijzen zijn inclusief btw, tenzij anders vermeld.

Betaling vindt plaats via de betaalmethoden die in de app worden
aangeboden. Bij een abonnement wordt het bedrag maandelijks
automatisch verlengd, tenzij je opzegt.

## 6. Herroepingsrecht

**Je hebt het recht om binnen 14 dagen na aankoop de overeenkomst
zonder opgave van redenen te herroepen.**

Dit recht geldt voor de eerste aankoop van een abonnement. Voor losse
sessies geldt het herroepingsrecht alleen als de sessie nog niet is
gebruikt.

Om je herroepingsrecht uit te oefenen, stuur je een e-mail naar
[e-mailadres] met een duidelijke verklaring dat je de overeenkomst
herroept. Wij bevestigen de ontvangst en betalen binnen 14 dagen
het volledige bedrag terug.

**Uitzondering:** het herroepingsrecht vervalt zodra je een sessie
daadwerkelijk hebt gebruikt, omdat de dienst dan volledig is geleverd.

## 7. Gebruik van de dienst

Je mag de app alleen gebruiken voor persoonlijke, niet-commerciële
doeleinden. Het is niet toegestaan om:

- De app te gebruiken voor illegale doeleinden
- De app te reverse-engineeren of te kopiëren
- Inhoud te uploaden die in strijd is met de wet
- De app te gebruiken om anderen te schaden

Wij behouden ons het recht voor om je account te schorsen of te
beëindigen als je deze voorwaarden schendt.

## 8. Intellectueel eigendom

Alle inhoud in de app — waaronder de filosofen-personages, de
gesprekslogica, en de vormgeving — is eigendom van de aanbieder.

Jouw gesprekken en inzichten zijn van jou. Wij claimen geen eigendom
over de inhoud die jij inbrengt.

## 9. Aansprakelijkheid

Aurelius is een coach-app, geen therapeut, geen arts, en geen
crisis-dienst. De app is niet bedoeld voor medische of psychische
noodgevallen.

Wij zijn niet aansprakelijk voor:

- Schade die voortkomt uit het gebruik van de app
- Beslissingen die je neemt op basis van gesprekken in de app
- Technische storingen of gegevensverlies

Onze aansprakelijkheid is beperkt tot het bedrag dat je voor de
dienst hebt betaald.

## 10. Beschikbaarheid en wijzigingen

Wij kunnen de dienst op elk moment wijzigen, tijdelijk opschorten, of
beëindigen. Bij belangrijke wijzigingen informeren wij je vooraf.

Als wij de dienst definitief beëindigen, heb je recht op een
proportionele terugbetaling van je abonnement.

## 11. Klachten en geschillen

Heb je een klacht? Neem contact op via [e-mailadres]. Wij proberen
binnen 14 dagen te reageren.

Als wij er niet samen uitkomen, kun je je klacht voorleggen aan de
bevoegde rechter in Nederland.

## 12. Toepasselijk recht

Op deze voorwaarden is Nederlands recht van toepassing.

## 13. Wijzigingen van deze voorwaarden

Wij kunnen deze voorwaarden aanpassen. De meest recente versie staat
altijd in de app. Bij belangrijke wijzigingen informeren wij je
vooraf via e-mail of een melding in de app.

## 14. Contact

Voor vragen over deze voorwaarden kun je contact opnemen via
[e-mailadres].
"""


def toon_voorwaarden():
    """Toont de algemene voorwaarden in de app."""
    st.markdown(VOORWAARDEN_TEKST)
