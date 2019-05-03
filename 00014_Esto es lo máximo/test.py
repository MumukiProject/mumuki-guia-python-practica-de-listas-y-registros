
  def test_maxima_ganancia_devuelve_la_ganancia_mas_alta(self):
    self.assertEqual(maxima_ganancia([{ "mes": "enero", "ganancia": -40 }, { "mes": "febrero", "ganancia": 42 }, { "mes": "marzo", "ganancia": 19}, { "mes": "abril", "ganancia":  -5}]), 42)