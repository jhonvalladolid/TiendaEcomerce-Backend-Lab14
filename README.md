# J&N Moda - Backend

Este es el proyecto backend para J&N Moda, una tienda en línea de moda. Esta aplicación ha sido desarrollada con Django y Django REST Framework.

## Requisitos

- Python (>=3.10)
- Django (>=4.0)
- Django REST Framework (>=3.12)
- Pillow
- django-cors-headers

## Instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/jhonvalladolid/TiendaEcomerce-Backend-Lab14.git
   ```

2. **Crear el entorno virtual fuera del directorio del proyecto**

   ```bash
   python -m venv ent_virtual
   ```

3. **Activar el entorno virtual**

   En Windows:

   ```bash
   ent_virtual\Scripts\activate
   ```

   O en Unix/MacOS:

   ```bash
   source ent_virtual/bin/activate
   ```

4. **Navegar al directorio del proyecto**

   ```bash
   cd TiendaEcomerce-Backend-Lab14
   ```

5. **Instalar dependencias desde el archivo `requirements.txt`**

   ```bash
   pip install -r requirements.txt
   ```

   Si algunas dependencias no se instalaron correctamente, instálalas manualmente:

   ```bash
   pip install python-dotenv
   pip install str2bool
   ```

   Dependencias que se están instalando:
   - `django`: El framework principal para el desarrollo web.
   - `djangorestframework`: Un paquete para construir APIs RESTful con Django.
   - `django-cors-headers`: Un paquete para manejar CORS (Cross-Origin Resource Sharing) en Django.
   - `Pillow`: Una librería para manejar archivos de imagen en Python.
   - `python-dotenv`: Un paquete para manejar archivos .env en Python.
   - `str2bool`: Un paquete para convertir cadenas en booleanos.
   - `django-admin-soft-dashboard`: Un paquete para el dashboard administrativo.
   - `whitenoise`: Un paquete para servir archivos estáticos en producción.
   - `gunicorn`: Un servidor HTTP WSGI para aplicaciones Python.

6. **Crear un superusuario**

   ```bash
   python manage.py createsuperuser
   ```

   O en sistemas donde el comando python se usa de forma diferente:

   ```bash
   py manage.py createsuperuser
   ```

## Ejecutar la aplicación en desarrollo

Para iniciar la aplicación en modo de desarrollo, usa uno de los siguientes comandos:

```bash
python manage.py runserver
```
O en sistemas donde el comando python se usa de forma diferente:

```bash
py manage.py runserver
```

Esto abrirá la aplicación en `http://127.0.0.1:8000/`.

## Configuración del Backend

Este proyecto backend está diseñado para funcionar con un frontend específico. Asegúrate de configurar y ejecutar el frontend correspondiente antes de utilizar este backend.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. **Fork el repositorio**
2. **Crea una nueva rama (git checkout -b feature/nueva-funcionalidad)**
3. **Realiza los cambios necesarios y realiza commit de tus cambios (git commit -m 'Añadir nueva funcionalidad')**
4. **Empuja tus cambios a la rama (git push origin feature/nueva-funcionalidad)**
5. **Abre un Pull Request**

## Notas adicionales

- Asegúrate de tener instalado Pillow para manejar los campos de imagen.
- Asegúrate de tener configurado y ejecutado el backend antes de intentar conectar el frontend.

Para más detalles sobre la configuración y el uso de Django, consulta la [documentación oficial](https://docs.djangoproject.com/en/stable/).
```

Este archivo README.md proporciona una guía clara y detallada para la instalación y configuración del proyecto, incluyendo todos los pasos necesarios para instalar las dependencias y configurar el entorno de desarrollo.