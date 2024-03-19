# Desafío Teórico

# Procesos, hilos y corrutinas.

- **Un caso en el que usarías procesos para resolver un problema y por qué.**

Podríamos usar procesos en una tarea que se pueda separar en tareas que sean independientes entre sí, entonces la tarea principal se dividiría en subprocesos que se encargarían de diferentes partes del código al tiempo.

- **Un caso en el que usarías threads para resolver un problema y por qué.**

Respuesta

- **Un caso en el que usarías corrutinas para resolver un problema y por qué.**

Respuesta

---

# Optimización de recursos del sistema operativo.

- **Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos información en una API HTTP. ¿Cómo lo harías? Explicar**

Respuesta

---

# Análisis de complejidad.

- **Dados 4 algoritmos A, B, C y D que cumplen la misma funcionalidad, con
complejidades $O(n^2)$, $O(n^3)$, $O(2^n)$ y $O(n\log n)$, respectivamente, ¿Cuál de los
algoritmos favorecerías y cuál descartarías en principio? Explicar por qué.**

Para datasets pequeños por lo general la complejidad algorítmica no importa mucho a menos que nos encontremos con una complejidad exponencial, me refiero a $O(2^n)$, por lo que sería la primera en descartar, es una función que crece extremadamente rápido y puede hacer que nuestro programa sea imposible de ejecutar, por lo general lo podemos ver en algoritmos de backtracking o varios algoritmos de lógica para ciencias de la computación ya que no son muy eficientes, por ejemplo, DPLL, el problema de la 8 reinas etc. Posteriormente se descartaría $O(n^3)$ ya que es el siguiente en orden de complejidad. El primero en favorecer sería $O(n\log n)$ ya que es más eficiente que $O(n^2)$, no obstante $O(n^2)$ no es para nada malo, ya que varios algoritmos de ordenamiento se ejecutan en ese tiempo, por lo general siempre se quiere llegar a $O(n^2)$ o menos en cualquier algoritmo que se plantee. También podemos ver el tema de complejidad como funciones, para esto agregaré una imagen que los represente.

![Imagen](image.png)

En la anterior imagen podemos ver cómo se comportan las funciones anteriormente nombradas, notarán que el mejor rendimiento lo tiene $n \log n$, y posteriormente le sigue $n^2$, también vemos un comportamiento extraño con las otras 2 funciones porque $n^3$ empieza siendo más ineficiente, pero a medida que hay más datos realmente $2^n$ termina siendo más ineficiente.

- **Asume que dispones de dos bases de datos para utilizar en diferentes
problemas a resolver. La primera llamada AlfaDB tiene una complejidad de $O(1)$
en consulta y $O(n^2)$ en escritura. La segunda llamada BetaDB que tiene una
complejidad de $O(n\log n)$ tanto para consulta, como para escritura. ¿Describe en
forma sucinta, qué casos de uso podrías atacar con cada una?**

Teniendo en cuenta que AlfaDB tiene tiempo constante en consulta y cuadrático en escritura deberíamos aprovechar lo eficiente que es al leer datos, por lo que debería usarse en algún problema que requiera poca escritura y mucha lectura de datos, puede ser por ejemplo en algún negocio en una página web que tenga muchísimos clientes y no tenga tantos productos, de todas formas que tenga o no muchos productos no afecta mucho pero los datos se traerían en un tiempo extremadamente rápido por la eficiencia en lectura que tiene la base de datos AlfaDB, al subir un nuevo producto tampoco se demoraría mucho ya que no es un tiempo muy grande pero es mucho mejor para el vendedor que puedan ver sus productos rápidamente.

Para el caso de BetaDB como tiene la misma complejidad en lectura y escritura se podría usar para ver datos en tiempo real, podría por ejemplo usarse en una página de noticias, en donde los datos tengan rapidez al insertarse y al leerse, al contar con un tiempo lineal-logarítmico podemos contar con una fluidez aceptable al publicar y leer contenido nuevo.