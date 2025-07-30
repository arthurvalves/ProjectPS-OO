# 🚗 Car Rental System

Este é um sistema simples de locação de veículos desenvolvido em Python. Ele permite o cadastro de clientes e veículos, a reserva de veículos, a listagem de veículos disponíveis, além de apresentar um menu interativo para navegação.

---

## ✅ Funcionalidades implementadas

- Cadastro de clientes (nome, CPF, telefone)
- Cadastro de veículos (modelo, placa, ano, valor por dia)
- Reserva de veículos (apenas se o cliente estiver cadastrado)
- Listagem de veículos disponíveis
- Menu principal com opções numeradas

---

## 🚧 Funcionalidades futuras (em desenvolvimento)

- Efetuar pagamento
- Registrar manutenção
- Relatar incidente
- Avaliar aluguel
- Devolver veículo

---

## 🧱 Estrutura do Código

- `clientes`: lista de objetos contendo os dados dos clientes.
- `veiculos`: lista de objetos com os veículos cadastrados e status de disponibilidade.
- `reservas`: lista de objetos representando reservas realizadas.

### 🔧 Funções principais

- `cadastrar_cliente()`
- `cadastrar_veiculo()`
- `fazer_reserva()`
- `listar_veiculos()`
- `menu()`

---

## 🔍 Modelagem e Granularidade

Para este projeto, foi adotada uma **granularidade grossa** na modelagem dos objetos, visando simplificar a estrutura dos dados e manter o foco em funcionalidades básicas.

### 🧩 Exemplo:

- A classe `Cliente` armazena diretamente:
  - Nome
  - CPF
  - Telefone

- A classe `Veiculo` armazena diretamente:
  - Modelo
  - Placa
  - Ano
  - Valor do aluguel diário
  - Status de disponibilidade

- A classe `Reserva` armazena diretamente:
  - CPF do cliente
  - Placa e modelo do veículo
  - Quantidade de dias
  - Valor total da reserva

> Essa abordagem concentra mais dados em menos objetos, reduzindo a complexidade estrutural e facilitando o desenvolvimento inicial.

---

## 🚀 Execução

Para rodar o sistema:

```bash
python sistema_locadora.py
