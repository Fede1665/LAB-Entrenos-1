from entrenos import lee_entrenos

def test_lee_entrenos(datos):
    print ("Test de la función lee_entrenos")
    print ("Leídos", {len(datos)},"registros")
    print ("Mostrando los 3 primeros: ")
    for registro in datos[:3]:
        print("\t", registro)
    print ("Mostrando los tres últimos: ")
    for registro in datos[-3:]:
        print("\t", registro)
    print("="*30)

def test_tipos_entrenos()

if __name__=='__main__':
    datos = lee_entrenos("data/entrenos.csv")
    test_lee_entrenos(datos)
    