# Pruebas Unitarias 2019
## Python

El siguiente proyecto consiste en ejecutar diferentes casos de prueba sobre un modulo en particular. 
Para utilizar el siguiente programa debemos ejecutar el siguiente comando:
`python3 app.py [casos_de _prueba.txt] [Nombre_del_Modulo] [Nombre_de_la_clase]`

El archivo de casos de prueba debe tener el siguiente formato:

`[id]:[nombre_de_la_funcion]:[parametro]:[valor_esperado]`

Una vez terminada la ejecución, el programa creará un archivo JSON reportando los resultados de los casos de prueba con el siguiente formato:

```
{
    "case_id": [id_del_caso_de_prueba],
    "status": [estado_del_caso_de_prueba], // false = fallido, true = exitoso
    "generated": [valor_generado_por_el_metodo],
    "expected": [valor_esperado],
    "exception": [mensaje_de_error], // null = caso de prueba no generó excepciones
    "time_exe": [tiempo_de_ejecucion_de_la_funcion]
}
```

Para ejecutar el caso de prueba de ejemplo ejecutar el siguiente comando (ejecutar desde la raiz).

`python3 proyecto/app.py proyecto/CasosPrueba.txt Medias Media`