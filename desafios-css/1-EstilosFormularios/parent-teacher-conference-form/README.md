# 📝 Instrucciones del Desafío - Parent Teacher Conference Form
Simular un formulario para completar con los personales de un padre de un alumno.

## 🏗️ Estructura HTML 
Semantica Main, Header, Section, Article Footer:

Header:
- Un título con la descripción "Parent Teacher Conference Form". Seguido de un parrafo descriptivo para completar el formulario.

Section:
- Un elemento <form> que contenga cuatro elementos <fieldset> con los siguientes títulos:
 * Student Information
 * Parent/ Guardian Information
 * Preferred Contact Method
 * Additional Notes

- En el artículo "Student Information", debe contener dos elementos <input>, uno para el nombre (tipo texto) y el otro para el grado (tipo número).

- En el artículo "Parent/ Guardian Information" colocar un elemento <input> de tipo texto.

- En el artículo "Preferred Contact Method" colocar dos <input> de tipo radio. Uno con el texto Email (debe estar seleccionado por defecto) y otro con Teléfono.

- En el artículo "Additional Notes" se debe colocar un elemento <textarea>.

- Cada elemento <input> debe estar vinculado a través de los elementos <label> y a estos darles una descripción adecuada para el campo del formulario.

- Al finalizar el formulario un elemento <button> con texto "Submit".

Footer:
- Párrafo con derechos.

## 🎨 Estilos CSS Requeridos

- El elemento <body> debe tener un fondo de color (preferentemente tonos azules).

- Una fuente general y otra de respaldo.

- El elemento <main> debe estar centrado, con un color diferente al elemento <body>. Debe tener los bordes redondeados y todo su contenido debe estar centrado. Adicionalmente, tiene que tener un efecto de sombreado en todos sus lados.

- El texto del elemento <main> debe estar en un color diferente a negro.

- Los bordes de los elementos <fieldset> deben estar en un color diferente a negro.

- Los campos de los elementos <input> deben estar con los bordes redondeados, con un color diferente a negro y un fondo de color en el tono de los azules.

- El elemento <textarea> debe tener el mismo color de fondo, bordes y redondeado como los elementos <input>.

- El elemento <button> debe tener un fondo de color en tono azul, las letras de un color diferente a negro y los bordes redondeados. Adicionalmente, agregarle un efecto de hover para cambiar de color el fondo.