import os
from datetime import datetime, timedelta

class clientes():
    
    def __init__(self, nome='', cpf=''):
    
        self.nome = nome
        self.cpf = cpf
    
    def cadastrar_cliente(self):
        self.nome = input("Nome: ")
        
        while True:
            cpf = input("CPF: ")
            if len(cpf) != 11 or not cpf.isdigit():
                print("CPF inválido! Deve conter 11 dígitos numéricos.")
            else:
                break
            
        if cpf in [c.cpf for c in l_clientes]:
            print("CPF já cadastrado! Por favor, utilize outro CPF.")
            return
        else:
            self.cpf = cpf
    
        print("\nCliente cadastrado com sucesso! \n")    
        
    

class veiculos():
        
    def __init__(self, modelo='', placa='', ano='', valor=0.0):
        
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.valor = valor
        self.disponivel = True
        self.manutencao = []
        
    def cadastrar_veiculo(self):
        
        self.modelo = input("Modelo: ").title()
        
        while True:
            placa = input("Placa: ").upper()
            
            if len(placa) == 7:            
                if placa in [p.placa for p in l_veiculos]:
                    print("Carro já cadastrado! Por favor, utilize outra placa.")
                else:
                    self.placa = placa
                    break
            else:
                print("Placa inválida! Deve conter 7 digitos alfanuméricos")
        
        while True:
            ano = input("Ano: ")
            
            if len(ano) == 4:
                self.ano = ano
                break
            else:
                print("Ano inválido! Deve conter 4 dígitos numéricos.")
                
        while True:
            try:
                valor = float(input("Valor por dia: "))
                if valor > 0:
                    self.valor = valor
                    break  
                else:
                    print("O valor deve ser maior que zero.")
            except ValueError:
                print("Valor inválido!")

        self.disponivel = True
        
        print("Veiculo cadastrado com sucesso! \n")
    
    @staticmethod
    def listar_veiculos(lista):
        print("======== Veículos disponíveis ========\n")
        for i, n in enumerate(lista):
            if n.disponivel:
                print(f"{i + 1} - Modelo: {n.modelo} | Ano: {n.ano} | R${n.valor}/dia")
                
    def registrar_manutencao(self):
        desc = input(f"Descreva a manutenção do veículo {self.modelo} ({self.placa}): ").strip()
        while True:
            data = input("Data da manutenção (dd/mm/aaaa): ").strip()
            try:
                data_obj = datetime.strptime(data, "%d/%m/%Y")
                data_f = data_obj.strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Data inválida! Use o formato correto dd/mm/aaaa.")
        
        while True:
            custo_str = input("Custo da manutenção (R$): ").strip().replace(',', '.')
            try:
                custo = float(custo_str)
                if custo >= 0:
                    break
                else:
                    print("O custo deve ser zero ou um valor positivo.")
            except ValueError:
                print("Valor inválido! Digite um número válido para o custo.")

        manutencao = {
            'descricao': desc,
            'data': data_f,
            'custo': custo
        }

        self.manutencao.append(manutencao)
        print("Manutenção registrada com sucesso!\n")

        
    def listar_manutencoes(self):
        if not self.manutencao:
            print(f"O veículo {self.modelo} ({self.placa}) não possui manutenções registradas.\n")
            return

        print(f"Manutenções do veículo {self.modelo} ({self.placa})")
        for i, m in enumerate(self.manutencao, 1):
            print(f"{i}. Data: {m['data']} | Descrição: {m['descricao']} | Custo: R${m['custo']}")
        print()
    
        

