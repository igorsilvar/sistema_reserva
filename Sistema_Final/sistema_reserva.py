import os

#Criando menu para reservar voo
def menu():
    print("====== SISTEMA DE RESERVA DE VOOS ======")
    print(" 1 . CADASTRAR VOO ")
    print(" 2 . PESQUISAR VOOS DISPONIVEIS ")
    print(" 3 . RESERVAR VOO ")
    print(" 0 . Sair ")
    
#Pegando Origem
def pede_origem():
    return str(input("Digite a origem : ")) 

#Pegando Destino
def pede_destino():
     return str(input("Informe o destino do voo : "))
 
#Pegando Numero do voo
def pega_numero_voo():   
    return int(input("Informe o numero do voo : "))

#Pegando Horario de saída do voo
def pega_horario_saida_voo():
    return str(input("Informe o horario de saída do voo : "))

#Pegando Horario de chegada Do Voo
def pega_horario_chegada_voo():
    return str(input("Informe o horário de chegada do voo : "))

#Pegando a data do Voo
def pega_data_voo():
    return str(input("Informe a data do voo : "))

#Pegando o nome da pessoa
def pega_nome_pessoa():
    return str(input("Digite o nome completo : "))

#Pegando o numero do passaporte
def pega_numero_passaporte():
    return str(input("Digite o numero do seu passaporte ou documento de indentificação : "))

#Pegando numero da poltrona
def pega_numero_poltrona():
    return str(input("Informe o número da poltrona : "))

#criando uma lista vazia para armazenar os dados do voo
dados_voo = []
#Criando a função para salvar voos em arquivos txt
def gravar_voo(voo):
    nome_arquivo = 'voos.txt'
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for voo in dados_voo:
        arquivo.write("%s#%s#%s#%s#%s#%s \n" %(voo[0], voo[1], voo[2], voo[3], voo[4], voo[5]))
    arquivo.close()

#Criando função para salvar os dados da reserva
def gravar_reserva(reserva):
    nome_arquivo = 'reserva.txt'
    arquivo_reserva = open(nome_arquivo,"w",encoding="utf-8")
    for reserva in reserva:
        arquivo_reserva.write("%s#%s#%s \n" %(reserva[0],reserva[1],reserva[2]))
    arquivo_reserva.close()
     
#Criando a função pesquisar voo   
def pesquisar_voos():
    qual_origem = pede_origem()
    qual_destino = pede_destino()
    nome_arquivo = 'voos.txt'
    
    #abrindo o e percorrendo o arquivo para fazer a busca 
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    for dado in arquivo.readlines():
        if qual_origem and qual_destino:
            origem, destino, numero_voo, horario_saida_voo, horario_chegada_voo, data_voo = dado.strip().split("#")
            if qual_origem == origem and qual_destino == destino:
                print(
                    f'Origem: {origem},Destino : {destino}, Numero do voo : {numero_voo}, Horário de saída do voo : {horario_saida_voo}, Horário de chegada do voo : {horario_chegada_voo}, Data do voo : {data_voo}'
                )
        elif qual_origem and not qual_destino:
            if qual_origem == origem:
                print(
                    f'Origem: {origem}, Destino : {destino}, Numero do voo : {numero_voo}, Horário de saída do voo : {horario_saida_voo}, Horário de chegada do voo : {horario_chegada_voo}, Data do voo : {data_voo}'
                )
        elif qual_destino and not qual_origem:
            if qual_destino == destino:
                print(
                    f'Origem: {origem}, Destino : {destino}, Numero do voo : {numero_voo}, Horário de saída : {horario_saida_voo}, Horário de chegada: {horario_chegada_voo}, Data : {data_voo}'
                )
                
    arquivo.close()

#Criando a função Cadastro de Voo
def cadastrar_voos():
    data_voo = pega_data_voo()
    origem = pede_origem()
    destino = pede_destino()
    numero_voo = pega_numero_voo()
    horario_saida_voo = pega_horario_saida_voo()
    horario_chegada_voo = pega_horario_chegada_voo()
    dados_voo.append([origem,destino,numero_voo,horario_saida_voo,horario_chegada_voo,data_voo])
    gravar_voo(dados_voo)
        
#Criando a função de reserva de voos
dados_reserva = []
def reservar_voo():
    nome_pessoa = pega_nome_pessoa()
    passaporte = pega_numero_passaporte()
    numero_poltrona = pega_numero_poltrona()
    
    if not os.path.exists("reserva.txt"):
        a = open('reserva.txt', "w", encoding="utf-8")
    
    arquivo = open('reserva.txt', "r", encoding="utf-8")
    existe = False
    
    for dado in arquivo.readlines():
        _nome_pessoa, _passaporte, _numero_poltrona = dado.strip().split("#")
        if numero_poltrona == _numero_poltrona:
            existe = True
                 
    if existe:
        print('Já existe uma reserva pra a poltrona selecionada.')
    else:
        dados_reserva.append([nome_pessoa,passaporte,numero_poltrona])
        gravar_reserva(dados_reserva)
        
while True:   
    menu()
    opcao = int(input("Digite a opção desejada : "))
    if opcao == 0:
        break
    if opcao == 1:
        cadastrar_voos()
    if opcao == 2:
        pesquisar_voos()
    if opcao == 3:
        reservar_voo()