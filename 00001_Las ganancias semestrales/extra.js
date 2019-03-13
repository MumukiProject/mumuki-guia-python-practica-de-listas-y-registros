let ultimoSemestre = [{ mes: "julio", ganancia: 50 }, { mes: "agosto", ganancia: -12 }, { mes: "septiembre", ganancia: 1000 }, { mes: "octubre", ganancia: 300 }, { mes:  "noviembre", ganancia: 200 }, { mes: "diciembre", ganancia: 0 }];

let primerTrimestre = [{ mes: "enero", ganancia: 80 }, { mes: "febrero", ganancia: 453 }, { mes: "marzo", ganancia: 1000 }];

function gananciasSemestre(unSemestre) {
  return unSemestre[0].ganancia + unSemestre[1].ganancia +
         unSemestre[2].ganancia + unSemestre[3].ganancia +
         unSemestre[4].ganancia + unSemestre[5].ganancia;