# 🔒 Desafío: Validación de Código de Usuario con Tuplas y Conjuntos

## 📌 Descripción del Desafío

El objetivo de este programa es validar un código de usuario, asegurando que todos sus caracteres pertenezcan a un conjunto predefinido de caracteres permitidos.

### 🔹 Requisitos

✔ El código debe tener más de 4 caracteres.
✔ Solo se permiten:

* Letras minúsculas (a-z)

* Letras mayúsculas (A-Z)

* Números (0-9)

* Caracteres especiales (-, _, .)

## 📌 Explicación del Código

funcion valid_alpha_mail: Contiene todos los caracteres permitidos.

Bucle while True: Mantiene al usuario en un ciclo hasta que ingrese un código válido.

Validación de longitud (len(user) > 4): Asegura que el código tenga más de 4 caracteres.

Uso de conjuntos (set()): 

* a = set(valid_alpha_mail) → Caracteres permitidos.

* b = set(user) → Caracteres ingresados.

* b - a → Diferencia entre conjuntos (caracteres no permitidos).

* Si len(b - a) > 0, hay caracteres inválidos.

### Mensajes de salida

* Usuario inválido: Si no cumple con los requisitos.

* Usuario válido: Si pasa todas las validaciones.

## 📊 Ejemplo de Ejecución

* Caso 1: Código Válido

```bash
    Ingrese el nombre del usuario: Python_2024  
    ✅ Usuario válido.  
```

* Caso 2: Código con Caracteres Inválidos

```bash
    Ingrese el nombre del usuario: Coder@123  
    ❌ Usuario inválido: Caracteres no permitidos.  
```

* Caso 3: Código Demasiado Corto

```bash
    Ingrese el nombre del usuario: abc  
    ❌ Usuario inválido: Debe tener más de 4 caracteres.  
```

### 📌 ¿Cómo Probar el Programa?

Copia el código en un archivo validacion_usuario.py. Ejecútalo con:

```bash
    python validacion_usuario.py
```

Prueba ingresando diferentes códigos para ver cómo responde.

### 🚀 Aprendizajes Clave

✔ Validación de datos usando conjuntos (set()).
✔ Manejo de bucles (while) para repetir hasta éxito.
✔ Comparación de caracteres con operaciones de conjuntos.
✔ Mensajes claros para guiar al usuario.

### 🔹 Sugerencias mejoras

¿Qué pasa si cambias los caracteres permitidos?

¿Cómo podrías mejorar los mensajes de error?

### Contribuciones

Las sugerencias y mejoras son bienvenidas. Abre un issue o envía un pull request.