# Instrucciones Desafío

* Generar una estructura HTML con contenido para una página de adopción de mascotas. El archivo debe contar con la siguiente estructura:

    1. Introducir !DOCTYPE html.
    2. Generar Estructura HTML y colocar el atributo lang en "en".
    3. Completar meta información necesaria.
    4. Agregar un título a la página con el nombre "Survey Form".
    5. En el cuerpo generar una estructura semántica correcta con los siguientes elementos obligatorios:

        * Un elemento header con un título con texto "Survey Form". El elemento "h1" debe tener un id. Seguido de un elemento párrafo que sea descriptivo.

        * Un nuevo bloque con un elemento "form", este elemento debe tener un "id" con valor "survey-form".

        * En el bloque del formulario colocar los siguientes campos: 1 para nombre (obligatorio); 1 para email (obligatorio); 1 para edad; 1 elemento select; 3 radios; 1 elemento select; 5 checkbox; 1 textarea y finalmente un elemento "button" con texto "submit". Cada elemento de entrada se debe colocar una propiedad "id", "name" y una propiedad "placeholder" que oriente al usuario.

        * Para cada elemento de entrada colocar un elemento "label" que lo vincule.

        * Para el campo del elemento "Age" establecer un mínimo y máximo.

        * Para el 4° elemento (select) el texto del elemento "label" debe ser "Which option best describes your current role?" y las opciones: "Select current role" (esta debe estar seleccionada), "Student", "Full Time Job", "Full Time Learner", "Prefer not Say" y "Other".

        * Para el 5° elemento (radio) el texto del elemento "label" debe ser "What is your favorite feature of JotaCamp?". Los textos de los elementos radio deben ser: "Definitely" (checked), "Maybe" y "Not sure". Seguido del elemento "Select" con las siguientes opciones: "Select an option" (selected), "Challenges", "Community" y "Open Source".

        * El siguiente bloque debe tener un elemento "label" con texto "What would you like to see improved? (Check all that apply)" con los siguientes campos checkbox: "Front-end Projects", "Back-end Projects", "Challenges", "Wiki" y "Forum". Cada elemento debe contener una propiedad "value".

        * En el siguiente bloque se debe colocar un elemento "label" con texto "Any comments or suggestions?", seguido de un elemento "textarea". Al elemento "textarea" colocar un placeholder.

        * Finalmente el elemento button con una propiedad "id" con valor "submit".