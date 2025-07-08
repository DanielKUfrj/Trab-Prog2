from time import sleep
from random import choice
from tkinter import *


class Local:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao


class Jogador:
    def __init__(self, nome, localizacao, vidas, dano, inventario=[]):
        self.nome = nome
        self.localizacao = localizacao
        self.vidas = vidas
        self.dano = dano
        self.inventario = inventario


class Personagem:
    """Classe designada aos personagens de batalha"""

    def __init__(self, nome, dano, vidas, nivel):
        """Função construtora da classe. Tem objetivo de criar um novo personagem.

        nome: Nome do personagem
        dano: Dano que o pergonagem causará ao jogador
        vidas: Quantidade de vidas que o personagem possui
        nivel: Nível de dificuldade do personagem 
            (Pode ser: facil, medio, dificil)

        """
        self.nome = nome
        self.dano = dano
        self.vidas = vidas

        # As perguntas estão definidas como atributo privado da classe
        self.perguntas = self.carrega_perguntas(nivel)
        self.ultima_resposta = ""

    def carrega_perguntas(self, nivel):
        """Função para ler o arquivo onde estão contidas as perguntas"""
        perguntas = {
            "facil": [
                {
                    "pergunta": "Qual a definição de classe?",
                    "respostas": {
                        "A": "Objeto que contém a informação sobre um tipo definido pelo programador.",
                        "B": "Tipo definido pelo programador",
                        "C": "Criar um objeto."
                    },
                    "resposta_correta": "B"
                },
                {
                    "pergunta": "Sapato é uma variável de qual tipo?",
                    "respostas": {
                        "A": "String",
                        "B": "Inteiro",
                        "C": "Float"
                    },
                    "resposta_correta": "A"
                },
                {
                    "pergunta": "Variáveis armazenam oque ?",
                    "respostas": {
                        "A": "Dados",
                        "B": "Classes",
                        "C": "Tipos"
                    },
                    "resposta_correta": "A"
                },
                {
                    "pergunta": "Definição de objeto?",
                    "respostas": {
                        "A": "Qualquer entidade que armazena estado e comportamento",
                        "B": "Tipo definido pelo programador",
                        "C": "Criar um objeto"
                    },
                    "resposta_correta": "A"
                },
                {
                    "pergunta": "Qual é a posição do primeiro elemento de uma lista?",
                    "respostas": {
                        "A": "1",
                        "B": "12",
                        "C": "0"
                    },
                    "resposta_correta": "C"
                },
                {
                    "pergunta": "45 é uma variável de qual tipo?",
                    "respostas": {
                        "A": "String",
                        "B": "Inteiro",
                        "C": "Float"
                    },
                    "resposta_correta": "B"
                },
                {
                    "pergunta": "395.66 é uma variavel de qual tipo?",
                    "respostas": {
                        "A": "Inteiro",
                        "B": "String",
                        "C": "Float"
                    },
                    "resposta_correta": "C"
                },
                {
                    "pergunta": "Qual a extensão do arquivo python?",
                    "respostas": {
                        "A": ".py",
                        "B": ".js",
                        "C": ".rb"
                    },
                    "resposta_correta": "A"
                },
                {
                    "pergunta": "Qual palavra-chave é usada para definir uma classe em Python??",
                    "respostas": {
                        "A": "Class",
                        "B": "def",
                        "C": "and"
                    },
                    "resposta_correta": "A"
                }
            ],
            "medio": [
                {
                    "pergunta": "Como você cria um objeto a partir de uma classe chamada Carro?",
                    "respostas": {
                        "A": "obj = Carro()",
                        "B": "obj = new Carro",
                        "C": "obj = criar Carro"
                    },
                    "resposta_correta": "A"
                },
                {
                    "pergunta": "Qual método especial em Python é usado para inicializar um objeto",
                    "respostas": {
                        "A": "create",
                        "B": "init",
                        "C": "start"
                    },
                    "resposta_correta": "B"
                },
                {
                    "pergunta": "O que significa encapsulamento em OOP?",
                    "respostas": {
                        "A": "Esconder os detalhes internos e expor apenas o necessário",
                        "B": "Reutilizar código de outras classes",
                        "C": "Criar múltiplas instâncias de uma classe"
                    },
                    "resposta_correta": "A"
                },
                {
                    "pergunta": "Qual destas é uma vantagem da programação orientada a objetos?",
                    "respostas": {
                        "A": "Código que nunca precisa ser testado",
                        "B": " Reutilização de código através de herança e encapsulamento",
                        "C": "Execução mais rápida que código procedural"
                    },
                    "resposta_correta": "B"
                },
                {
                    "pergunta": "Como você torna um atributo privado em Python?",
                    "respostas": {
                        "A": "Usando a palavra-chave private",
                        "B": "Declarando o atributo fora da classe",
                        "C": "Colocando dois underlines antes do nome do atributo"
                    },
                    "resposta_correta": "C"
                },
                {
                    "pergunta": "O que é polimorfismo em OOP?",
                    "respostas": {
                        "A": "Executar código sem erros",
                        "B": "Criar variáveis globais",
                        "C": "Capacidade de usar métodos com o mesmo nome em diferentes classes"
                    },
                    "resposta_correta": "C"
                },
                {
                    "pergunta": "Qual é o resultado de tentar acessar um atributo privado diretamente fora da classe?",
                    "respostas": {
                        "A": "Erro de atributo",
                        "B": "Retorna o valor do atributo",
                        "C": "Retorna None"
                    },
                    "resposta_correta": "A"
                },
                {
                    "pergunta": "Diagramas de objetos e classes são diagramas de?",
                    "respostas": {
                        "A": "PDF",
                        "B": "UML",
                        "C": "JPG"
                    },
                    "resposta_correta": "B"
                },
                {
                    "pergunta": "Qual a definição de sobrecarga de operador?",
                    "respostas": {
                        "A": "Método que modifica o comportamento do operador para que ele\natue como um tipo definido pelo programador",
                        "B": "Objeto armazenado como um atributo dentro de outro objeto",
                        "C": "Criar um objeto dentro de uma classe"
                    },
                    "resposta_correta": "A"
                }
            ],
            "dificil": [
                {
                    "pergunta": "Nome do autor do livro Pensando em Tkinter?",
                    "respostas": {
                        "A": "Michael James",
                        "B": "Steven Ferg",
                        "C": "Jesse Andersen"
                    },
                    "resposta_correta": "B"
                },
                {
                    "pergunta": "Nome do autor Pense em Python?",
                    "respostas": {
                        "A": "Gary Oldman",
                        "B": "Gustav Fried",
                        "C": "Allen B. Downey"
                    },
                    "resposta_correta": "C"
                },
                {
                    "pergunta": "Nome do conjunto de 5 práticas recomendado para um programa orientado a objetos?",
                    "respostas": {
                        "A": "GOLEM",
                        "B": "SOLID",
                        "C": "SILVER"
                    },
                    "resposta_correta": "B"
                },
                {
                    "pergunta": "Sempre que um programa encontra dificuldades não previstas, ocorre uma?",
                    "respostas": {
                        "A": "Exceção",
                        "B": "Erro",
                        "C": "None"
                    },
                    "resposta_correta": "A"
                },
                {
                    "pergunta": "Descrição da classe IOError?",
                    "respostas": {
                        "A": "Falha no acesso ou atribuição a atributo de classe",
                        "B": "Falha no acesso a arquivo inexistente ou outros de E/S",
                        "C": "Chave inexistente de dicionário"
                    },
                    "resposta_correta": "B"
                },
                {
                    "pergunta": "Descrição da classe TypeError?",
                    "respostas": {
                        "A": "Falha no acesso a arquivo inexistente ou outros de E/S",
                        "B": "Falha no acesso ou atribuição a atributo de classe",
                        "C": "Operador embutido aplicado a objeto de tipo errado"
                    },
                    "resposta_correta": "C"
                },
                {
                    "pergunta": "Descrição da classe Exception?",
                    "respostas": {
                        "A": "Classe base para todas as exceções",
                        "B": "Erro de sintaxe (código errado)",
                        "C": "Índice inexistente de seqüência"
                    },
                    "resposta_correta": "A"
                },
                {
                    "pergunta": "Ano da criação da linguagem Python?",
                    "respostas": {
                        "A": "1989",
                        "B": "1997",
                        "C": "1995"
                    },
                    "resposta_correta": "A"
                },
                {
                    "pergunta": "Ano da criação da primeira linguagem?",
                    "respostas": {
                        "A": "1942",
                        "B": "1978",
                        "C": "1990"
                    },
                    "resposta_correta": "A"
                }
            ]
        }

        return perguntas[nivel]

    def obtem_pergunta(self):
        """Função para obter a pergunta"""
        pergunta = choice(self.perguntas)

        return pergunta

    def define_resposta(self, letra):
        self.ultima_resposta = letra

    def obtem_resposta(self, pergunta, respostas):
        """Cria uma interface para o jogador responder a pergunta."""
        # Limpa o que tem salvo nesta variável
        self.ultima_resposta = ""

        janela = Tk()
        janela.title("Mundo da programação orientada a objetos.")
        janela.geometry("700x200")

        label = Label(janela, text=pergunta)
        label.pack(pady=10)

        # Cria um botão para cada opção e atribui duas funções a cada
        # Definir a resposta (A, B ou C) e fechar a interface
        botao_a = Button(janela, text=respostas["A"], command=lambda: [self.define_resposta("A"), janela.destroy()])

        botao_b = Button(janela, text=respostas["B"], command=lambda: [self.define_resposta("B"), janela.destroy()])

        botao_c = Button(janela, text=respostas["C"], command=lambda: [self.define_resposta("C"), janela.destroy()])

        botao_a.pack()
        botao_b.pack()
        botao_c.pack()

        janela.mainloop()

        return self.ultima_resposta


