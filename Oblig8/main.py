from spillebrett import Spillebrett


def main():

    # Vi tar imot input fra brukeren for antall rader og kolonner, og lager vi brettet:
    rad = int(input('Oppgi antall rader: \n'))
    kolonner = int(input('Oppgi antall kolonner: \n'))
    obj = Spillebrett(rad, kolonner)
    obj.tegnBrett()
    print('\n')
    print('Første Generasjon')
    #vi skal ogsaa fortelle  hvor mange levende celler det er i
    print(obj.finnAntallLevende())
    print('\n')
    #saa ber vi om brukeren skal fortsette til neste generasjon
    #hvis brukeren taster inn Enter skal vi oppdatere brettet
    nesteSteg = ''
    generasjon = 1
    while nesteSteg != 'q':
        #hvis taste inn 'q', avslutter vi alt
        nesteSteg = input('Trykk enter for neste generasjon eller q til å avslutte: \n')

        if nesteSteg == '':

            obj.oppdatering()
            #Oppdatere cellenenes status og tegne nytt brett
            obj.tegnBrett()
            print('\n')
            #generasjon skal oekes med 1
            generasjon += 1
            print(f'Generasjon: {generasjon}')
            #fortelle hvormange levende celler det er
            print(obj.finnAntallLevende())
            print('\n')





main()
