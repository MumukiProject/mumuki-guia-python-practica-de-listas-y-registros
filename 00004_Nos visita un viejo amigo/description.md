Lo que tenemos que hacer, entonces, es repetir la operación de acumular varias veces, una por cada elemento de la lista. ¡Digamos hola :wave: (nuevamente) al `for...of`!

```javascript
function gananciaTotal(unPeriodo) {
  let sumatoria = 0;
  for (let gananciaDelMes of unPeriodo) {
    sumatoria = sumatoria + gananciaDelMes.ganancia;
  }
  return sumatoria;
}
```

Como ves, el `for...of` nos permite visitar y hacer algo con cada elemento de una lista; en este caso, estaremos visitando cada `gananciaDelMes` de `unPeriodo`.  

> ¿Aún no te convenciste? Nuevamente, probá las siguientes expresiones en la consola:
>
> * `gananciaTotal([])`
> * `gananciaTotal([{ mes: "noviembre", ganancia: 5 }])`
> * `gananciaTotal([{ mes: "marzo", ganancia: 8 }, { mes: "agosto", ganancia: 10 }])`
> * `gananciaTotal([{ mes: "enero", ganancia: 2 }, { mes: "febrero", ganancia: 10 }, { mes: "marzo", ganancia: -20 }])`
> * `gananciaTotal([{ mes: "enero", ganancia: 2 }, { mes: "febrero", ganancia: 10 }, { mes: "marzo", ganancia: -20 }, { mes: "abril", ganancia: 0 }, { mes: "mayo", ganancia: 10 }])`