# Criando todos os locais do jogo
quarto = Local("Quarto", "Você desperta lentamente em uma cama simples. O quarto ao seu redorbestá iluminado apenas pela luz de uma vela acessa sobre a mesa ao lado")
sala = Local("Sala", "Ao atravessar a porta,você encontra um homem idoso sentado em uma cadeira. Ele dorme profundamente, com a cabeça apoiada sobre um livro aberto, em cima de uma mesa de vidro.")
rua = Local("Rua", "Você sai pela porta da frente da casa e se depara com uma rua estreita e suja que está mergulhada em sombras, com paredes desgastadas e grafites descascados que contam histórias de abandono.")
castelo = Local("Castelo", "Você chega na castelo, um castelo sombrio, envolto por névoa espessa. Suas torres altas e irregulares perfuram o céu cinzento, enquanto as pedras gastas e cobertas de musgo parecem absorver toda a luz ao redor.")
# Inicio do jogo
print("Bem vindo ao Mundo da programação orientada a objeto!")
nome = input("Digite o seu nome: ")
# Depois da janela com o título do jogo com a opção jogar e sair,
# criar uma nova janela ou estrutura para o jogador botar o seu nome e
# botar esse input dentro da janela, tambem botar a opção voltar.
jogador = Jogador(nome, quarto, 5, 1)

