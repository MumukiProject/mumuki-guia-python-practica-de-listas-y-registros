describe("", function(){
  it("minima_ganancia_positiva devuelve la ganancia mas baja de las positivas", function() {
    assert.equal(minima_ganancia_positiva([{ "mes": "enero", "ganancia": -40 }, { "mes": "febrero", "ganancia": 42 }, { "mes": "marzo", "ganancia": 19}, { "mes": "abril", "ganancia":  -5}]), 19)
  })
})