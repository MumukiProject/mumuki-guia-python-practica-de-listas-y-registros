describe("", function(){
  it("maxima_ganancia devuelve la ganancia mas alta", function() {
    assert.equal(maxima_ganancia([{ "mes": "enero", "ganancia": -40 }, { "mes": "febrero", "ganancia": 42 }, { "mes": "marzo", "ganancia": 19}, { "mes": "abril", "ganancia":  -5}]), 42)
  })
})