import random

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
    aparece_inimigo = random.randint(0, 2)
    if aparece_inimigo:
        nome_inimigo = random.choice(inimigos[local["inimigos"]])
        print(f"\nApareceu um/uma {nome_inimigo}")
        combate(nome_inimigo)
    else:
        if local["items"]:
            jogador["inventario"].append(local["items"])
            print("\nConseguiste um/uma ", end="")
            print(" e um/uma ".join(local["items"]))
            del local["items"]
        else:
            print("\nNão encontraste nada!!")

def combate(inimigo):
    pass