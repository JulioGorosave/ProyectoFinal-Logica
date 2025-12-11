Proyecto final para Programación Lógica

Integrantes del equipo

Gorosave Osuna Julio César

Angulo Martínez Ángel Gabriel

Castillo Escareño Coral

Alonso Hernández Devorah

Lazcano Butcher Mario Antonio


Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de recomendación turística construido con FastAPI.
El sistema permite obtener hoteles y actividades cercanas según reglas lógicas basadas en:

Ciudad seleccionada

Presupuesto

Estilo o etiquetas del hotel

Distancia a puntos de interés

El motor aplica reglas lógicas explícitas (R1, R2 y R3) para filtrar opciones de manera razonada, retornando explicaciones detalladas de por qué cada hotel cumple o no con los criterios.

Tecnologías utilizadas

Python 3

FastAPI

Uvicorn

HTML/CSS/JS (frontend)

Motor de inferencia en Python

CORS Middleware


Estructura del proyecto

/api.py          → Servidor principal FastAPI

/config.py       → Configuración de tipos, distancias y etiquetas

/data.py         → Base de datos local de hoteles y puntos de interés

/logic.py        → Motor lógico de inferencia

/install.txt     → Dependencias del proyecto

/html/           → Archivos estáticos del frontend

/images/         → Imágenes para el frontend


Cómo ejecutar el proyecto
1. Instalar dependencias

Ejecuta en terminal:

pip install -r install.txt


2. Iniciar el servidor

Ejecuta:

uvicorn api:app --reload

3. Ingresar al sistema

Una vez levantado el servidor, abre el enlace que aparece en la terminal, por lo general:

http://127.0.0.1:8000/

Características principales del sistema

✔ Buscador inteligente de hoteles

✔ Filtrado por ciudad

✔ Filtrado por presupuesto

✔ Filtrado por etiquetas (romántico, familiar, lujo, etc.)

✔ Listado de actividades cercanas usando la distancia Haversine

✔ Explicaciones lógicas de por qué cada hotel fue aceptado o descartado

