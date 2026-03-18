# 📝 Instrucciones del Desafío - Registration Form
Simular un formulario para el registro de un nuevo usuario.

## 🏗️ Estructura HTML 
Semantica: <main>, <header>, <section>, <article>, <footer>:

### Header:
- Un título con la descripción "Registration Form". Seguido de un salto de línea y un parrafo descriptivo para completar el formulario.

### Section:
- Un elemento <form> con los siguientes campos a requerir:
 
 * Cuatro entradas <input> con sus tipos específicos para: nombre, apellido, mail y contraseña. Seguido de un salto de línea con una barra separadora.

 * Un elemento label con descripción "Account Type". Seguido de dos elementos <input> de tipo radio con las descripciones "Personal" y "Business".

 * Columna separadora

 * Un elemento <label> con descripción "Upload a profile picture", seguido de un elemento <input> de tipo carga de archivos.

 * Un elemento <label> con descripción "Input your Age", seguido de un elemento <input> de tipo número.

 * Un elemento <label> con descripción "How did you hear about us?, seguido de un elemento <select> con las siguientes opciones: select one (principal), Page News, Page Youtube Channel, Page Forum, Other.

 * Un elemento <label> con descripción "Provide a Bio", seguido de un elemento <textarea>.

 * Un elemento <input> de tipo checkbox con descripción "I accept the terms and conditions".

 * Un elemento <button> con descripción "Submit".

- Cada elemento <input> debe estar vinculado a través de un elemento <label>. Dar descripción del campo si fuera necesario.

### Footer:
- Párrafo con derechos.

## 🎨 Estilos CSS Requeridos

- El elemento <body> debe tener un fondo de color (preferentemente tonos azules).

- Una fuente general y otra de respaldo.

- El elemento <main> debe estar centrado y todo su contenido debe estar centrado.

- El texto de la página debe estar en un color diferente a negro.

- Los campos de los elementos <input> deben estar con un fondo de color en el tono de los azules (más oscuro que el de main).

- El elemento <textarea> debe tener el mismo color de fondo que los elementos <input>.

- El elemento <button> debe tener un fondo de color en tono azul (más claro que el de main) y las letras de un color diferente a negro. Adicionalmente, agregarle un efecto de hover para cambiar de color el fondo.