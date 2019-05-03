
  def test_ganancias_de_los_balances_de_un_periodo_me_devuelve_solo_los_valores_de_las_ganancias(self):
	self.assertEqual(ganancias([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia":0 }]), [10, 2, 0])