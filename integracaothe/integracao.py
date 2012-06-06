class Integracao:
	
	valor_passagem = None
	
	def __init__(self, valor_passagem):
		self.valor_passagem = float(valor_passagem)

	def meia_passagem(self):
		return self.valor_passagem / 2;

	def inteira_n_onibus(self, qtd_onibus):
		return self.valor_passagem * int(qtd_onibus)

	def meia_n_onibus(self, qtd_onibus):
		return self.meia_passagem() * int(qtd_onibus)


"""
a = Integracao(2.10)
print a.valor_passagem
print a.inteira_n_onibus(3)

"""
