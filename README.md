# Proyecto final para Programación Lógica

###  Integrantes del equipo
- **Gorosave Osuna Julio César**  
- **Angulo Martínez Ángel Gabriel**  
- **Castillo Escareño Coral**  
- **Alonso Hernández Devorah**  
- **Lazcano Butcher Mario Antonio**

---

## Descripción del proyecto
Este proyecto consiste en un **sistema de recomendación turística** desarrollado con **FastAPI**.  
El sistema permite al usuario obtener hoteles y actividades cercanas utilizando un **motor de inferencia lógica**, aplicando reglas basadas en:

- Ciudad seleccionada  
- Presupuesto disponible  
- Etiquetas o características del hotel  
- Distancia máxima hacia puntos de interés  

Cada resultado incluye explicaciones de las reglas aplicadas (R1, R2, R3) para entender por qué el hotel cumple con los criterios.

---

## Tecnologías utilizadas
- **Python 3**
- **FastAPI**
- **Uvicorn**
- **HTML / CSS / JavaScript**
- **Motor lógico en Python**
- **CORS Middleware**

---

## Estructura del proyecto

/api.py → Servidor FastAPI principal

/config.py → Configuración de etiquetas, distancias y tipos

/data.py → Datos de hoteles y actividades

/logic.py → Motor lógico y reglas de inferencia

/install.txt → Dependencias del proyecto

/html/ → Interfaz y archivos estáticos

/images/ → Imágenes del sistema


---

## Cómo ejecutar el proyecto

### 1️⃣ Instalar dependencias
Ejecutar en la terminal:

pip install -r install.txt

---

### 2️⃣ Iniciar el servidor
Ejecutar:

uvicorn api:app --reload


---

### 3️⃣ Abrir el sistema
Visitar en el navegador: http://127.0.0.1:8000/ 



---

## ⭐ Características principales
✔ Filtro por ciudad  
✔ Filtro por presupuesto  
✔ Selección de etiquetas del hotel  
✔ Reglas lógicas (R1, R2, R3) con explicación detallada  
✔ Actividades cercanas mediante distancia Haversine  
✔ API documentada automáticamente con FastAPI  
✔ Respuestas estructuradas en JSON  

---

##  Notas adicionales
Este proyecto fue creado como parte del **Proyecto Final de la materia Programación Lógica**, demostrando el uso de reglas, hechos y un motor de inferencia aplicado a un contexto real.

---





