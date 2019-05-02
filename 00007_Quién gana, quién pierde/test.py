describe("", function(){
  it("promedio_ganancias_positivas([{ "mes": marzo, "ganancia": 10 }, { "mes": agosto, "ganancia": 2 }, { "mes": septiembre, "ganancia": -9 }]) es 6", function() {
    assert.equal(promedio_ganancias_positivas([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": -9 }]), 6)
  })
  it("ganancia_positiva([{ "mes": marzo, "ganancia": 10 }, { "mes": agosto, "ganancia": 2 }, { "mes": septiembre, "ganancia": -9 }]) es 12", function() {
    assert.equal(ganancia_positiva([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": -9 }]), 12)
  })
})
