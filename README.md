# 🎬 Buscador Reactivo de Películas  
### Django + RxJS · Programación Avanzada · UCI

Este proyecto implementa una aplicación web con búsqueda reactiva de películas, usando **Python 3**, **Django** y **RxJS**.  
Permite realizar búsquedas en tiempo real, aplicar filtros, ver detalles, gestionar favoritos e historial de búsqueda.  

---

# 🖼 Vista general del sistema

![Vista general](./interfaz/captura.png)

---

# 🚀 Funcionalidades principales

- 🔍 **Búsqueda reactiva**  
- 🎚 **Filtros por año mínimo y máximo**
- 🔠 **Ordenamiento por título o año**
- 🎬 **Vista de detalle de película**
- ⭐ **Sistema de favoritos (persistente)**
- 🕘 **Historial de búsqueda**
- 🗂 **Dataset local de 500 películas**

---

# 🛠 Tecnologías utilizadas

- **Python 3.11+**
- **Django 5**
- **RxJS 7**
- HTML, CSS y JavaScript

# 🔧 Instalación y ejecución

## 1️⃣ Clonar el repositorio o descargar ZIP
- git clone URL_DEL_REPO
- cd Proy_PA_MIA

## 2️⃣ Crear entorno virtual
Windows:
- python -m venv .venv
- .venv\Scripts\activate

Linux / macOS:
- python3 -m venv .venv
- source .venv/bin/activate

## 3️⃣ Instalar dependencias
- pip install django django-cors-headers

## 4️⃣ Aplicar migraciones
- python manage.py migrate

## 5️⃣ Iniciar el servidor
- python manage.py runserver

Abrir en el navegador:
 http://127.0.0.1:8000/

🔄 Regenerar el dataset (opcional)

El dataset movies.json puede recrearse con el script:

python tools/generate_movies_json.py
