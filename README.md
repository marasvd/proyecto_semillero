# Entropy - Revista Científica (Proyecto Piloto)

## Descripción

Este repositorio contiene la versión beta (BB) y el prototipo inicial del proyecto de la revista científica "Entropy". Se ha desarrollado utilizando Django como framework para la visualización y gestión de la estructura básica de la revista. Este proyecto piloto sirve como una previsualización del proyecto más grande y completo que se desarrollará posteriormente.

## Acceso a la Revista (Versión Piloto)

Por el momento, la revista se puede visualizar accediendo a la siguiente dirección en tu navegador web:http://127.0.0.1:1800/
**Nota:** Es posible que necesites tener el servidor de desarrollo de Django en ejecución para acceder a esta dirección.

## Ejecución del Proyecto (Local)

Para ejecutar este proyecto piloto en tu entorno local, sigue estos pasos:

1.  **Abre la terminal o símbolo del sistema.**
2.  **Navega hasta la raíz del directorio del proyecto.**
3.  **Activa el entorno virtual:**
    ```bash
    .\venv\Scripts\activate
    ```
    (En sistemas macOS o Linux, podría ser `source venv/bin/activate`).
4.  **Arranca el servidor de desarrollo de Django:**
    ```bash
    python manage.py runserver 1800
    ```

## Base de Datos

Actualmente, este proyecto piloto utiliza la base de datos por defecto de Django: `db.sqlite3`. Se reconoce que para la escalabilidad y el rendimiento futuro del proyecto completo, se considerará la migración a una base de datos más robusta.

## Almacenamiento de Archivos

En esta fase piloto, los archivos adjuntos a los artículos (documentos, PDFs, etc.) se están guardando en la carpeta `media/articulos/`. Para la visualización y gestión de estos archivos, así como la información de los usuarios, se puede utilizar la interfaz de administración de Django (el "admin").

## Créditos

Este proyecto ha sido desarrollado íntegramente por:

**María Paz Saavedra**

Se reconoce que este es un prototipo inicial y que existen muchos detalles y funcionalidades que se mejorarán en futuras etapas del proyecto.
