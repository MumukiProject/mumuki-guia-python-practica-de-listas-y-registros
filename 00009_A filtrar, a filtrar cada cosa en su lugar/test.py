describe("", function(){
  it("balancesPositivos filtra los balances que tengan ganancia mayor a 0", function() {
    assert.deepEqual(balancesPositivos([{ mes: "marzo", ganancia: 10 }, { mes: "agosto", ganancia: -2 }, { mes: "septiembre", ganancia: 0 }]), [{ mes: "marzo", ganancia: 10 }])
  })
})