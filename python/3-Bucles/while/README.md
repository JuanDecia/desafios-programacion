# 🔁 Bucles While

Un bucle while es una estructura de control que repite un bloque de código mientras una condición sea verdadera. Es fundamental para ejecutar tareas repetitivas cuando no sabemos de antemano cuántas iteraciones serán necesarias.

## ⚙️ Sintaxis

```python 
    while condición:
        # Bloque de código que se ejecuta
        # mientras la condición sea True
```

### Funcionamiento

1. Evalúa la condición antes de cada iteración

2. Si es True, ejecuta el bloque de código

3. Si es False, sale del bucle

4. Vuelve a evaluar la condición después de cada iteración

## 📝 Operaciones básicas

```python
    contador = 1
    while contador <= 5:
        print(f"Iteración número {contador}")
        contador += 1  # Incremento crucial para evitar loop infinito
```

**Salida**:

```bash
    Iteración número 1  
    Iteración número 2  
    Iteración número 3  
    Iteración número 4  
    Iteración número 5  
```

## 📁 Estructura del directorio

```bash
└── /while/
	├── README.md
	├── /directorio-desafio/
           ├── solucion-desafio.py
           └── README.md
```

## ✅ Desafíos Realizados
** Aquí se colocan los desafíos que se encuentran en el directorio con una descripción del mismo **


## 📌 Contribuciones

**Sigue este flujo**:

1. Haz fork del repositorio
2. Crea una rama para tu feature: git checkout -b mi-nueva-feature
3. Commit tus cambios: git commit -m 'Agrega nueva feature'
4. Push a la rama: git push origin mi-nueva-feature
5. Abre un Pull Request