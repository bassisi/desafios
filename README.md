# Twitter Data Analysis Project

## Descripción
Este proyecto analiza un conjunto de datos de tweets para identificar patrones y obtener estadísticas importantes, como los días con más tweets, los emojis más utilizados y los usuarios más influyentes en función de las menciones.

## Estructura del Proyecto
- `challenge.ipynb`: Notebook Jupyter principal donde se realiza el análisis.
- `q1_memory.py`: Implementación de la primera función optimizada para el uso de memoria.
- `q1_time.py`: Implementación de la primera función optimizada para el tiempo de ejecución.
- `q2_memory.py`: Implementación de la segunda función optimizada para el uso de memoria.
- `q2_time.py`: Implementación de la segunda función optimizada para el tiempo de ejecución.
- `q3_memory.py`: Implementación de la tercera función optimizada para el uso de memoria.
- `q3_time.py`: Implementación de la tercera función optimizada para el tiempo de ejecución.

## Instalación
1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd tu_repositorio
    ```
3. Instala las dependencias utilizando Poetry:
    ```sh
    poetry install
    ```

## Uso
### Análisis de Datos
1. Abre `challenge.ipynb` en Jupyter Notebook:
    ```sh
    jupyter notebook challenge.ipynb
    ```
2. Ejecuta las celdas en el notebook para realizar el análisis de datos.

### Ejecución de Funciones
Cada función está disponible en sus respectivos archivos de Python y se pueden importar y utilizar directamente.

```python
from q1_memory import q1_memory
from q1_time import q1_time
from q2_memory import q2_memory
from q2_time import q2_time
from q3_memory import q3_memory
from q3_time import q3_time

# Ejemplo de uso
result = q1_memory('ruta/a/tu/archivo/json')
print(result)
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

<!-- CONTACT -->
## Contacto

Renato Bassi - [@RenaBassi](https://twitter.com/RenaBassi) - renato.bassi@sansano.usm.cl