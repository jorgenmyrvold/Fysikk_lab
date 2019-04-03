#README
Har prøvd å finne ut hva som er galt med koden, men sliter med å finne ut av
det... Posisjoner stemmer over ens med målinger for bane 1 og 3, men ikke for 2 
og x-posisjon mot tid stemmer for bane 1, men ikke for 2 og 3.

Per nå står koden slik at den plotter to plot, ett med posisjon (y mot x) og 
et med x mot tid. 

`trvalues` og `iptrack` ligger under `utilities.py`, men er importert til
`eulers_metode.py` slik at de kan brukes der. `tider.py` er kode for å beregne
gjennomsnittstid og standardavvik.

Har modifisert `iptrack` slik at den returnerer polynomet p i tillegg til
`t_malt, x_malt, y_malt`. 

Send gjerne en mail til jorgeum@stud.ntnu.no hvis noe er uklart.