gua = Personagem("Guarda", 1, 4, "facil")
com = Personagem("Comandandante", 2, 8, "medio")
imp = Personagem("Imperador Sintaxus", 3, 16, "dificil")

print(jogador.localizacao.descricao)
sleep(1)
print("Você consegue ver que em cima do chão há uma vestimenta, um tipo de armadura leve, feita de couro cru.")
sleep(1)

# Primeira ação do jogo: Vestir uma armadura
# Loop infinito para aguardar uma resposta válida e correta
while True:
    print("Deseja vestir a armadura?")
    resposta = input(">S/N ").upper()

    if resposta == "S":
        print("Você vestiu a armadura e se sente ligeiramente mais protegido.")
        jogador.vidas += 1
        break

    elif resposta == "N":
        print("Você não vestiu a armadura.")
        break
    else:
        # Após isso, o jogador voltará para a pergunta
        print("Por favor, escolha uma das alternativas adequadas.")
        sleep(1)
sleep(1)

print(
    "Após isso, você nota uma porta de madeira a sua frente e decide sair do quarto")
sleep(1)
print(f'{jogador.nome} tem {jogador.vidas} vidas.')
sleep(1)

jogador.localizacao = sala
print(jogador.localizacao.descricao)
sleep(1)

# Segunda ação do jogo: Acordar o velho
# Loop infinito para aguardar uma resposta válida e correta
while True:
    print("Deseja acordar o velho?")
    resposta = input(">S/N ").upper()

    if resposta == "S":
        print("Você acorda o acorda de forma cautelosa")
        sleep(1)
        break
    elif resposta == "N":
        print("Você não acordou o velho e decidiu esperar 5 minutos...")
        sleep(1)
        print("Após 5 minutos, o velho continua a dormir....")
        sleep(1)
        print("Você o acorda de forma cautelosa")
        sleep(1)
        break
    else:
        print("Por favor, escolha uma das alternativas adequadas.")
        sleep(1)

