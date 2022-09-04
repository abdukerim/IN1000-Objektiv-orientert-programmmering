class Celle:
   # Konstruktør
    def __init__(self):
        self._status = 'Doed'

    # Endre status
    def settDoed(self):
        self._status = 'Doed'

    def settLevende(self):
        self._status = 'Levende'

    # Hente status
    def erLevende(self):
        if self._status == 'Levende':
            return True
        return False

    #Hvis cellen er levende returners 'O', hvis Doed returners en prikk
    def hentStatusTegn(self):
        if self.erLevende():
            return ('O')

        return ('.')
