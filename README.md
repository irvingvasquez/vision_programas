# Programas de visión computacional

Material de laboratorio para la materia de [visión computacional][materia] (posgrado). Los ejercicios están organizados como notebooks de Jupyter y cubren los fundamentos de procesamiento de imágenes con **OpenCV** y **NumPy**, desde la lectura de píxeles hasta clasificación con K-NN.

Autor: Irving Vasquez — [jivg.org][jivg]

## Requisitos previos

- Conocimientos básicos de **Python**
- Familiaridad con arrays de NumPy (recomendado)
- **Conda** instalado en el sistema (solo para ejecución local)

No se requiere experiencia previa en visión computacional.

## Instrucciones (2025)

### Opción 1: Ejecutar en Colab

Cada notebook incluye un botón para abrirlo en Google Colab. Presiónalo en la lección que quieras trabajar; no necesitas instalar nada localmente.

### Opción 2 (Local): Ambiente Anaconda

Funciona en **Windows, macOS y Linux** (usa *Anaconda Prompt* o tu terminal).

#### Paso 1 — Crear y activar el ambiente

```bash
# crea el ambiente (Python 3.10 recomendado por compatibilidad amplia)
conda create -n intro_vision python=3.10 -y

# activa el ambiente
conda activate intro_vision
```

#### Paso 2 — Instalar librerías

```bash
# opencv
pip install opencv-python opencv-contrib-python

# paquetes de ipynb
pip install numpy matplotlib jupyterlab scipy moviepy
```

#### Paso 3 — Probar la instalación

```bash
python test_instalacion.py
```

#### (Opcional) Borrar el ambiente

```bash
conda remove --name intro_vision --all
```

El parámetro `--all` indica que se eliminarán todos los paquetes y configuraciones de ese ambiente.

## Instrucciones (Anteriores)

