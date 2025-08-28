# Programas de visión computacional

Bienvenidos al curso de visión computacional.

En este repositorio encontrarás la primera parte de ejercicios de la materia de [visión computacional][materia] correspondiente a la visión geométrica.

## Instrucciones (2025)

### Opción 1: Ejecutar en COLAB

Actualmente cada notebook tiene la opción de ejecutarse en colab. Simplemente tienes que oprimir el boton COLAB en cada lección.

### Opción 2 (Local): Ambiente Anaconda

Funciona en **Windows, macOS y Linux** (usa *Anaconda Prompt* o tu terminal).

#### Paso 1 — Crear y activar el ambiente
```bash
# crea el ambiente (Python 3.10 recomendado por compatibilidad amplia)
conda create -n intro_vision python=3.10 -y

# activa el ambiente
conda activate intro_vision

```

### Paso 2 — Instalar librerías


```bash
# opencv
pip install opencv-python opencv-contrib-python

# paquetes de ipynb
pip install numpy matplotlib jupyterlab
```

### Prueba la instalación

```bash
# en windows
python .\test_instalacion.py
```

### (Opcional) Borrar el ambiente

```bash
conda remove --name intro_vision --all
```

El parámetro --all indica que se eliminarán todos los paquetes y configuraciones de ese ambiente.

## Instrucciones (Anteriores)

Primero debes configurar el [ambiente][env] con conda. Una vez instalado y cargado el ambiente debes dirigirte a cada carpeta y ejecutar el notebook. El comando es:

```sh
$ jupyter notebook [archivo].ipynb
```

Si todo esta bien debes de ver el script en tu explorador.

---

Derechos reservados.

Irving Vasquez, 2019-2025
[jivg.org][jivg]


[jivg]: https://jivg.org/
[env]: <https://github.com/irvingvasquez/vision_environment>
[materia]: <https://jivg.org/courses/vision-computacional>
