# palautusrepositorio

https://github.com/KaiserSin/ohtuvarasto
https://github.com/KaiserSin/webcounter

# Raportti: Copilot katselmointi

Copilot analysoi koodin ja löysi muutamia tärkeitä kohtia:

1.  **Logiikkavirhe pisteiden laskennassa (`won_point`):**
    Copilot huomasi, että alkuperäinen koodi antoi pisteen automaattisesti pelaajalle 2, jos nimi ei ollut pelaaja 1. Tämä oli vaarallista, koska mikä tahansa väärä nimi olisi kasvattanut pelaajan 2 pisteitä.

2.  **Ohjelman kaatumisvaara (`_point_name`):**
    Copilot varoitti, että jos peli jatkuu pitkään ja pisteet nousevat suuriksi, ohjelma voi kaatua (`KeyError`), koska sanakirjassa ei ole määritelty kaikkia numeroita.

3.  **Yleiskatsaus (PR Overview):**
    Copilot tunnisti oikein, että kyseessä oli koodin parantaminen (refaktorointi). Se listasi tehdyt muutokset, kuten vakioiden käytön ja muuttujien nimeämisen.

## Olivatko ehdotetut muutokset hyviä

Kyllä, ehdotukset olivat erittäin hyviä ja paransivat koodin laatua:

1.  **Parempi virheenkäsittely:** Copilot ehdotti `elif` ja virheen nostamista (`raise ValueError`), jos pelaajan nimi on väärä. Tämä estää bugit.
2.  **Turvallisempi koodi:** Ehdotus käyttää `.get()` listan suoran haun sijaan estää ohjelman kaatumisen yllättävissä tilanteissa.

## Kuinka hyödylliseksi koit Copilotin tekemän katselmoinnin

Koin Copilotin katselmoinnin **erittäin hyödylliseksi**.

1.  Se löysi selkeitä virheitä (bugeja), jotka ihminen saattaa helposti jättää huomaamatta.
2.  Automaattinen kuvaus Pull Requestille säästi aikaa kirjoittamiselta.
