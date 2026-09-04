# MetalMueble MRP II — Simulación en FlexSim 2027

[![Validación](https://github.com/jtincovalverde/MetalMueble-MRP-II-FlexSim/actions/workflows/validacion.yml/badge.svg)](https://github.com/jtincovalverde/MetalMueble-MRP-II-FlexSim/actions/workflows/validacion.yml)
[![FlexSim](https://img.shields.io/badge/FlexSim-2027-2F6FED)](https://www.flexsim.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)

Proyecto de simulación de manufactura desarrollado a partir de un caso académico de **MRP II y planeamiento de capacidad**. El objetivo es representar el recorrido de un lote de producción, observar la formación de colas y contrastar el comportamiento del sistema con el análisis de capacidad realizado previamente.

> El caso general de MRP II fue desarrollado como trabajo grupal. Este repositorio reúne la parte de simulación, automatización, organización del modelo y validaciones técnicas utilizadas para presentar el proyecto.

## Proceso modelado

```mermaid
flowchart LR
    A[Materia Prima] --> B[Cola Corte]
    B --> C[Corte]
    C --> D[Cola Soldadura]
    D --> E[Soldadura]
    E --> F[Cola Ensamble]
    F --> G[Ensamble]
    G --> H[Cola Acabado]
    H --> I[Acabado]
    I --> J[Producto Terminado]
```

El escenario trabaja con un lote inicial de **420 unidades** y un horizonte de simulación de **40 horas**.

| Centro de trabajo | Tiempo de proceso |
| --- | ---: |
| Corte | 5.6976 min/unidad |
| Soldadura | 13.4723 min/unidad |
| Ensamble | 8.5046 min/unidad |
| Acabado | 10.4762 min/unidad |

El comportamiento esperado es una mayor acumulación antes de **Soldadura**, que también aparece como el centro con mayor presión de capacidad en el análisis del caso.

## Qué permite observar el modelo

- Flujo físico de las piezas entre los centros de trabajo.
- Formación y acumulación de colas.
- Tiempo de espera antes de Soldadura.
- Producción terminada durante el horizonte de simulación.
- Throughput del sistema.
- Identificación visual del cuello de botella.
- Comparación entre la simulación y el análisis de capacidad.

## Archivos principales

No es necesario revisar todo el repositorio para entender el proyecto. Los archivos más importantes son:

- **`iniciar_metalmueble.bat`** — abre FlexSim y prepara automáticamente el modelo.
- **`modelo_metalmueble.txt`** — contiene la lógica de construcción y configuración del modelo.
- **`data/plan_capacidad.csv`** — datos utilizados para contrastar carga y capacidad.
- **`scripts/analisis_capacidad.py`** — reproduce el análisis numérico del caso.
- **`scripts/validar_proyecto.py`** — comprueba que la configuración principal del proyecto se mantenga consistente.
- **`docs/caso_estudio.md`** — resume el contexto académico y los resultados principales.
- **`docs/instrucciones.txt`** — guía breve para ejecutar la simulación.

## Ejecutar la simulación

Se necesita **Windows** y una instalación compatible de **FlexSim 2027**.

1. Cerrar FlexSim si ya está abierto.
2. Ejecutar `iniciar_metalmueble.bat`.
3. Esperar a que FlexSim cargue y configure el modelo.
4. Pulsar **Ejecutar** una vez.
5. Avanzar la simulación para observar las colas, los procesos y el producto terminado.

El lanzador busca la instalación local de FlexSim, prepara un modelo base y carga `modelo_metalmueble.txt` como script de configuración.

## Análisis de capacidad

El caso compara la carga requerida con la capacidad disponible en Corte, Soldadura, Ensamble y Acabado. En el escenario base, **Soldadura requiere 77.85 h frente a 64.77 h disponibles**, por lo que se identifica como el centro sobrecargado.

El cálculo puede reproducirse con:

```bash
python scripts/analisis_capacidad.py
```

## Lógica del lote

La primera pieza se crea en `t = 0` y las siguientes se liberan cada `0.06 s`. La creación se detiene al completar las **420 piezas**, por lo que el lote queda liberado aproximadamente durante los primeros **25.14 segundos simulados**.

La simulación se detiene automáticamente al alcanzar las **40 horas**.

## Visualización de colas

Las piezas se distribuyen dentro del área de cada cola en filas, columnas y capas. Esto evita que todo el inventario en proceso se vea como una única torre y permite apreciar mejor dónde se está acumulando trabajo.

El mismo criterio se utiliza para el producto terminado.

## Indicadores visibles

El modelo incluye indicadores para:

- unidades terminadas;
- contenido de la cola de Soldadura;
- espera promedio antes de Soldadura;
- throughput;
- cuello de botella identificado.

## Validación del proyecto

GitHub Actions ejecuta `scripts/validar_proyecto.py` cada vez que se actualiza el repositorio. Esta validación comprueba, entre otros puntos, el lote de 420 unidades, el horizonte de 40 horas, los tiempos de proceso, los nombres de los objetos principales y la presencia de los indicadores esperados.

Esta comprobación es **estática**. La ejecución visual y dinámica del modelo debe verificarse directamente dentro de FlexSim 2027.

---

[Volver a mi perfil de GitHub](https://github.com/jtincovalverde)
