# inventory management system
# english language
This is an inventory management system, which allows the user to add products, consult, update, delete and calculate the total value of the inventory along with error handling.
# idioma español 
este es un sistema de gestion de inventario , el cual le permite al usuario , añadir producto , consultar , actualizar , eliminar y calcular el valor total del inventarion junto con el manejo de errores 

# characteristics
english language
-You can add new products by name, price, and quantity. 
-check product availability; update existing product prices. 
-remove products from inventory; and calculate the total inventory value. 
-All functions are possible thanks to an intuitive menu.
idioma español 
-Puedes añadir nuevos productos por nombre, precio y cantidad.
-Consultar la disponibilidad de productos y actualizar los precios de los productos existentes.
-Eliminar productos del inventario y calcular el valor total del inventario.
-Todas las funciones son posibles gracias a un menú intuitivo.

# how to use
english language
To operate the program, follow the instructions step by step.

        1 = Create inventory
        2 = Check existing product
        3 = Update price
        4 = Delete product
        5 = Add inventory
        6 = Exit
idioma español 
Para utilizar el programa, siga las instrucciones paso a paso.

        1 = Crear inventario
        2 = Consultar producto existente
        3 = Actualizar precio
        4 = Eliminar producto
        5 = Añadir inventario
        6 = Salir

# Technical Details

- Language: Python 3
- Data Structure: Nested dictionaries
- Input Validation: Ensures numeric values are properly entered
- Lambda Function: Calculates total value with: 
**valor_total = lambda: sum(item["price"] * item["amount"] for item in inventory.values())**

idioma español 

- Lenguaje: Python 3
- Estructura de datos: Diccionarios anidados
- Validación de entrada: Garantiza que los valores numéricos se introduzcan correctamente
- Función Lambda: Calcula el valor total con:
**valor_total = lambda: sum(item["price"] * item["amount"] for item in inventory.values())**

# Acceptance Criteria 
• The program must allow the addition of at least 5 initial products.
• When querying a product, it must indicate if it is not in inventory with a clear message.
• Price updates must validate that the new price is a positive number.
• Deleting a product must confirm its existence before deleting it.
• The calculation of the total inventory value must be accurate and display the result to two decimal places.
• The code must be structured into functions for each operation and must include explanatory comments.
• The code and comments must be 100% in English, without exception.

idioma español 

El programa debe permitir la adición de al menos 5 productos iniciales.
Al consultar un producto, debe indicar con un mensaje claro si no está en inventario.
Las actualizaciones de precios deben validar que el nuevo precio sea un número positivo.
Al eliminar un producto, se debe confirmar su existencia antes de eliminarlo.
El cálculo del valor total del inventario debe ser preciso y mostrar el resultado con dos decimales.
El código debe estar estructurado en funciones para cada operación e incluir comentarios explicativos.
El código y los comentarios deben estar 100 % en inglés, sin excepción.

# author
GABRIEL_ALBERTO_PALLARES

