import pytest, classiGeometriche

def test_Poligono():
    # 1. Creo un oggetto di tipo Poligono
    # 2. Testo le sue funzionalità (i suoi metodi, i suoi attributi, i suoi metodi dunder, ed il suo tipo)
    # NB: ricorda che puoi verificare con un assert il tipo di un oggetto con la funzione isinstance(nomeOggetto, tipo)
    p = classiGeometriche.Poligono(lati = [5, 5, 5], angoli = [60, 60, 60])
    assert p.lati == [5, 5, 5]
    assert p.angoli == [60, 60, 60]
    assert p.calcolaPerimetro() == 15
    assert p.sommaAngoli() == 180
    assert isinstance(p, classiGeometriche.Poligono)


def test_Triangolo():
    t = classiGeometriche.Triangolo(lato1 = 5, lato2 = 5, lato3 = 5, angolo1 = 60, angolo2 = 60, angolo3 = 60)
    assert t.__str__() == f"lati: {t.lati} -- angoli: {t.angoli} -- base: {t.base} -- altezza: {t.altezza:.2f}"
#   assert t.__add__





def test_rettangolo():
    pass