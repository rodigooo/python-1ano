import math
import random
from operator import xor


def criar_jogador(nome):
    return {
        "nome": nome,
        "hp": 100,
        "ataque": 20,
        "defesa": 10,
        "ouro": 20,
        "nivel": 1,
        "inventario": ["pocao", "anel"],
        "local": "casa",
    }

def criar_inimigo(nome, hp, ataque, xp_recompensa, gold_recompensa):
    return {
        "nome": nome,
        "hp": hp,
        "ataque": ataque,
        "xp_recompensa": xp_recompensa,
        "gold_recompensa": gold_recompensa,
    }

inimigos = {
    "sapo": criar_inimigo("Sapo", 30, 10, 55, 25),
    "bruxa": criar_inimigo("Bruxa", 20, 50, 70, 200),
    "esqueleto": criar_inimigo("Esqueleto", 100, 20, 100, 250),
}

locais = {
    "casa": {
        "nome": "Casa do herói",
        "descricao": "A tua casa!",
        "saidas": {"sul": "floresta"},
        "inimigos": [],
        "itens": ["espada de madeira"],
    },
    "floresta": {
        "nome": "Floresta",
        "descricao": "Floresta sombria",
        "saidas" : {
            "norte": "casa",
            "este": "cidade",
            "oeste": "mercado",
        },
        "inimigos":[
            inimigos["bruxa"],
            inimigos["esqueleto"],
        ],
        "itens": ["galho", "pó mágico"],
    },
    "cidade": {
        "nome": "Cidade",
        "descricao": "Grande cidade, aqui não entram inimigos!",
        "saidas": {
            "oeste": "floresta",
        },
        "inimigos": [],
        "itens": [
            "moeda de ouro",
            "metade de uma espada",
        ],
    },
    "mercado": {
        "nome": "Mercado",
        "descricao": "Mercado dos duendes! Vende e compra as tuas coisas aqui!",
        "saidas": {
            "este": "floresta",
        },
        "inimigos": ["sapo"],
        "itens": ["escudo partido"],
    }
}

def explorar(jogador):
    local = locais[jogador["local"]]
    print(f"\nDecidiste explorar o/a {local}")
    match random.randint(1, 3):
        case 1:
            nome_inimigo = random.choice(inimigos[local["inimigos"]])
            print(f"\nApareceu um/uma {nome_inimigo}")
            combate(inimigos[nome_inimigo], jogador)
        case 2:
            if local["items"]:
                jogador["inventario"].append(local["items"])
                print("\nConseguiste um/uma ", end="")
                print(" e um/uma ".join(local["items"]))
                del local["items"]
        case 3:
            print("\nNão encontraste nada!!")

def combate(inimigo, jogador):
    print("Apareceu um inimigo!!")
    inimigo_hp = inimigo["hp"]
    while True:
        if inimigo_hp == 0:
            ## codigo de conseguir recompensa aqui
            return
        print(f"A lutar com: {inimigo['nome']}")
        print("Opções: ")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Fugir")
        dano_ao_inimigo = random.randint(
            math.floor(jogador["ataque"] / 2),
            jogador["ataque"] * 2
        )
        dano_ao_jogador = random.randint(
            math.floor((inimigo["ataque"] - jogador["defesa"]) / 2),
            (inimigo["ataque"] - jogador["defesa"]) * 2
        )
        match input("Escolhe uma das opções: "):
            case "1":
                inimigo_hp -= dano_ao_inimigo
                inimigo_hp = max(0, inimigo_hp)
                if inimigo_hp == 0:
                    continue
                jogador["hp"] -= dano_ao_jogador
                jogador["hp"] = max(0, jogador["hp"])
                if jogador["hp"] == 0:
                    perder()
                print(f"{inimigo['nome']} sofreu {dano_ao_inimigo} dano!\n")
            case "2":
                dano_ao_jogador //= random.randint(1, 5)
                jogador["hp"] -= dano_ao_jogador
                jogador["hp"] = max(0, jogador["hp"])
                if jogador["hp"] == 0:
                    perder()
            case "3":
                match random.randint(1, 2):
                    case 1:
                        print("Conseguiste fugir!")
                        return
                    case 2:
                        print("Não conseguiste fugir")
                        jogador["hp"] -= dano_ao_jogador
                        jogador["hp"] = max(0, inimigo_hp)
                        if jogador["hp"] == 0:
                            continue
        print(f"Sofreste {dano_ao_jogador} dano!")


def perder():
    quit()