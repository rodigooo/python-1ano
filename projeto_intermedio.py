import math
import random
import time
import json
from datetime import datetime

def criar_jogador(nome: str):
    return {
        "nome": nome,
        "max_hp": 100,
        "hp": 100,
        "ataque": 20,
        "defesa": 10,
        "ouro": 20,
        "nivel": 1,
        "exp": 0,
        "exp_para_proximo_nivel": 100,
        "inventario": ["frasco de pocao", "anel"],
        "local": "casa",
        "ultima_vez_jogado": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

def criar_inimigo(nome: str, hp: int, ataque: int, xp_recompensa: int, gold_recompensa: int):
    return {
        "nome": nome,
        "hp": hp,
        "ataque": ataque,
        "xp_recompensa": xp_recompensa,
        "gold_recompensa": gold_recompensa,
    }

inimigos = {
    "sapo": criar_inimigo("sapo", 30, 10, 55, 25),
    "bruxa": criar_inimigo("bruxa", 20, 50, 70, 200),
    "esqueleto": criar_inimigo("esqueleto", 100, 20, 100, 250),
}

locais = {
    "casa": {
        "nome": "casa do herói",
        "descricao": "A tua casa!",
        "saidas": {"sul": "floresta"},
        "inimigos": [],
        "itens": ["espada de madeira"],
    },
    "floresta": {
        "nome": "floresta",
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
        "nome": "cidade",
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
        "nome": "mercado",
        "descricao": "Mercado dos duendes! Vende e compra as tuas coisas aqui!",
        "saidas": {
            "este": "floresta",
        },
        "inimigos": [inimigos["sapo"]],
        "itens": ["escudo partido"],
    }
}

itens_a_venda = {
    "espada": {
        "preço": 50,
        "efeito": [10 , "ataque"],
    },
    "feitiço de proteção": {
        "preço": 25,
        "efeito": [20, "defesa"],
    },
    "poção mágica": {
        "preço": 35,
        "efeito": [100 , "hp"]
    }
}

save_path = "savegame.json"

def explorar(jogador):
    local = locais[jogador["local"]]
    print(f"\nDecidiste explorar o/a {local['nome']}, {local['descricao']}.")
    time.sleep(1)
    match random.randint(1, 3):
        case 1:
            if not local["inimigos"]:
                print("\nNão encontraste nada!!")
                return
            nome_inimigo = random.choice(local["inimigos"]).get("nome")
            print(f"\nApareceu um/uma {nome_inimigo}")
            combate(inimigos[nome_inimigo], jogador)
        case 2:
            if local["itens"]:
                item_encontrado = random.choice(local["itens"])
                jogador["inventario"].append(item_encontrado)
                print(f"\nEncontraste um/uma {item_encontrado}!")
                local["itens"].remove(item_encontrado)
            else:
                print("\nNão encontraste nada!!")
        case 3:
            print("\nNão encontraste nada!!")

def combate(inimigo, jogador):
    inimigo_hp = inimigo["hp"]
    while True:
        if inimigo_hp == 0:
            jogador["ouro"] += inimigo["gold_recompensa"]
            jogador["exp"] += inimigo["xp_recompensa"]
            while jogador["exp"] >= jogador["exp_para_proximo_nivel"]:
                jogador["nivel"] += 1
                jogador["exp"] -= jogador["exp_para_proximo_nivel"]
                jogador["exp_para_proximo_nivel"] = math.floor(jogador["exp_para_proximo_nivel"] * 1.5)
                print(f"Subiste de nível! Agora és nível {jogador['nivel']}!")
                jogador["max_hp"] += 20
                jogador["ataque"] += 5
                jogador["defesa"] += 5
            print(f"Derrotaste o/a {inimigo['nome']}! Recebeste {inimigo['gold_recompensa']} ouro e {inimigo['xp_recompensa']} de experiência!")
            return
        print("==============================================================")
        print(f"A lutar com: {inimigo['nome']}, HP: {inimigo_hp}")
        print(f"Teu HP: {jogador['hp']}")
        print("==============================================================")
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
                print(f"{inimigo['nome']} sofreu {dano_ao_inimigo} dano!")
                time.sleep(0.5)
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
                        jogador["hp"] = max(0, jogador["hp"])
                        if jogador["hp"] == 0:
                            perder()
        print(f"Sofreste {dano_ao_jogador} dano!")
        time.sleep(0.5)

def loja(itens, jogador):
    print("Bem-vindo à loja.")
    print("Itens disponíveis para compra:")
    for item, info in itens.items():
        print(f"\t{item}: {info['preço']} ouro")
    print("Escolhe um item para comprar, digita 'vender' para vender itens ou digita 'sair' para sair da loja.")
    match input("Escolha: "):
        case "sair":
            print("Saíste da loja.")
            return
        case "vender":
            qtd = len(jogador["inventario"])
            for item in jogador["inventario"][::]:
                jogador["inventario"].remove(item)
                jogador["ouro"] += 10
            print(f"Vendeste {qtd} itens e ganhaste {qtd * 10} ouro.")
            del qtd
        case item if item in itens:
            if jogador["ouro"] >= itens[item]["preço"]:
                jogador["ouro"] -= itens[item]["preço"]
                if itens[item]["efeito"][1] == "hp":
                    jogador["hp"] += min(itens[item]["efeito"][0], jogador["max_hp"] - jogador["hp"])
                else:
                    jogador[itens[item]["efeito"][1]] += jogador[itens[item]["efeito"][0]]
                print(f"Compraste {item}! Ganhaste +{itens[item]['efeito'][0]} de {itens[item]['efeito'][1]}.")
            else:
                print("Não tens ouro suficiente para comprar este item.")
        case _:
            print("Opção inválida.")
            
def guardar_jogo(caminho, jogador):
    jogador["ultima_vez_jogado"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(caminho, "w") as f:
            json.dump(jogador, f)
        print("\nJogo guardado com sucesso!")
    except Exception as e:
        print(f"Erro ao guardar o jogo: {e}")

def carregar_jogo(caminho):
    try:
        with open(caminho, "r") as f:
            jogador = json.load(f)
        print(f"Bem-vindo de volta, {jogador['nome']}!")
        print("Queres continuar de onde paraste ou começar um novo jogo?")
        print("1 - Continuar")
        print("2 - Novo jogo")
        match input("Escolhe uma das opções: "):
            case "1":
                print("Continuando o jogo...")
                print(f"Última vez jogado: {jogador.get('ultima_vez_jogado', 'Desconhecido')}")
            case "2":
                nome = input("Qual é o teu nome? ")
                jogador = criar_jogador(nome)
            case _:
                print("Opção inválida. Continuando o jogo...")
                print(f"Última vez jogado: {jogador.get('ultima_vez_jogado', 'Desconhecido')}")
        print("Jogo carregado com sucesso!")
    except Exception:
        nome = input("Qual é o teu nome? ")
        jogador = criar_jogador(nome)
    return jogador
    
def jogo():
    global jogador
    print("Bem-vindo ao jogo!")
    time.sleep(1)
    while True:
        print("==============================================================")
        print(f"{jogador['nome']}, HP: {jogador['hp']}, Ouro: {jogador['ouro']}, Nível: {jogador['nivel']}, EXP: {jogador['exp']}, EXP para próximo nível: {jogador['exp_para_proximo_nivel']}")
        print(f"Inventário: {', '.join(jogador['inventario'])}")
        print(f"Local: {jogador['local']}")
        print("==============================================================")
        print("Opções: ")
        print("\t1 - Explorar")
        print("\t2 - Guardar jogo")
        print("\t3 - Sair do jogo (não guardará o progresso)")
        print("\t4 - Ir para outro local")
        if jogador["local"] == "mercado":
            print("\t5 - Entrar na loja")
        match input("Escolhe uma das opções: "):
            case "1":
                explorar(jogador)
            case "2":
                guardar_jogo(save_path, jogador)
            case "3":
                sair()
            case "4":
                saidas_disponiveis = locais[jogador["local"]]["saidas"]
                print("Locais disponíveis para ir: ")
                for direcao, local in saidas_disponiveis.items():
                    print(f"\t{direcao} - {local}")
                direcao_desejada = input("Para onde queres ir?: ")
                if direcao_desejada in locais[jogador["local"]]["saidas"].keys():
                    jogador["local"] = locais[jogador["local"]]["saidas"][direcao_desejada]
                    print(f"Foste para {direcao_desejada}.")
                else:
                    print("Não podes ir para esse local a partir daqui.")
            case "5" if jogador["local"] == "mercado":
                loja(itens_a_venda, jogador)
            case _:
                print("Opção inválida.")

jogador = carregar_jogo(save_path)
    
def perder():
    print("Perdeste!!")
    quit()
    
def sair():
    print("Saíste do jogo.")
    quit()
    
if __name__ == "__main__":
    try:
        jogo()
    except KeyboardInterrupt:
        guardar_jogo(save_path, jogador)
        sair()