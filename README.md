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
│
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