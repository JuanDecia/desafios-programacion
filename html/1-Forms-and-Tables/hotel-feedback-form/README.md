# Instrucciones Desafío

* Generar una estructura HTML con contenido para una página de adopción de mascotas. El archivo debe contar con la siguiente estructura:

    1. Introducir !DOCTYPE html.
    2. Generar Estructura HTML y colocar el atributo lang en "en".
    3. Completar meta información necesaria.
    4. Agregar un título a la página con el nombre "Hotel Feedback Form".
    5. En el cuerpo generar una estructura semántica correcta con los siguientes elementos obligatorios:

        * Un header con un título con texto "Hotel Feedback Form". Seguido de un parrafo descriptivo.

        * Un nuevo bloque con un elemento "form". El elemento "form" va a quedar dividido en 4 elementos "fieldset" y un "textarea".

        * En el primer "fieldset" se debe colocar un elemento "legend" con el texto "Personal Information". Seguido, debe tener un elemento "input" de tipo "text" con referencia al nombre, otro de tipo "mail", ambos deben estar con una propiedad placeholder que oriente al usuario y deben ser campos obligatorios. Finalizando el bloque se debe colocar un input de tipo "number" para la edad.

        * En el siguiente elemento "fieldset" debe tener como título "Was this your first time at our hotel?". Seguido de dos input de tipo "radio" uno con texto "yes" y el otro "no". Establecer la selección y valor de uno.

        * En el tercer elemento "fieldset" debe contener el texto "Why did you choose to stay at our hotel? (Check all that apply)". Seguido de cinco elementos input con el tipo "checkbox". Cada checkbox debe tener el siguiente texto: "Social Media Ads", "Personal Recommendation", "Location", "Reputation" y "Price". El checckbox de "reputation" debe estar marcado por defecto.

        * Para el último elemento "fieldset" se debe establecer el nombre "Ratings". Seguido de dos elementos "select".

        * El primer elemento "select" debe tener 5 elementos options con los valores de "Poor", "Satisfactory", "Good", "Very Good" y "Excellent". La opción "Excelent" es la que debe aparecer primero por defecto. El label que lo vincula debe tener el texto "How was the service?".

        * El segundo elemento "select" debe tener las mismas propiedades. El elemento label que lo vincula debe tener el texto "How was the food?".

        * El elemento final debe ser un "textarea" estableciendo las columnas y las filas. El elemento label que lo vincula debe tener el texto "Other Comments?".

        * Para cada elemento input del ejercicio se debe establecer y vincular su respectivo elemento "label".