print("O velho acorda lentamente")
sleep(1)
print("???: Oh! você finalmente acordou!")
sleep(1)
print("Afonso: Me chamo Afonso e te resgatei quando você estava desacordado na floresta")
sleep(1)
print("Afonso: O meu povo estava ansioso pela sua volta, você deve ser o guerreiro lendário de nossa lenda!")
sleep(1)
print("O velho explica para você que nesse mundo, a humanidade vive uma cruel escravidão sob o comando do maligno imperador SINTAXUS, que atráves de seu conhecimento sobre uma desconhecida e antiga magia, chamada programação orientada a objeto, reinava sobre o imperio todo")
sleep(1)
print("E que após 2025 anos de escravidão, apareceria um salvador conhecedor dessa magia e capaz de lutar contra Sintaxus e reestaurar a paz e harmonia no império.")
sleep(1)
print("Além disso, ele explica que ele é o ultimo membro de uma antiga e nobre família desse império e que foi profetizado que o descendente de sua familia, do ano da volta do héroi, iria-o resgatar numa floresta desacordado")
sleep(1)
print("Afonso: Por favor, me diga seu nome.")
sleep(1)
print("Você se apresenta a ele.")
sleep(1)
print(f"Muito prazer, {jogador.nome}!")
sleep(1)
print(f"Afonso: Agora por favor, {jogador.nome}! Me prove que você é o heroi e me responda essa pergunta que re-contada aos representantes da minha familia a milênios até esse importante momento")
sleep(1)

# Primeira pergunta do jogo
# Loop infinito para aguardar a resposta correta
# Cria uma interface com 3 botões para escolher a resposta
pergunta = {
    "pergunta": "Qual a definição de classe?",

    "respostas": {
        "A": "Objeto que contém a informação sobre um tipo definido pelo programador.",
        "B": "Tipo definido pelo programador",
        "C": "Criar um objeto."
    },

    "resposta_correta": "B"
}
while True:
    # vai ser uma pergunta ja definida, 3 alternativas uma correta, se o personagem erra,fecha a tela, da print do afonso:Se concentre por favor,abre a janela,,repetir isso ate resposta certa
    resposta = gua.obtem_resposta(pergunta["pergunta"], pergunta["respostas"])

    if resposta == pergunta["resposta_correta"]:
        break
    elif resposta == "":
        exit()
    else:
        print("Afonso: Se concentre por favor...")
        sleep(1)
        print("Afonso: Irei repetir a pergunta!")
        sleep(1)


sleep(1)

print()
print("Afonso: Você realmente é o heroi lendário!")
sleep(1)
print("Afonso puxa um baú de madeira debaixo da mesa, coloca-o cuidadosamente sobre o tampo e abre a tampa, revelando seu conteúdo")
sleep(1)
print("Assim que Afonso ergue a tampa do baú, seus olhos se deparam com um conjunto impressionante: uma espada forjada em aço damasco e um escudo robusto de bronze polido.")
sleep(1)
print("Ambos os itens possuem uma cobra verde esmeralda incrustada. Você fica curioso e pergunta a ele o motivo do símbolo em ambos os equipamentos.")
sleep(1)
print("Afonso:Esse símbolo representa o brasão da minha familia, da família Python")
sleep(1)

# Segunda pergunta do jogo
while True:
    print("Digite E para pegar a  espada e S para pegar escudo")

    equip = input("E/S:").upper()
    if equip == "E":
        jogador.dano += 1
        print("Afonso:Bela escolha! Essa espada carregada com a magia derivada do conhecimento antigo será de bela ajuda!")
        sleep(1)
        print("Você se sente consideravelmente mais forte agora")
        sleep(1)
        break
    elif equip == "S":
        jogador.vidas += 1
        print("Afonso:Bela escolha! Esse escudo carregado com a magia derivada do conhecimento antigo será de bela ajuda!")
        sleep(1)
        print("Você se sente consideralvemente mais protegido agora")
        sleep(1)
        break

    else:
        print("Por favor, escolha uma das alternativas adequadas.")
    sleep(1)