También puedes usar el ambiente Conda del repositorio dedicado: **[vision_environment](https://github.com/irvingvasquez/vision_environment)**.

Una vez activado, verifica las librerías principales:

```sh
python -c "import cv2, numpy, matplotlib; print('OpenCV', cv2.__version__)"
```

### Dependencias principales

| Librería    | Uso                                      |
|-------------|------------------------------------------|
| OpenCV      | Lectura, filtrado, bordes, contornos, ML |
| NumPy       | Operaciones con arrays de píxeles        |
| Matplotlib  | Visualización de imágenes                |
| SciPy       | Kernels gaussianos (`multivariate_normal`) |
| MoviePy     | Procesamiento de video (proyecto de carriles) |

## Cómo ejecutar los notebooks

1. Activa el ambiente Conda (`intro_vision` o `vision_environment`).
2. Entra a la carpeta del módulo que vayas a trabajar (los notebooks usan rutas relativas a imágenes locales).
3. Inicia Jupyter desde esa carpeta:

```sh
cd 02_geometria
jupyter notebook 01_operaciones_basicas.ipynb
```

También puedes usar JupyterLab:

```sh
cd 02_geometria
jupyter lab
```

> **Importante:** ejecuta cada notebook desde su propia carpeta para que las rutas a imágenes y videos (`Lenna.png`, `test_videos/`, etc.) se resuelvan correctamente.

## Estructura del repositorio

```
vision_programas/
├── 01_introduccion/          Lectura y manipulación básica de imágenes
├── 02_geometria/             Operaciones con píxeles y miniproyecto NDI
├── 03_filtrado/              Ruido, correlación, filtro gaussiano, template matching
├── 04_bordes/                Gradientes y detección de bordes (Canny)
├── 05_hough/                 Transformada de Hough y detección de carriles
├── 06_regiones/              Regiones binarias, contornos y segmentación de letras
├── 07_puntos_caracteristicos/ Esquinas de Harris y detección ORB
├── 08_reconocimiento/        Clasificación de dígitos con K-NN
└── soluciones/               Notebooks de referencia para el instructor
```

## Contenido por módulo

### 01 — Introducción

| Notebook | Tema |
|----------|------|
| `01_leer_img.ipynb` | Qué es OpenCV, `imread`, canales BGR/RGB, escala de grises |

> El notebook de introducción referencia `imagen.jpg`. Puedes usar cualquier imagen propia con ese nombre o copiar una de otro módulo (por ejemplo `02_geometria/Lenna.png`).

### 02 — Geometría

| Notebook | Tema |
|----------|------|
| `01_operaciones_basicas.ipynb` | Canales de color, muestreo y cuantización |
| `02_oper_basic.ipynb` | Operaciones aritméticas entre imágenes |
| `Tarea_1_NDI.ipynb` | **Miniproyecto:** índice de diferencia normalizado (NDI) sobre mosaico aéreo |

### 03 — Filtrado

| Notebook | Tema |
|----------|------|
| `01_ruido.ipynb` | Ruido aleatorio en sensores |
| `02_correlacion_cruz.ipynb` | Correlación cruzada y convolución |
| `03_flt_gaussiano.ipynb` | Filtro de media y filtro gaussiano |
| `04_template_match.ipynb` | Búsqueda de plantillas en imágenes |

### 04 — Bordes

| Notebook | Tema |
|----------|------|
| `01_bordes.ipynb` | Gradientes, magnitud, umbralización y detector de Canny |

### 05 — Hough

| Notebook | Tema |
|----------|------|
| `01_deteccion_lineas.ipynb` | Transformada de Hough para detección de líneas |
| `Proyecto_lineas_del_carril.ipynb` | **Miniproyecto:** detección de carriles en imágenes y video (inspirado en Udacity) |

Los videos de prueba están en `05_hough/test_videos/`; las salidas generadas se guardan en `05_hough/test_videos_output/`.

### 06 — Regiones

| Notebook | Tema |
|----------|------|
| `01_regiones.ipynb` | Umbralización de Otsu, máscaras binarias |
| `02_regiones_letras.ipynb` | Segmentación y limpieza de letras en fotografías |

### 07 — Puntos característicos

| Notebook | Tema |
|----------|------|
| `01_esquinas_de_Harris.ipynb` | Detector de esquinas de Harris |
| `orb_detection.ipynb` | Detección y emparejamiento de features con ORB |

### 08 — Reconocimiento

| Notebook | Tema |
|----------|------|
| `01_classificacion_digitos.ipynb` | Clasificación de dígitos manuscritos con K-NN (`cv2.ml`) |

## Carpeta `soluciones/`

Contiene notebooks resueltos para uso del instructor. Los estudiantes deben intentar completar los ejercicios marcados con `TODO` o `RESOLVER` antes de consultarlos.

| Notebook | Corresponde a |
|----------|---------------|
| `01_leer_img_solucion.ipynb` | `01_introduccion/01_leer_img.ipynb` |
| `02_correlacion_cruz_solucion.ipynb` | `03_filtrado/02_correlacion_cruz.ipynb` |
| `03_flt_gaussiano_solucion.ipynb` | `03_filtrado/03_flt_gaussiano.ipynb` |
| `NDI_solucion.ipynb` | `02_geometria/Tarea_1_NDI.ipynb` |

Las variantes `*_youtube.ipynb` son versiones preparadas para grabación de video.

## Convenciones de los ejercicios

- **`TODO`** — sección que el estudiante debe completar.
- **`RESOLVER`** — ejercicio práctico con código pendiente.
- Las imágenes de ejemplo (`Lenna.png`, `ESCOM2_small.jpg`, etc.) están en la misma carpeta del notebook o en carpetas vecinas referenciadas con rutas relativas (`../02_geometria/Lenna.png`).

## Recursos adicionales

- [Curso de visión computacional][materia]
- [Ambiente Conda del curso (legacy)][env]
- [Documentación de OpenCV](https://docs.opencv.org/)

---

Derechos reservados. Irving Vasquez, 2019–2025.

[jivg]: https://jivg.org/
[env]: https://github.com/irvingvasquez/vision_environment
[materia]: https://jivg.org/courses/vision-computacional
