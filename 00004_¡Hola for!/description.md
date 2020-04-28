 Lo que tenemos que hacer, entonces, es repetir la operación de acumular varias veces, una por cada elemento de la lista. ¡Digamos hola :wave: al `for...in`!

```python
def ganancia_total(balances_de_un_periodo):
  sumatoria = 0
  for balance in balances_de_un_periodo:
    sumatoria = sumatoria + balance["ganancia"]
  return sumatoria
```

Como ves, el `for...in` nos permite visitar y hacer algo con cada elemento de una lista; en este caso, estaremos visitando cada `balance` de `balances_de_un_periodo`.  

> ¿Aún no te convenciste? Nuevamente, probá las siguientes expresiones en la consola:
>
>``` python
ム ganancia_total([])
ム ganancia_total([
    { "mes": "noviembre", "ganancia": 5 }
   ])
ム ganancia_total([
    { "mes": "marzo", "ganancia": 8 }, 
    { "mes": "agosto", "ganancia": 10 }
   ])
ム ganancia_total([
    { "mes": "enero", "ganancia": 2 }, 
    { "mes": "febrero", "ganancia": 10 }, 
    { "mes": "marzo", "ganancia": -20 }
   ])
ム ganancia_total([
    { "mes": "enero", "ganancia": 2 }, 
    { "mes": "febrero", "ganancia": 10 }, 
    { "mes": "marzo", "ganancia": -20 }, 
    { "mes": "abril", "ganancia": 0 }, 
    { "mes": "mayo", "ganancia": 10 }
   ])
```


