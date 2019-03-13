Ana, contadora de una conocida empresa :office:, tiene registros para representar las ganancias de cada mes y una lista para guardar estas ganancias. Por ejemplo, para el último semestre del año pasado registró las siguientes:

```javascript
//En julio ganó $50, en agosto perdió $12, etc
let ultimoSemestre = [{ mes: "julio", ganancia: 50 }, { mes: "agosto", ganancia: -12 }, { mes: "septiembre", ganancia: 1000 }, { mes: "octubre", ganancia: 300 }, { mes:  "noviembre", ganancia: 200 }, { mes: "diciembre", ganancia: 0 }];
```

Y nos acaba de preguntar: _"¿puedo saber la ganancia de todo **un semestre**?"_

_"Obvio, solo tenemos que sumarlas todas"_, dijimos, y escribimos el siguiente código:

```javascript
function gananciasSemestre(unSemestre) {
  return unSemestre[0].ganancia + unSemestre[1].ganancia +
         unSemestre[2].ganancia + unSemestre[3].ganancia +
         unSemestre[4].ganancia + unSemestre[5].ganancia;
}
```

_"Gracias :plus1:"_, nos dijo Ana, y se fue calcular las ganancias usando la función que le pasamos. Pero un rato más tarde, volvió contandonos que también había registrado las ganancias del primer trimestre de este año:

```javascript
//En enero la empresa ganó $80, en febrero, $453, en marzo $1000
let primerTrimestre = [{ mes: "enero", ganancia: 80 }, { mes: "febrero", ganancia: 453 }, { mes: "marzo", ganancia: 1000 }];
```

Y nos preguntó: _"¿Podría usar esta función que me dieron para calcular las ganancias del primer trimestre?"_. :thought_balloon:

> ¿Tiene algún problema la función `gananciasSemestre` que escribimos anteriormente? ¿Funcionará con trimestres? ¿Y con cuatrimestres?
>
> ¡Probala en la consola!
