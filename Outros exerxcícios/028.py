class carro:
    def __init__(self, marca, modelo, valor):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
    def ligar(self):
        print('Ligando o carro')
    def EstacionarCarro(self):
        print('Estacionando o carro')
    def ViraCarro(self):
        print('Virado o carro')
    def InformacaoDoCarro(self):
        print(f'Marca: {self.marca:>10}\nModelo:{self.modelo:>10}\nValor: {self.valor:>10}')


veiculo = carro('Hyundai', 'hb20', '63.690')
veiculo.InformacaoDoCarro()
veiculo.ligar()
veiculo.ViraCarro()
veiculo.EstacionarCarro()
