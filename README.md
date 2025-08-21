# EntregaFinal+Echalecu

Proyecto web desarrollado en **Django** siguiendo el patrón **MVT**, como parte del curso de Python en Coderhouse.

---

## 🎯 Objetivo

Crear una aplicación web básica que permita:

- Agregar videojuegos mediante un formulario.
- Ver el listado de videojuegos cargados.
- Buscar videojuegos por título, género o clasificación.
- Ver detalle de cada videojuego.
- Editar o borrar videojuegos existentes (CRUD completo).
- Usar herencia de templates para reutilizar estructura HTML.
- Autenticación de usuarios (registro, login, logout y perfil).
- Página de inicio y página “Acerca de mí”.

---

## ⚙️ Tecnologías utilizadas

- Python 3
- Django 4
- SQLite3 (base de datos por defecto)
- HTML + CSS (templates con herencia)
- Git & GitHub

---

## 📦 Instalación y ejecución

1. **Clonar el repositorio**

```bash
git clone https://github.com/JaviEcha94/EntregaFinal-Echalecu.git
cd EntregaFinal-Echalecu
```

2. **Crear entorno virtual (opcional)**

```bash
python -m venv env
# Mac/Linux
source env/bin/activate
# Windows
.\env\Scripts\activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Crear base de datos y migraciones**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Iniciar el servidor**

```bash
python manage.py runserver
```

👉 Luego ingresá en tu navegador a:  
http://127.0.0.1:8000/

---

## 🚀 Funcionalidades

- **Página principal**: bienvenida y acceso al catálogo.
- **Acerca de mí**: breve biografía de Javier Echalecu.
- **Catálogo de videojuegos**: listado con buscador.
- **Detalle de videojuego**: ver información individual.
- **Formulario de creación/edición/borrado** (CRUD).
- **Autenticación de usuarios**:
  - Registro con username, email y password.
  - Login y logout.
  - Vista de perfil (nombre, apellido, email).
- **Uso de mensajes y validaciones**.
- **Herencia de templates** (`base.html`).

---

## 📁 Estructura del proyecto

EntregaFinal+Echalecu/
├── store/
│   ├── models.py          # Modelo Game
│   ├── forms.py           # Formulario GameForm
│   ├── views.py           # Vistas CBV (List, Detail, Create, Update, Delete)
│   ├── urls.py            # Rutas de la app store
│   └── templates/store/   # Templates del catálogo
├── accounts/
│   ├── forms.py           # Formulario de registro de usuario
│   ├── views.py           # Registro, login, logout, perfil
│   ├── urls.py            # Rutas de la app accounts
│   └── templates/accounts # Templates de autenticación
├── entrega/
│   ├── settings.py        # Configuración del proyecto
│   ├── urls.py            # Rutas principales
│   ├── views.py           # Home y About
│   └── templates/         # Base, home, about, login/logout
├── media/                 # Imágenes subidas por usuarios (en .gitignore)
├── static/                # Archivos estáticos (CSS, imágenes del proyecto)
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md

---

## ✅ Notas

- El archivo `db.sqlite3` y la carpeta `media/` están incluidos en `.gitignore` (no se suben a GitHub).
- El proyecto incluye CBVs con `LoginRequiredMixin` y un decorador `@login_required` en la vista de perfil.
- Templates organizados con herencia (`base.html`).

---

## 👨‍💻 Autor

**Javier Echalecu**  
Proyecto final del curso de Python — Coderhouse.
