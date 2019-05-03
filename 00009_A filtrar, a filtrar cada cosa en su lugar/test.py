
  def test_balances_positivos_filtra_los_balances_que_tengan_ganancia_mayor_a_0(self):
	self.assertEqual(balances_positivos([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": -2 }, { "mes": "septiembre", "ganancia": 0 }]), [{ "mes": "marzo", "ganancia": 10 }])