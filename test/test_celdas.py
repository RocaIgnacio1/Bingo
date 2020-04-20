from src.bingo import carton

def test_contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda

    assert contador == 15

def test_al_menos_una_celda_ocupada_por_columna():
    mi_carton = carton()
    contador = 0
    for filas in mi_carton:
        for celda in filas:
            contador = contador + celda

        assert contador >= 6
