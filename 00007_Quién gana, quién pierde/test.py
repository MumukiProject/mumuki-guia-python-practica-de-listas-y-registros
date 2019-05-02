describe("", function(){
  it("promedioGananciasPositivas([{ "mes": marzo, "ganancia": 10 }, { "mes": agosto, "ganancia": 2 }, { "mes": septiembre, "ganancia": -9 }]) es 6", function() {
    assert.equal(promedioGananciasPositivas([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": -9 }]), 6)
  })
  it("gananciaPositiva([{ "mes": marzo, "ganancia": 10 }, { "mes": agosto, "ganancia": 2 }, { "mes": septiembre, "ganancia": -9 }]) es 12", function() {
    assert.equal(gananciaPositiva([{ "mes": "marzo", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "septiembre", "ganancia": -9 }]), 12)
  })
})
