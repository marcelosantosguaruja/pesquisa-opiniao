import os
os.system("cls")

excelente = 0
ruim = 0
bom = 0

for i in range(1, 51):
    print(f"""
     ════════════════════════════════════════════════
     A empresa de Marketing TUDOWEB convida para uma ░
     pesquisa de sobre o seu atendimento.            ░
     Sua opinião é muito importante para nós.        ░
     ══════════════════════════════════════════════1

         """)
    nome = input("Informe o seu nome: ")
    idade = int(input("Qual a sua idade: "))
    opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
        print(f"Obrigado {nome} pela sua opinião registrada como EXCELENTE")

    elif opiniao == 2:
        bom += 1
        print(f"Obrigado {nome} pela sua opinião registrada como BOM")

    elif opiniao == 3:
        ruim += 1
        print(f"Obrigado {nome} pela sua opinião registrada como RUIM")

    else:
        print("Opção Inválida.")

print(f"""
     ══════════════════════════════════════════════════
     O resultado da pesquisa de analise de atendimento ░
     da empresa TUDOWEB foi concluída com sucesso. Sua ░
     participaçao  foi fundamental.   Agradeçemos pela ░
     sua disponibilidade e  participação. Segue abaixo ░
     o resultado final da pesquisa.                    ░
     ══════════════════════════════════════════════════░
     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

     Quantidade de respostas Excelentes: {excelente}   
     Quantidade de respostas Ruins: {ruim}

     O total de pesquisados foram: {excelente + ruim + bom}
     """)