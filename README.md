# Proyecto: Registro de Usuarios con Flask

Este proyecto es una aplicación web simple creada con Flask que permite registrar usuarios, ver una lista de los usuarios registrados y eliminar usuarios existentes. La aplicación incluye validaciones en el formulario de registro y una interfaz sencilla para la gestión de usuarios.

## Características

- Registro de usuarios con nombre, documento de identidad y número de teléfono.
- Posibilidad de borrar usuarios de la lista.
- Interfaz sencilla y funcional.
- Conteo total de usuarios registrados.
  
## Tecnologías Utilizadas

- **Flask**: Framework web para Python.
- **HTML5**: Para estructurar la página.
- **CSS3**: Para estilos básicos.
- **Python**: Para la lógica del backend.

## Instalación y Configuración

### Requisitos

- Python 3.x
- Flask

### Ejecución

1. Inicia la aplicación:
    ```bash
    flask run
    ```

2. Abre tu navegador y visita:
    ```
    http://127.0.0.1:5000/
    ```

## Uso

### Registrar un Usuario

- Ingresa un nombre, documento de identidad y número de teléfono.
- Haz clic en "Registrar" para agregar al usuario a la lista.

### Eliminar un Usuario

- Cada usuario registrado tiene un botón "Borrar" que, al hacer clic, eliminará al usuario de la lista.

### Contador de Usuarios

- En la parte superior de la página se muestra el total de usuarios registrados.

## Archivos Importantes

- **app.py**: Archivo principal de la aplicación Flask donde se definen las rutas y la lógica del servidor.
- **templates/index.html**: Archivo HTML que contiene el formulario de registro y la lista de usuarios.
- **requirements.txt**: Lista de dependencias del proyecto para instalar con pip.
- **static/css/styles.css**: Archivo CSS opcional para personalizar los estilos de la página.