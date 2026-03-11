# 📝 Instrucciones del Desafío - Job Application Form
Simular un formulario para completar con los requisitos para un puesto de trabajo.

## 🏗️ Estructura HTML 
Semantica Main, Section, Footer:

Section:
- Debe encontrarse dentro del elemento main. A su vez, un elemento <h1> y un elemento <form> que contenga los siguientes campos:
 * Name Information
 * Email Information
 * Position (Select Input)
 * Availability (Radio Input)
 * Textarea

- El campo <select> debe tener tres elementos <option> conlos siguientes datos: Developer, Designer, Manager. Por defecto, debe aparecer la opción "Select a position" como primera vista.

- En la sección de los radio inputs, debe tener dos opciones: "full-time" y "part-time".

- Todos los elementos de entradas deben estar vinculados con la etiqueta <label>. Además que, cada campo de entrada de texto debe tener una propiedad "placeholder" para orientar al usuario. También, deben teneer cada campo la validación de rellenar obligatoriamente.

- Al finalizar el formulario, se debe tener un elemento <button> con texto "Submit".

Footer:
- Párrafo con derechos.

## 🎨 Estilos CSS Requeridos

- Sacar los estilos por defecto del navegador con el selector universal.

- La página debe tener una fuente general y otra de respaldo.

- El elemento <main> debe estar centrado, con una propiedad "box-shadow" que marque el relieve del elemento <section>. El elemento <main> debe tener los bordes redondeados y todo su contenido debe estar centrado.

- La descripción de los campos de entrada deben estar sobre el campo de entrada.

- Los campos de entrada deben tener los bordes de color rojo y deben estar redondeados.

- El selector de los radio input deben estar de color verde.

- El elemento <button> debe tener un fondo de color verde, las letras de un color diferente a negro y los bordes redondeados. Adicionalmente, agregarle un efecto de hover para cambiar de color el fondo y al cursor.