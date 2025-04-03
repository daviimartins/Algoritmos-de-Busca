class Vertex:  # Define Vertex first, as Adjacent will reference it
    def __init__(self, label: str, target_distance: int):
        self.label = label
        self.target_distance = target_distance
        self.adjacent = []  # This is a list, not a callable function
        self.visited = False

    def add_adjacent(self, adjacent):  # This method will add an adjacent vertex
        self.adjacent.append(adjacent)

    def list_adjacent(self):
        for adjacent in self.adjacent:
            print(f"{adjacent.vertex.label} - {adjacent.cost}")

class Adjacent:
    def __init__(self, vertex: 'Vertex', cost: int):  # Use a string to reference 'Vertex'
        self.vertex = vertex
        self.cost = cost

class Graph:
    porto_uniao = Vertex("Porto União", 231)
    paulo_frontin = Vertex("Paulo Frontin", 186)
    canoinhas = Vertex("Canoinhas", 154)
    irati = Vertex("Irati", 139)
    palmeira = Vertex("Palmeira", 110)
    sao_mateus = Vertex("São Mateus", 150)
    tres_barras = Vertex("Três Barras", 143)
    mafra = Vertex("Mafra", 117)
    lapa = Vertex("Lapa", 86)
    contenda = Vertex("Contenda", 41)
    araucaria = Vertex("Araucária", 37)
    curitiba = Vertex("Curitiba", 0)
    campo_largo = Vertex("Campo Largo", 29)
    balsa_nova = Vertex("Balsa Nova", 51)
    sao_jose_dos_pinhais = Vertex("São José dos Pinhais", 15)
    tijucas_do_sul = Vertex("Tijucas do Sul", 64)

    porto_uniao.add_adjacent(Adjacent(paulo_frontin, 46))
    porto_uniao.add_adjacent(Adjacent(canoinhas, 78))
    porto_uniao.add_adjacent(Adjacent(sao_mateus,87))

    paulo_frontin.add_adjacent(Adjacent(porto_uniao, 46))
    paulo_frontin.add_adjacent(Adjacent(irati, 75))

    canoinhas.add_adjacent(Adjacent(porto_uniao, 78))
    canoinhas.add_adjacent(Adjacent(tres_barras, 12))
    canoinhas.add_adjacent(Adjacent(mafra, 66))

    tres_barras.add_adjacent(Adjacent(canoinhas, 12))
    tres_barras.add_adjacent(Adjacent(sao_mateus, 43))

    sao_mateus.add_adjacent(Adjacent(tres_barras, 43))
    sao_mateus.add_adjacent(Adjacent(porto_uniao, 87))
    sao_mateus.add_adjacent(Adjacent(irati, 57))
    sao_mateus.add_adjacent(Adjacent(palmeira, 77))
    sao_mateus.add_adjacent(Adjacent(lapa,60))

    irati.add_adjacent(Adjacent(sao_mateus, 57))
    irati.add_adjacent(Adjacent(paulo_frontin, 75))
    irati.add_adjacent(Adjacent(palmeira, 75))

    palmeira.add_adjacent(Adjacent(irati, 75))
    palmeira.add_adjacent(Adjacent(sao_mateus, 77))
    palmeira.add_adjacent(Adjacent(campo_largo, 55))

    campo_largo.add_adjacent(Adjacent(palmeira, 55))
    campo_largo.add_adjacent(Adjacent(balsa_nova, 22))
    campo_largo.add_adjacent(Adjacent(curitiba, 29))

    balsa_nova.add_adjacent(Adjacent(campo_largo, 22))
    balsa_nova.add_adjacent(Adjacent(contenda, 19))
    balsa_nova.add_adjacent(Adjacent(curitiba, 51))

    contenda.add_adjacent(Adjacent(balsa_nova, 19))
    contenda.add_adjacent(Adjacent(lapa, 26))
    contenda.add_adjacent(Adjacent(araucaria, 18))

    lapa.add_adjacent(Adjacent(contenda, 26))
    lapa.add_adjacent(Adjacent(mafra, 57))
    lapa.add_adjacent(Adjacent(sao_mateus, 60))

    mafra.add_adjacent(Adjacent(lapa, 57))
    mafra.add_adjacent(Adjacent(tijucas_do_sul, 99))
    mafra.add_adjacent(Adjacent(canoinhas, 66))

    tijucas_do_sul.add_adjacent(Adjacent(mafra, 99))
    tijucas_do_sul.add_adjacent(Adjacent(sao_jose_dos_pinhais, 49))

    sao_jose_dos_pinhais.add_adjacent(Adjacent(tijucas_do_sul, 49))
    sao_jose_dos_pinhais.add_adjacent(Adjacent(curitiba, 15))

    curitiba.add_adjacent(Adjacent(sao_jose_dos_pinhais, 15))
    curitiba.add_adjacent(Adjacent(araucaria, 37))
    curitiba.add_adjacent(Adjacent(campo_largo, 29))
    curitiba.add_adjacent(Adjacent(balsa_nova, 51))

    araucaria.add_adjacent(Adjacent(curitiba, 37))
    araucaria.add_adjacent(Adjacent(contenda, 18))