class reserva():
    
    def __init__(self):
        self.cpf = ''
        self.placa = ''
        self.modelo = ''
        self.dias = 0
        self.total = 0.0
        self.incidentes = []
        self.pago = False
     
    @staticmethod    
    def buscar_reserva_por_cpf():
        cpf = input("Digite o CPF da reserva: ").strip()
        reservas_cliente = [r for r in l_reservas if r.cpf == cpf]

        if not reservas_cliente:
            print("Nenhuma reserva encontrada.\n")
            return None

        print(f"\nReservas encontradas para CPF {cpf}:\n")
        for i, r in enumerate(reservas_cliente, 1):
            status_pagamento = "Pago" if r.pago else "Pendente"
            print(f"{i} - Modelo: {r.modelo} | Placa: {r.placa} | {r.dias} dias | Total: R${r.total:.2f} | Pagamento: {status_pagamento}")

        while True:
            try:
                escolha = int(input("\nSelecione o número da reserva desejada: "))
                if 1 <= escolha <= len(reservas_cliente):
                    return reservas_cliente[escolha - 1]
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite o número da reserva.")


    def fazer_reserva(self, clientes, reservas, lista_veiculos):
        
        cpf = input("Digite seu CPF: ").strip()
        print("\n Verificando...")
        
        cliente = None
        
        for n in clientes:
            if n.cpf == cpf:
                cliente = n
                break
                
        if not cliente:
            print("Cliente não cadastrado! \n Efetue o cadastro em nosso sistema para aproveitar as ofertas!")        
            return   
            
        ver_veiculos = [n for n in lista_veiculos if n.disponivel]   
        if not ver_veiculos:
            print("Sem veículos disponíveis no momento")
            return
        

        veiculos.listar_veiculos(ver_veiculos)
        
        try:
            escolha = int(input("Escolha o número do seu veículo: ")) -1
            v_escolhido = ver_veiculos[escolha]
        except (ValueError, IndexError):
            print("Escolha inválida.\n")
            return

        try:
            day = int(input("Quantidade de dias que deseja alugar: \n\n"))
            os.system('cls')    
            if day <= 0:
                print("Quantidade inválida! \n")
                return     
            
        except ValueError:
            print("Entrada inválida! \n")
            return
                
        total = day * v_escolhido.valor
        
        self.cpf = cpf
        self.placa = v_escolhido.placa
        self.modelo = v_escolhido.modelo
        self.dias = day
        self.total = total
                
        
        reservas.append(self)
        
        v_escolhido.disponivel = False
            
            
        print(f"Reserva efetuada com sucesso por {cliente.nome} \n")
        print(f"Veiculo: {self.modelo} | Total: R${self.total:.2f}\n")
    
    def efetuar_pagamento(self):
        if self.pago:
            print("Não há nenhum valor pendente para pagamento.\n")
            return
        
        print(f"Sua reserva deu um total de R$ {self.total}\n\n")
        print("O pagamento será à vista (1) ou parcelado (2)? ")
        while True: 
            
            pg = input( )
            
            if pg == '1':
                desc = self.total - (self.total * 0.1) 
                print(f"Aplicado 10% de desconto para pagamentos a vista! R${desc:.2f} ")
                while True:
                    sn = input("Deseja confirmar o pagamento? (s/n) ").lower()
                    if sn == 's':
                        print("Pagamento efetuado! Agradecemos a confiança e volte sempre!")
                        self.pago = True
                        break
                    elif sn == 'n':
                        print("Pagamento cancelado!")
                        return None
                    else:
                        print("Digite uma opção válida! (s/n)")
                if self.pago:
                    break
                
            elif pg == '2':
                print("Parcelamos em até 12x. Até 3x sem juros!\n")
                try:
                    pcl = int(input("Em quantas parcelas deseja? "))
                except ValueError:
                    print("Erro: Valor inválido.")    
                
                if pcl <= 3:
                    v_p = self.total / pcl
                    print(f"Valor das parcelas R${v_p:.2f}. Deseja confirmar o pagamento? (s/n)")
                    while True:
                        sn = input().lower()
                        if sn == 's':
                            print("Pagamento efetuado! Agradecemos a confiança e volte sempre!")
                            self.pago = True
                            break
                        elif sn == 'n':
                            print("Pagamento cancelado!")
                            break
                        else:
                            print("Digite uma opção válida! (s/n)")
                    if self.pago:
                        break
                    
                elif 4 <= pcl <= 12:
                    for i in range(1, pcl + 1):
                        v_p = self.total / pcl
                        parcela = v_p * ((1 + (5/100)) ** i)
                        print(f"Parcela {i} - R$ {parcela:.2f}")
                        
                    print("Deseja confirmar o pagamento? (s/n)")
                    while True:
                        sn = input().lower()
                        if sn == 's':
                            print("Pagamento efetuado! Agradecemos a confiança e volte sempre!")
                            self.pago = True
                            break
                        elif sn == 'n':
                            print("Pagamento cancelado!")
                            break
                        else:
                            print("Digite uma opção válida! (s/n)")
                    if self.pago:
                        break
                    
                else:
                    print("Digite uma quantidade válida!")
            else:
                    print("Digite uma opção válida! (1) ou (2).")
    
    def devolver_veiculo(self, veiculos, reservas):
        if not self.pago:
            print("Não é possível devolver o veículo antes de efetuar o pagamento total da reserva.\n")
            return

        for v in veiculos:
            if v.placa == self.placa:
                v.disponivel = True
                print(f"\nVeículo {v.modelo} ({v.placa}) devolvido com sucesso!\n")

                opcao = input("Deseja registrar alguma manutenção para este veículo? (s/n): ").strip().lower()
                if opcao == 's':
                    v.registrar_manutencao()
                    
                avaliar = input("Deseja avaliar o aluguel? (s/n): ").strip().lower()
                if avaliar == 's':
                    self.avaliar_aluguel()
                break
        else:
            print("Veículo não encontrado!\n")
            return

        os.system('cls')
        print("===== Resumo da Reserva =====")
        print(f"Cliente (CPF): {self.cpf}")
        print(f"Veículo: {self.modelo}")
        print(f"Dias alugados: {self.dias}")
        print(f"Valor total pago: R$ {self.total:.2f}")


        veic_res = next((v for v in veiculos if v.placa == self.placa), None)
        if veic_res and veic_res.manutencao:
            print("\nManutenções realizadas neste veículo durante a reserva:")
            for i, m in enumerate(veic_res.manutencao, 1):
                print(f"{i}. Data: {m['data']} | Descrição: {m['descricao']} | Custo: R${m['custo']}")

        if hasattr(self, 'avaliacao'):
            print(f"\nAvaliação do aluguel: Nota {self.avaliacao}")
            if self.comentario:
                print(f"Comentário: {self.comentario}")
                        
        reservas.remove(self)


    def avaliar_aluguel(self):
        if not self.pago:
            print("Você só pode avaliar o aluguel após efetuar o pagamento da reserva.\n")
            return


        while True:
            try:
                nota = int(input("Dê uma nota de 1 a 5 para o aluguel: "))
                if 1 <= nota <= 5:
                    break
                else:
                    print("Digite uma nota entre 1 e 5.")
            except ValueError:
                print("Por favor, digite um número válido.")
        
        comentario = input("Deseja deixar um comentário? (opcional): ")
        self.avaliacao = nota
        self.comentario = comentario
        print("Avaliação registrada com sucesso!\n")

                  
                  
    def relatar_incidente(self):
        print("=== Relatar Incidente ===")
        
        while True:
            data = input("Data do incidente (dd/mm/aaaa): ").strip()
            try:
                data_obj = datetime.strptime(data, "%d/%m/%Y")
                data_f = data_obj.strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Data inválida! Use o formato correto dd/mm/aaaa.")
                
        descricao = input("Descreva o incidente ocorrido: ").strip()
        
        incidente = {
            'data': data_f,
            'descricao': descricao
        }

        self.incidentes.append(incidente)
        print("Incidente registrado com sucesso!\n")


        
    def exibir_contrato(self, cliente):
        data_inicio = datetime.now()
        data_fim = data_inicio + timedelta(days=self.dias)

        print("\n=========== CONTRATO DE LOCAÇÃO DE VEÍCULO ===========\n")
        print("CLIENTE:")
        print(f"Nome: {cliente.nome}")
        print(f"CPF: {cliente.cpf}\n")

        print("VEÍCULO:")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Valor diário: R$ {self.total / self.dias:.2f}\n")

        print("RESERVA:")
        print(f"Data da reserva: {data_inicio.strftime('%d/%m/%Y')}")
        print(f"Período: {self.dias} dias")
        print(f"Data de devolução prevista: {data_fim.strftime('%d/%m/%Y')}")
        print(f"Total: R$ {self.total:.2f}")
        
        print(f"Forma de pagamento: {'Pago' if self.pago else 'A definir no momento do pagamento'}\n")


        print("CONDIÇÕES GERAIS:")
        print("- O veículo deve ser devolvido limpo e com o tanque cheio;")
        print("- Qualquer dano deverá ser comunicado imediatamente;")
        print("- O cliente é responsável por infrações durante a locação;")
        print("- Em caso de atraso, haverá cobrança adicional por dia;\n")


