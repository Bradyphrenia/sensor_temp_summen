class weisel:
    def __init__(self):
        self.__eilegerate = 0
        self.__temperatur = 0.0

    def eilegerate(self, temp):
        self.__temperatur = round(temp)
        try:
            self.__eilegerate = round(22.8295 * (self.__temperatur ** 1.4254))
        except ValueError:
            self.__eilegerate = 0
        except TypeError:
            self.__eilegerate = 0
        return self.__eilegerate


class kaste:
    def __init__(self, tage):
        self.__tage = tage  # Anzahl der Tage
        self.__anzahl = []  # Anzahl der Mitglieder der Kaste
        for i in range(self.__tage):  # Generieren der jeweiligen Liste
            self.__anzahl.append(0)

    def fifo(self, _in: int) -> int:  # first in -> first out der Liste
        _out = self.__anzahl.pop(self.__tage - 1)
        self.__anzahl.insert(0, _in)
        return _out

    def fin(self, _in):  # Hinzufügen einer Startmenge
        self.__anzahl[0] = self.__anzahl[0] + _in

    @property
    def summe(self):  # Summe der Liste
        return sum(self.__anzahl)


class eier(kaste):
    def __init__(self):
        super().__init__(3)


class offeneBrut(kaste):
    def __init__(self):
        super().__init__(5)


class verdeckelteBrut(kaste):
    def __init__(self):
        super().__init__(13)


class bienen(kaste):
    def __init__(self):
        super().__init__(40)  # Abgang nach ca. 40 Tagen


class brutnest:
    def __init__(self):
        self.__eier = eier()
        self.__offeneBrut = offeneBrut()
        self.__verdeckelteBrut = verdeckelteBrut()
        self.__bienen = bienen()
        self.ausBienen = 0  # Abgang der Bienen

    def berechne(self, datum, temp):
        k = weisel()
        eilege = k.eilegerate(temp)  # Eilegerate der Weisel
        ausEier = self.__eier.fifo(eilege)  # neu geschlüpfte Eier
        ausOffeneBrut = self.__offeneBrut.fifo(ausEier)  # neu verdeckelte Brut
        ausVerdeckelteBrut = self.__verdeckelteBrut.fifo(ausOffeneBrut)  # neu geschlüpfte Bienen
        self.ausBienen = self.__bienen.fifo(ausVerdeckelteBrut)  # neu abgegangene Bienen

    @property
    def eier(self):
        return self.__eier.summe

    @property
    def offeneBrut(self):
        return self.__offeneBrut.summe

    @property
    def verdeckelteBrut(self):
        return self.__verdeckelteBrut.summe

    @property
    def bienen(self):
        return self.__bienen.summe

    @property
    def toteBiene(self):
        return self.ausBienen

    def setzeBienen(self, anz):  # Anzahl der Bienen zum Start der Simulation setzen
        self.__bienen.fin(anz)

    @property
    def relation(self):
        return round(
            ((self.__verdeckelteBrut.summe + self.__offeneBrut.summe + self.__eier.summe) / self.__bienen.summe) * 100)


def main():
    pass


if __name__ == '__main__':
    main()
