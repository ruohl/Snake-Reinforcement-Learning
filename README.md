# Snake Game con IA

Este proyecto es un juego de Snake que cuenta con dos modos de juego: uno controlado por un agente aleatorio (`Random`) y otro por un agente de inteligencia artificial (`IA`). Ambos agentes pueden jugar y aprender a través de interacciones en el entorno de juego.

## Estructura del Proyecto

- **`juegos.py`**: Contiene la lógica de los jugadores y las clases `Random` e `IA`, que representan los tipos de jugadores.
- **`jugadores.py`**: Contiene las implementaciones de los agentes `Random` e `IA`, que interactúan con el juego `Snake`.
- **`grilla.py`**: Define la clase `Grilla`, que gestiona el tablero donde se desarrolla el juego.
- **`main.py`**: El archivo principal que permite ejecutar el juego con los distintos agentes.

## Instrucciones de Uso

Para ejecutar el juego, utiliza el siguiente comando en la terminal:

```bash
python main.py ia si ./train.pkl <tamano_grilla> <maxManzanas>
```

## Parametros

1. tipo_jugador: Define el tipo de jugador que controlará el juego. Los valores posibles son:
   - `random`: Jugador aleatorio.
   - `ia`: Jugador de inteligencia artificial.
2. entrenar: Define si el jugador de inteligencia artificial debe entrenarse o no. Los valores posibles son:
   - `si`: Entrenar al jugador.
   - `no`: No entrenar al jugador.
3. archivo: Nombre del archivo donde se guardará el modelo entrenado.
4. tamano_grilla: Tamaño de la grilla del juego.
5. maxManzanas: Cantidad máxima de manzanas que pueden aparecer en la grilla.

## Clases principales

### Grilla

Esta clase representa el tablero del juego y se encarga de renderizarlo en la pantalla utilizando pygame. Tiene funcionalidades para definir el tamaño de cada celda, posicionar elementos en la cuadrícula y ajustar los colores de la cuadrícula.

### Random

Esta clase representa un jugador aleatorio que controla el juego. El jugador toma decisiones aleatorias sobre la dirección en la que se moverá la serpiente.

- Methodos:
  1. jugar(): Ejecuta el juego tomando decisiones aleatorias
  2. entrenar(): Entrena al jugador para que tome decisiones aleatorias

### IA

Un agente basado en Q-learning que aprende de sus acciones y ajusta su política para maximizar la recompensa.

- Methodos:
  1. jugar(): Ejecuta el juego tomando decisiones basadas en el modelo entrenado
  2. entrenar(): Entrena al jugador utilizando Q-learning
  3. save(): Guarda el modelo entrenado en un archivo
  4. load(): Carga un modelo entrenado desde un archivo

## Requisitos

- Instalar python 3
- Instalar pygame

## Integrantes

- Rudolf Garcia Bohl
- Tomas Korzusehec
- Federico Vega
