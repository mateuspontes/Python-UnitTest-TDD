import unittest
from integracao import Integracao

class TestIntegracao(unittest.TestCase):
	global integracao
	integracao = Integracao(2.1)

	#def test_meia_passagem(self):
	#	self.assertEqual(integracao.meia_passagem(), 1.05)

	def test_inteira_n_onibus(self):
		self.assertEqual(integracao.inteira_n_onibus(1), 2.1)
		self.assertEqual(integracao.inteira_n_onibus(2), 4.2)
		self.assertEqual(integracao.inteira_n_onibus(4), 8.4)
	
	def test_meia_n_onibus(self):
		self.assertEqual(integracao.meia_n_onibus(1), 1.05)
		self.assertEqual(integracao.meia_n_onibus(2), 2.1)
		self.assertEqual(integracao.meia_n_onibus(4), 4.2)

if __name__ == "__main__":
	unittest.main()