Ana, contadora de una conocida empresa :office:, tiene diccionarios para representar los balances de cada mes y una lista para guardarlos. Por ejemplo, para el último semestre del año pasado registró los siguientes:

```python
#En julio ganó $50, en agosto perdió $12, etc
balances_ultimo_semestre = [
  { "mes": "julio", "ganancia": 50 }, 
  { "mes": "agosto", "ganancia": -12 }, 
  { "mes": "septiembre", "ganancia": 1000 }, 
  { "mes": "octubre", "ganancia": 300 }, 
  { "mes":  "noviembre", "ganancia": 200 }, 
  { "mes": "diciembre", "ganancia": 0 }
]
```

Y nos acaba de preguntar: _"¿puedo saber la ganancia de todo **un semestre**?"_

_"Obvio, solo tenemos que sumar las ganancias de todos los balances"_, dijimos, y escribimos el siguiente código:

```python
def ganancia_semestre(balances):
  return balances[0]["ganancia"] + balances[1]["ganancia"] +
         balances[2]["ganancia"] + balances[3]["ganancia"] +
         balances[4]["ganancia"] + balances[5]["ganancia"]
```

_"Gracias :plus1:"_, nos dijo Ana, y se a fue calcular las ganancias usando la función que le pasamos. Pero un rato más tarde, volvió contándonos que también había registrado los balances del primer trimestre de este año:

```python
#En enero la empresa ganó $80, en febrero, $453, en marzo $1000
balances_primer_trimestre = [
  { "mes": "enero", "ganancia": 80 }, 
  { "mes": "febrero", "ganancia": 453 }, 
  { "mes": "marzo", "ganancia": 1000 }
]
```

Y nos preguntó: _"¿Podría usar esta función que me dieron para calcular las ganancias del primer trimestre?"_. :thought_balloon:

> ¿Tiene algún problema la función `ganancia_semestre` que escribimos anteriormente? ¿Funcionará con los balances trimestrales? ¿Y con los cuatrimestrestrales?
>
> ¡Probala en la consola!