print("Assim que Afonso termina de falar, você começa a ouvir gritos vindo de fora da casa. O barulho é alto, cheio de medo")
sleep(1)
print("Afonso:Devem ser os guardas de Sintaxus...")
sleep(1)
print("Afonso:A cada dia que passa, Sintaxus e o Império impõem leis e comportamentos cada vez mais tirânicos, apertando o cerco sobre a população.")
sleep(1)
print("Afonso:As regras se tornam mais rígidas, os castigos mais severos, e o poder é exercido de forma autoritária, sem espaço para questionamentos ou resistência.")
sleep(1)
print("Você sente uma indignação muito grande, uma mistura de raiva e determinação que não pode ser ignorada. Sem hesitar, você decide agir")
sleep(1)

jogador.localizacao = rua
print(jogador.localizacao.descricao)
sleep(1)

print("Em meio a esse cenário miserável, um guarda imperial, com o rosto endurecido , avança com agressividade contra um cidadão indefeso. O homem tenta recuar, mas não há escapatória.")
sleep(1)
print("Você decide então avançar")
sleep(1)
print(f"{jogador.nome}: Pare com isso agora!")
sleep(1)
print("Guarda:Me detenha então!")
sleep(1)

while gua.vidas > 0 and jogador.vidas > 0:
    print()
    print(f'{jogador.nome} tem {jogador.vidas} vidas e dá {jogador.dano} de dano')
    sleep(1)
    print(f'{gua.nome} tem {gua.vidas} vidas e dá {gua.dano} de dano')
    sleep(1)

    pergunta = gua.obtem_pergunta()
    resposta = gua.obtem_resposta(pergunta["pergunta"], pergunta["respostas"])

    if resposta == pergunta["resposta_correta"]:
        gua.vidas -= jogador.dano
        print(f'O guarda agora possui {gua.vidas} de vida')
        sleep(1)

    elif resposta == "":
        exit()
    else:
        jogador.vidas -= gua.dano
        print(f'O herói agora possui {jogador.vidas} de vida')
        sleep(1)

if jogador.vidas <= 0:
    print("Fim de jogo")
    exit()
elif gua.vidas <= 0:
    print("Você derrotou o guarda")
    sleep(1)


print("Você percebe que o guarda ficou desacordado")
sleep(1)
print("Você ajuda o cidadão a levantar")
sleep(1)
print("Cidadão:Muito obrigado")
sleep(1)
print("O cidadão então recolhe sua bolsa que estava no chão e abre a bolsa")
sleep(1)
print("Cidadão:Como sinal de agradecimento,escolha uma dessas poções,irá te ajudar")
sleep(1)
print("Você olha a bolsa e se depara com 2 poções: Uma vermelha e a outra azul")
sleep(1)
print("Cidadão:A poção vermelha te dará mais coragem e força")
sleep(1)
print("Cidadão:Já a poção azul te dará mais resistência")
sleep(1)

while True:
    print("Escolha uma poção:")
    sleep(1)
    print("V para vermelho e A para azul")
    sleep(1)
    pocao = input("V/A:").upper()
    if pocao == "V":
        jogador.inventario.append("Poção de dano")
        print("Você guardou a poção no seu inventário")
        break
    elif pocao == "A":
        jogador.inventario.append("Poção de resistência")
        print("Você guardou a poção no seu inventário")
        break
    else:
        print("Por favor, escolha uma das alternativas adequadas.")
        sleep(1)
sleep(1)

print("Após pegar a poção, você percebe que o castelo do imperador está proximo")
sleep(1)
print("Você decide seguir para o castelo")
sleep(1)
jogador.localizacao = castelo
print(jogador.localizacao.descricao)
sleep(1)
print("Você percebe que o portão do castelo está aberto")
sleep(1)
print("Você entra no castelo")
sleep(1)
print("???:Estava te esperando,herói lendario!")
sleep(1)
print("Comandante:Eu sou o comandante deste castelo e não deixarei você chegar na sala do imperador!")
sleep(1)
# Sempre que começar uma nova batalha após o personagem ter ganho a poção, aparecerá a opção de usar a poção caso ele ainda n tenha usado
print("Você deseja usar a poção guardada?")
sleep(1)
while True:
    usar_pocao = input("S/N:").upper()
    if usar_pocao == "S":
        if jogador.inventario[0] == "Poção de dano":
            jogador.dano += 1
            print("Você tomou a poção de dano e se sente mais forte")
        else:
            jogador.vidas += 1
            print("Você tomou a poção de resistência e se sente mais resistente")
        sleep(1)
        break
    elif usar_pocao == "N":
        print("Você não usou a poção")
        sleep(1)
        break
    else:
        print("Por favor, escolha uma das alternativas adequadas.")
    sleep(1)


