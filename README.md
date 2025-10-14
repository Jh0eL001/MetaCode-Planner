# MetaCode Planner - Planificador Deportivo

Proyecto desarrollado en **Python** con **CustomTkinter** para la gestión de actividades deportivas, por el grupo MetaCode, para la materia de Metodos Tecnicas y  Taller de Programacion.
---
# ESTRUCTURA DEL PROYECTO

```
MetaCode-Planner/
│
├── main.py                      # Punto de entrada de la aplicación
│
├── ui/                          # Interfaces gráficas (pantallas con CustomTkinter)
│   ├── __init__.py
│   ├── ventana_principal.py     # Ventana principal con menú
│   ├── vista_actividades.py     # Pantalla para ver actividades
│   ├── agregar_actividad.py     # Pantalla para agregar actividades
│   └── vista_alertas.py         # Pantalla para alertas
|
├── datos
├── actividades.csv              # Archivo que guarda los datos
|
├── modelos/                     # Lógica de datos y clases
│   ├── __init__.py
│   ├── actividad.py             # Clase Actividad
│   ├── usuario.py               # Clase Usuario/Jugador/Entrenador
│   └── equipo.py                # Clase Equipo
│
├── servicios/                   # Procesos auxiliares
│   ├── __init__.py
│   ├── gestor_actividades.py    # Funciones para agregar/modificar actividades
│   └── generador_reportes.py    # Reportes (para más adelante)
│
├── recursos/                    # Recursos (imágenes, íconos, etc.)
│   └── (vacío por ahora)
│
├── pruebas/                     # Pruebas y validación de código
│   ├── __init__.py
│   └── prueba_basica.py
│
└── README.md                    # Documentación inicial del proyecto
```
# Cambios Y Mejoras a la Interfaz y Estructuras de Datos.

1. Corrección de errores en la interfaz

Se detectó y solucionó un conflicto causado por la duplicidad del parámetro fg_color en los botones principales, lo cual generaba inconsistencias visuales y advertencias en tiempo de ejecución.

Se reorganizó la jerarquía de widgets en la ventana principal, encapsulando los elementos dentro de marcos (CTkFrame) para mantener una estructura más clara y escalable.

2. Mejoras estéticas y de usabilidad

Se redimensionaron los botones principales a un tamaño más amplio (320x55) y se aumentó la tipografía a Arial 16 negrita, con el propósito de mejorar la legibilidad y accesibilidad visual.

Se unificó la paleta de colores: azul para acciones principales y rojo para la opción de salida, garantizando una mejor diferenciación entre funciones.

Se agregó un espaciado uniforme entre botones (pady=15) para evitar saturación visual y facilitar la navegación del usuario.

Se ajustó la ventana principal a una dimensión estándar de 600x400 píxeles, centrada y con márgenes amplios para un diseño limpio y moderno.

3. Estandarización del diseño

Se definió un estilo común para los botones a través de un diccionario de configuración (button_style), permitiendo modificar su formato desde un solo lugar y mantener coherencia visual.

Se mejoró la jerarquía del contenido: el título principal ahora se encuentra centrado, con fuente ampliada (Arial 28 negrita), lo que refuerza la identidad del proyecto.

Se estructuraron los botones dentro de un marco secundario (button_frame) para mejorar la organización del layout y facilitar futuras expansiones (por ejemplo, agregar nuevos menús o paneles laterales).

4. Refactorización funcional

Se simplificó la lógica de navegación mediante la creación de métodos dedicados (abrir_lista, abrir_agregar) que permiten abrir nuevas ventanas sin sobrecargar la clase principal.

Se eliminó código redundante y se reorganizaron los importes para mantener un orden más coherente con la arquitectura modular del proyecto.

5. Implementación de nuevas estructuras de datos

Se introdujo el uso de listas y diccionarios como estructuras de datos principales para el manejo de la información (actividades, usuarios y equipo).

Se integró un gestor de persistencia local mediante archivos JSON, con funciones para guardar y cargar datos desde la carpeta data/, lo cual permite conservar la información entre sesiones sin necesidad de utilizar una base de datos.

Se estandarizó la representación de objetos dentro del código a través de clases modelo (Actividad, Usuario, Equipo), lo que facilita la lectura, manipulación y validación de datos.

Se planificó una separación lógica de capas:

Modelos (representación de datos)

Servicios (procesos de gestión y persistencia)

Interfaz (UI) (presentación visual)
Esta estructura modular favorece la mantenibilidad y escalabilidad futura del sistema.

6. Optimización general del proyecto

Se garantizó que todos los componentes gráficos estén alineados con las buenas prácticas de diseño en CustomTkinter.

Se mejoró la legibilidad general del código, implementando nombres descriptivos en español para clases, métodos y variables, de acuerdo con el idioma del proyecto.

Se redujo la complejidad visual y lógica del archivo principal, estableciendo una estructura más clara y fácilmente entendible para los nuevos integrantes del equipo.
