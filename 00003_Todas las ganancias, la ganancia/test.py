
  def test_ganancia_total_4_debe_sumar_las_ganancias_de_4_balances(self):
    self.assertEqual(ganancia_total_4([{ "mes": "enero", "ganancia": 2 }, { "mes": "febrero", "ganancia": 10 }, { "mes": "marzo", "ganancia": 20 }, { "mes": "abril", "ganancia": 0 }]), 32)
  
  def test_ganancia_total_4_debe_funcionar_con_numeros_negativos(self):
    self.assertEqual(ganancia_total_4([{ "mes": "enero", "ganancia": 2 }, { "mes": "febrero", "ganancia": 10 }, { "mes": "marzo", "ganancia": -20 }, { "mes": "abril", "ganancia": 0 }]), -8)
  