while com.vidas > 0 and jogador.vidas > 0:
    print()
    print(f'{jogador.nome} tem {jogador.vidas} vidas e dá {jogador.dano} de dano')
    sleep(1)
    print(f'{com.nome} tem {com.vidas} vidas e dá {com.dano} de dano')
    sleep(1)

    pergunta = com.obtem_pergunta()
    resposta = com.obtem_resposta(pergunta["pergunta"], pergunta["respostas"])

    if resposta == pergunta["resposta_correta"]:
        com.vidas -= jogador.dano
        print(f'O comandante agora possui {com.vidas} de vida')
        sleep(1)

    elif resposta == "":
        exit()
    else:
        jogador.vidas -= com.dano
        print(f'O herói agora possui {jogador.vidas} de vida')
        sleep(1)

if jogador.vidas <= 0:
    print("Fim de jogo")
    exit()
elif com.vidas <= 0:
    print("Você derrotou o comandante")
    sleep(1)

sleep(1)
print("No momento em que comandante cai, você percebe um baú atras dele")
sleep(1)
print("Você decide abrir o bau")
sleep(1)
print("Você se depara com um Machado de bronze e um clava de aço")
sleep(1)
while True:
    print("Digite M para machado e C para clava")

    equip = input("Escolha um equipamento:").upper().strip()
    if equip == "M":
        jogador.inventario.append("Machado")
        print("Você guardou o machado no seu inventário")
        break
    elif equip == "C":
        jogador.inventario.append("Clava")
        print("Você guardou a clava no seu inventário")
        break
    else:
        print("Por favor, escolha uma das alternativas adequadas.")
sleep(1)
print("No momento em que você guarda o novo equipamento no inventário, você se depara com uma sala fechada")
sleep(1)
print("Você entra na sala do castelo")
sleep(1)
print("Quando você entra na sala, você encontra o imperador sentado em seu trono")
sleep(1)
print("Sintaxus:Finalmente herói lendário! Chegou a hora da batalha final!")
sleep(1)
if len(jogador.inventario) == 2:
    print("Você percebe que irá precisar de todo poder e resistência possivel")
    sleep(1)
    if jogador.inventario[0] == "Poção de dano":
        jogador.dano += 1
        print("Você tomou a poção de dano e se sente mais forte")
        sleep(1)
    else:
        jogador.vidas += 1
        print("Você tomou a poção de resistência e se sente mais resistente")
        sleep(1)
    jogador.inventario.pop(0)
print(f"Você tem {jogador.inventario[0]} no seu inventário ")
sleep(1)
while True:
    print("Deseja equipar?")
    sleep(1)
    usar_equip = input("S/N:").upper()
    if usar_equip == "S":
        print("Você equipou o novo equipamento")
        sleep(1)
        jogador.dano += 1
        break

    elif usar_equip == "N":
        print("Você não equipou")
        sleep(1)
        break
    else:
        print("Por favor, escolha uma das alternativas adequadas.")
        sleep(1)

while imp.vidas > 0 and jogador.vidas > 0:
    print()
    print(f'{jogador.nome} tem {jogador.vidas} vidas e dá {jogador.dano} de dano')
    sleep(1)
    print(f'{imp.nome} tem {imp.vidas} vidas e dá {imp.dano} de dano')
    sleep(1)

    pergunta = imp.obtem_pergunta()

    resposta = imp.obtem_resposta(pergunta["pergunta"], pergunta["respostas"])

    if resposta == pergunta["resposta_correta"]:
        imp.vidas -= jogador.dano
        print(f'O Imperador agora possui {imp.vidas} de vida')
        sleep(1)

    elif resposta == "":
        exit()
    else:
        jogador.vidas -= imp.dano
        print(f'O herói agora possui {jogador.vidas} de vida')
        sleep(1)

if jogador.vidas <= 0:
    print("Fim de jogo")
    exit()
elif imp.vidas <= 0:
    print("Você derrotou o imperador")
    sleep(1)
    print('Parabéns! Você zerou o jogo.')
    exit()
