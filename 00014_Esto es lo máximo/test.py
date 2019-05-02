describe("", function(){
  it("maximaGanancia devuelve la ganancia mas alta", function() {
    assert.equal(maximaGanancia([{ "mes": "enero", "ganancia": -40 }, { "mes": "febrero", "ganancia": 42 }, { "mes": "marzo", "ganancia": 19}, { "mes": "abril", "ganancia":  -5}]), 42)
  })
})