l_clientes = []
l_veiculos = []
l_reservas = [] 
           
def menu():
    os.system('cls')
    while True:
        print("\n" + "="*40)
        print("     SISTEMA DE LOCAÇÃO DE VEÍCULOS")
        print("="*40)
        print(f"""
        1  - Cadastrar cliente
        2  - Cadastrar veículo
        3  - Ver veículos disponíveis
        4  - Reservar veículo
        5  - Exibir contrato de locação
        6  - Efetuar pagamento
        7  - Registrar manutenção
        8  - Relatar incidente
        9  - Devolver veículo
        10 - Listar manutenções do veículo
        11 - Sair do sistema
        """)
        print("="*40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            c = clientes()
            c.cadastrar_cliente()
            l_clientes.append(c)

        elif opcao == '2':

            os.system('cls')
            v = veiculos()
            v.cadastrar_veiculo()
            l_veiculos.append(v)

        elif opcao == '3':
            os.system('cls')
            veiculos.listar_veiculos(l_veiculos)
    
        elif opcao == '4':
            r = reserva()
            r.fazer_reserva(l_clientes, l_reservas, l_veiculos)
            
        elif opcao == '5':
            os.system('cls')
            cpf = input("Digite o CPF para exibir contrato(s): ").strip()

            cliente = next((c for c in l_clientes if c.cpf == cpf), None)
            if not cliente:
                print("Cliente não encontrado.\n")
                continue

            contratos = [r for r in l_reservas if r.cpf == cpf]

            if not contratos:
                print("Nenhuma reserva encontrada para este CPF.\n")
            else:
                for r in contratos:
                    r.exibir_contrato(cliente)
                    print("=" * 50)

        elif opcao == '6':
            os.system('cls')
            r = reserva.buscar_reserva_por_cpf()
            if r:
                r.efetuar_pagamento()

        elif opcao == '7':
            os.system('cls')
            placa = input("Digite a placa do veículo para registrar manutenção: ").strip().upper()
            veic = next((v for v in l_veiculos if v.placa == placa), None)
            if veic:
                veic.registrar_manutencao()
            else:
                print("Veículo não encontrado.\n")

        elif opcao == '8':
            os.system('cls')    
            r = reserva.buscar_reserva_por_cpf()
            if r:
                r.relatar_incidente()

        elif opcao == '9':  
            print("\n=== DEVOLUÇÃO ===")
            reserva_escolhida = reserva.buscar_reserva_por_cpf()
            
            if reserva_escolhida:
                if reserva_escolhida.pago:
                    reserva_escolhida.devolver_veiculo(l_veiculos, l_reservas)
                else:
                    print("Não é possível devolver o veículo antes de efetuar o pagamento total da reserva.\n")

        elif opcao == '10':
            os.system('cls')
            placa = input("Digite a placa do veículo para listar manutenções: ").strip().upper()
            veic = next((v for v in l_veiculos if v.placa == placa), None)
            if veic:
                veic.listar_manutencoes()
            else:
                print("Veículo não encontrado.\n")


        elif opcao == '11' or opcao.lower() == 'sair':
            break

        else:
            print("Opção inválida. Tente novamente.\n")

menu()
