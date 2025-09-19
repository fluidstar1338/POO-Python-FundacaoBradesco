class Main:
    nome = "joao"
    print(len(nome))
    pass
    print("testando o projeto")

    from Cliente import Cliente
    from Conta import Conta

    c1 = Cliente("Joao","119442323")
    conta = Conta(c1._nome, "300", "1338")
    print(c1)
    print(c1._nome, " e ",c1._telefone)
    print(conta._titular, "tem o saldo de -> ", conta.saldo, "e numero ", conta._numero)

    conta.deposita(500)
    conta.saque(250)
    conta.extrato()