describe("", function(){
  it("ganancia_total_4 debe sumar las ganancias de 4 balances", function() {
    assert.equal(ganancia_total_4([{ "mes": "enero", "ganancia": 2 }, { "mes": "febrero", "ganancia": 10 }, { "mes": "marzo", "ganancia": 20 }, { "mes": "abril", "ganancia": 0 }]), 32)
  })
  
  it("ganancia_total_4 debe funcionar con numeros negativos", function() {
    assert.equal(ganancia_total_4([{ "mes": "enero", "ganancia": 2 }, { "mes": "febrero", "ganancia": 10 }, { "mes": "marzo", "ganancia": -20 }, { "mes": "abril", "ganancia": 0 }]), -8)
  })
})
