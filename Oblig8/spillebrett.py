#forst importerer vi klasse celle og random

import random
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner): #oppretter vi klasse Spillebrett
       self._rader = rader
       self._kolonner = kolonner        #Konstruktør inneholder ogsaa generasjon
       self._generasjon = 0             #som starter fra null
       self._brett = []


       for i in range(self._rader):      #her lager vi rutenett
           celler = []                  #starter med en tom liste
           for j in range(self._kolonner):
               celler.append(Celle())       #legger vi til nye objekter i listen
           self._brett.append(celler)
       self._generer()



    def tegnBrett(self):
        print('\n'*3)                       #for mellomrom
        for rad in range(self._rader):      #looper vi gjennom brettet
            for kol in range(self._kolonner):
                print(self._brett[rad][kol].hentStatusTegn(), end="")
                #setter vi inn 'o' eller prikk som vi laget i klassen celle
            print()

    #sannsynligheten for at en celle er levende er 1/3,
    #for tilfeldig bestemme om cellen levende eller doed
    #bruker vi random.randint, fra 0 til og med 2
    def _generer(self):
        for rad in range(self._rader):
            for kol in range(self._kolonner):
                tall = random.randint(0,2)
                 #hvis vi faar null, saa cellen er levende
                if tall == 0:
                    self._brett[rad][kol].settLevende()


    def finnNabo(self, rad, kolonne):
        #forst oppretter vi en tom liste
        naboListe = []
        #en rad opp, samme rad og en rad ned, forrige kolonne, diagonal, og neste
        #kolonne skal være naboer
        for i in range(-1, 2):
            for j in range(-1,2):
                naboRad = rad + i
                naboKolonne = kolonne + j

                #Vi maa ogsaa tenke paa kanten av brettet,
                #hvis cellen kan ikke vaere utenfor brettet
                #derfor bestemmer vi gyldigheten
                gyldig = True

                #selve cellen heller ikke vaere naboen for seg selv
                if naboRad == rad and naboKolonne == kolonne:
                    gyldig = False

                #hvis naborad stoerre enn brette eller mindre enn null, da er det ugyldig
                if naboRad < 0 or naboRad >= self._rader:
                    gyldig = False

                #samme for kolonenene
                if naboKolonne < 0 or naboKolonne >= self._kolonner:
                    gyldig = False

                #Hvis alt er greit, leggeer vi naboene i nabolisten
                if gyldig:
                    naboListe.append(self._brett[naboRad][naboKolonne])
        return naboListe

    def finnAntallLevende(self):
        antalllevende = 0
        #looper gjennom cellene og ser om de lever og hvis gjoer det legger vi
        # 1 til anntalllevende
        for rad in range(self._rader):
            for kol in range(self._kolonner):
                if self._brett[rad][kol]._status == 'Levende':
                    antalllevende += 1

        #forteller antall levende celler
        return (f'Det er {antalllevende} levende celler.')


    def oppdatering(self):
        for rad in range(len(self._brett)):
            for kol in range(len(self._brett[rad])):
                cellen = self._brett[rad][kol]
                naboer = self.finnNabo(rad, kol)
                #looper gjennom brettet, finner naboer
                levendeNabo = []
                #saa finner vi levende naboceller
                for naboCelle in naboer:
                    if naboCelle.erLevende():
                        #lager vi en liste med levende naboceller
                        levendeNabo.append(naboCelle)
                #Vi skal se foerst om cellen selv er levende
                #hvis cellen er levende og har mindre enn 2 eller mer
                #enn 3 levende naboceller, skal cellen doed
                if cellen.erLevende() == True:
                    if len(levendeNabo) < 2 or len(levendeNabo) > 3:
                        cellen.settDoed()
                    #hvis cellen har 2 eller 3 levende naboceller
                    #skal cellen leve videre
                    if len(levendeNabo) == 2 or len(levendeNabo) == 3:
                        cellen.settLevende()
                #hvis cellen er doed, men har tre levende naboceller
                #skal cellen tilbake i liv
                else:
                    if len(levendeNabo) == 3:
                        cellen.settLevende()
