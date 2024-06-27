# CRIAÇÃO DA CLASSE 
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome 
        self.numero = numero
        self.plano = plano
        
# CRIAÇÃAO DE PROPRIEDADES PARA RETORNAR OS VALORES
        @property
        def nome(self):
            return self.nome
        
        @property
        def numero(self):
            return self.numero
        
        @property
        def plano(self):
            return self.plano
        
# Método para representação em string do objeto

    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."

# FUNÇÃO PRINCIPAL PARA SIMULAR A ENTRADA E SAÍDE DE DADOS


def main():
    
    nome = input()
    numero = input()
    plano = input()
    
# CRIAÇÃO DE UM OBJETO COM OS DADOS FORNECIDOS
    usuario = UsuarioTelefone(nome, numero, plano)

    print(usuario)
    
# Quando o programa é executado (if __name__ == "__main__":), a função main() é chamada.


if __name__ == "__main__":
    main()
