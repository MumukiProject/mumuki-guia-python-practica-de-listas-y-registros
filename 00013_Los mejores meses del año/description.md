¡Vamos a terminar esta lección con todo! :muscle:

> Definí estas tres nuevas funciones:
>
* `meses`, el cual dada una lista con registros devuelve una lista de meses :calendar:;
* `afortunados`, que filtra aquellos registros que tuvieron una ganancia mayor a $1000 :dollar:;
* `mesesAfortunados`, devuelve aquellos meses que fueron afortunados.
>
```javascript
ム meses([{ mes: "enero", ganancia: 870 }, { mes: "febrero", ganancia: 1000 }, { mes: "marzo", ganancia: 1020 }, { mes: "abril", ganancia: 2300 }, { mes: "mayo", ganancia: -10 }])
["enero", "febrero", "marzo", "abril", "mayo"]
>
ム afortunados([{ mes: "enero", ganancia: 870 }, { mes: "febrero", ganancia: 1000 }, { mes: "marzo", ganancia: 1020 }, { mes: "abril", ganancia: 2300 }, { mes: "mayo", ganancia: -10 }])
[ { mes: "marzo", ganancia: 1020 }, { mes: "abril", ganancia: 2300 }]
>
ム mesesAfortunados([{ mes: "enero", ganancia: 870 }, { mes: "febrero", ganancia: 1000 }, { mes: "marzo", ganancia: 1020 }, { mes: "abril", ganancia: 2300 }, { mes: "mayo", ganancia: -10 }])
["marzo", "abril"]
```