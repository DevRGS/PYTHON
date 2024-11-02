# Dicionário contendo as quantidades de pedras necessárias para cada nível de boost para cada natureza
# Dicionário contendo as quantidades de pedras necessárias para cada nível de boost para cada natureza
boost_dict = {
    "1": {"nome": "Pedra", "valores": [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 58, 62, 66, 70, 74, 78, 83]},
    "2": {"nome": "Água", "valores": [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 58, 62, 66, 70, 74, 78, 83]},
    "3": {"nome": "Planta", "valores": [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 58, 62, 66, 70, 74, 78, 83]},
    "4": {"nome": "Veneno", "valores": [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 58, 62, 66, 70, 74, 78, 83]},
    "5": {"nome": "Terra", "valores": [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 58, 62, 66, 70, 74, 78, 83]},
    "6": {"nome": "Gelo", "valores": [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 58, 62, 66, 70, 74, 78, 83]},
    "7": {"nome": "Voador", "valores": [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 58, 62, 66, 70, 74, 78, 83]},
    "8": {"nome": "Normal", "valores": [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 58, 62, 66, 70, 74, 78, 83]},
    "9": {"nome": "Inseto", "valores": [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 58, 62, 66, 70, 74, 78, 83]},
    "10": {"nome": "Elétrico", "valores": [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 58, 62, 66, 70, 74, 78, 83]},
    "11": {"nome": "Fogo", "valores": [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 58, 62, 66, 70, 74, 78, 83]},
    "12": {"nome": "Psíquico", "valores": [1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 38, 41, 44, 47, 50, 53]},
    "13": {"nome": "Fantasma", "valores": [1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 38, 41, 44, 47, 50, 53]},
    "14": {"nome": "Lutador", "valores": [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 38, 41, 44, 47, 50, 53]},
    "15": {"nome": "Metal", "valores": [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 38, 41, 44, 47, 50, 53]},
    "16": {"nome": "Noturno", "valores": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 21, 24, 27, 30, 33, 36, 39, 41, 44, 47, 50, 53, 56, 60]},
    "17": {"nome": "Dragão", "valores": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 21, 24, 27, 30, 33, 36, 39, 41, 44, 47, 50, 53, 56, 60]},
    "18": {"nome": "Fada", "valores": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 21, 24, 27, 30, 33, 36, 39, 41, 44, 47, 50, 53, 56, 60]},
}


def calcular_pedras(natureza, boost):
    if natureza in boost_dict and 1 <= boost <= 30:
        return sum(boost_dict[natureza]["valores"][:boost])
    else:
        return "Natureza ou valor de boost inválido."

def exibir_naturezas():
    print("Naturezas disponíveis:")
    for codigo, info in boost_dict.items():
        print(f"[{codigo}] - {info['nome']}")

def main():
    while True:
        exibir_naturezas()
        natureza = input("Escolha a natureza pelo código: ")
        boost = int(input("Escolha o nível de boost (+1 a +30): "))
        
        pedras_necessarias = calcular_pedras(natureza, boost)
        print(f"\nPara um boost de +{boost} na natureza {boost_dict[natureza]['nome']}, você precisará de {pedras_necessarias} pedras.\n")

        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()
