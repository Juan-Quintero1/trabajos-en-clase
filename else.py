# numero = 24

# if numero > 40:
#     print("El numero es grande")
# else:
#     print("El numero es chico")

#    multiples if
#veamos un ejemplo de como podemos trabajar con multiples ifs anidados

#ejemplo 1
 
# x = 25
# if x > 10:
#     print("Por encima de diez")
#     if x > 20:
#         print("y tambien por encima de 20")
#     else:
#         print("pero no por encima de 20")

# #ejemplo 2

# x = 15
# if x > 10:
#     print("por encima de diez")
#     if x > 20:
#         print("y tambien por encima de 20")
#     else:
#         print("pero no por encima de 20")

#  elif

#   sentencia elfi

# La utlima sentencia condicional que podemos encontrar es el elif (si no si) tambien podriamos decir
# que es un hermano de if, ya que se utiliza en continuacion al if para poder encadenar muchicisimas mas comprobaciones

#estructura basica de condicionales 
# edad = int(input("ingresar edad"))

# if edad < 0:
#     print("no cumple")
# elif edad <= 17:
#     print("es menor de edad")
# elif edad >= 18:
#     print("es mayor de edad")
# elif edad >=45:
#     print("es un adulto mayor")
# else:
#     print("la edad no existe")


# vocal = input("ingrese su vocal para convertir a mayuscula o minuscula")

# if vocal == "a":
#     print("A")
# elif vocal == "e":
#     print("E")
# elif vocal == "i":
#     print("I")
# elif vocal == "o":
#     print("O")
# elif vocal == "u":
#     print("U")
# else:
#     print(f"{vocal}")
    

# # para que sirve la sentencia elif?

# comando = "salir"
# if comando == "ENTRAR":
#     print("Bienvenido al sistema")
# elif comando == "Saludo":
#     print("Hola!¿como estas?")
# elif comando == "salir":
#     print("saliendo del sistema")
# else:
#     print("No se reconoce el comando.")

# basicamente nos sirve para poder darle multiples opciones al programa


# ejercicios condicionales y operaciones matematicas

# verifica si un numero es positivo negativo o cero

# numero = int(input("ingrese un numero"))

# if numero <= -1:
#     print("es un numero negativo")
# elif numero >=1:
#     print("es un numero positivo")
# elif numero == 0:
#     print("el numero es 0")
# else:
#     print("este valor no es un numero")

# calcula es mayor de dos numeros ingresados 

# num1 = int(input("ingresa un numero: "))
# num2 = int(input("ingresa un numero: "))

# if num1 > num2:
#     print(f"el numero {num1} es mayor que {num2}")
# elif num1 < num2:
#     print(f"el numero {num2} es mayor que {num1}")
# else:
#     print("no ingresaste un valor valido")

# determina si un numero es par o impar

# numero = float(input("ingresa un numero"))

# if numero % 2 == 0:             # se usa el % para saber el residuo de la division entre 2 si es 0 es par si no impar
#     print("el numero es par")
# elif numero % 2 == 1:
#     print("el numero es impar")
# else:
#     print("numero no valido")


# dado un numero verifica si esta entre 10 y 20

# numero = int(input("ingrese un numero"))

# if numero <=20 and numero >=10:
#     print("el numero esta entre el 10 y el 20")
# else:
#     print("el numero no esta entre el 10 y el 20")

# dado tres numeros, encuentre el mayor usando condicionales

# num1 = int(input("ingrese el un numero: "))
# num2 = int(input("ingrese el un numero: "))
# num3 = int(input("ingrese el un numero: "))

# if num1 > num2 and num1 > num3:
#     print(f"{num1} es el mayor")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} es el mayor")
# elif num3 > num1 and num3 > num2:
#     print(f"{num3} es el mayor")
# else:
#     print("no se cumple la condiciones")

# calcula el precio final con un 10% de descuento si el total es mayor a $100

# precio = float(input("ingresa el precio:"))

# descuento = precio * 0.10
# precio_final = precio - descuento

# if precio > 100:
#     print(f"el precio final es de {precio_final}")
# else:
#     print(f"el precio final es de {precio}")

# verifica si una persona puede votar (mayor o igual a 18 años)

# edad = int(input("ingresa tu edad: "))

# if edad >= 18:
#     print("puedes votar")
# else:
#     print("no puedes votar")

# dado el precio y tipo de cliente (vip o normal), aplica un descuento del 20% solo al vip

# precio = float(input("ingresa el precio: "))
# tipo_cliente = input("ingres el tipo de cliente (VIP) o (NORMAL): ")

# descuento = precio * 0.10
# precio_final = precio - descuento

# if tipo_cliente == "VIP":
#     print(f"Eres usuario VIP con el 20% de descuento, tu precio final es de {precio_final}")
# elif tipo_cliente == "NORMAL":
#     print(f"Eres usuario NORMAL y tu precio final es de {precio}")
# else:
#     print("Datos mal digitados")

# determina si un numero es multiplo de 5 y de 3 al mismo tiempo

# numero = int(input("ingresa un numero: "))

# if numero % 5 == 0 and numero % 3 == 0:
#     print(f"el numero {numero} es multiplo de 5 y de 3")
# elif numero % 5 == 0:
#     print(f"el numero {numero} es multiplo solamente de 5")
# elif numero % 3 == 0:
#     print(f"el numero {numero} es multiplo solamente de 3")
# else:
#     print("el numero no es multiplo de 5 ni de 3")

# dado un numero verifica si es divisible entre dos numeros dados

# numero = int(input("ingresa un numero: "))

# d1 = int(input("ingres un numero con el que vas a dividir: "))
# d2 = int(input("ingres un numero con el que vas a dividir: "))

# if numero % d1 == 0 and numero % d2 == 0:
#     print(f"el numero {numero} es divisible entre {d1} y {d2}")
# elif numero % d1 == 0:
#     print(f"el numero {numero} solo es divisible entre {d1}")
# elif numero % d2 == 0:
#     print(f"el numero {numero} solo es divisible entre {d2}")
# else:
#     print(f"el numero {numero} no es divisible entre ninguno de los dos numeros")

# ejercicios con listas (con condicionales)

# crea un listado con 5 numeros. si el tercer numero es mayor que 10, muestra "mayor a 10", si no, muestra "menor o igual a 10".

# lista = [5,10,23,10,3]

# if lista[2] > 10:
#     print("mayor a 10")
# else:
#     print("menor o igual a 10")

# # verifica si el numero 7 esta en la lista [3, 5, 7, 9] si esta, muestra "Esta en la lista", si no, muestra "No esta en la lista".
# numeros = [3, 5, 7, 9]

# if 7 in numeros:
#     print("Está en la lista")
# else:
#     print("No está en la lista")

# #suma los dos primeros elementos de la lista [4,6,2,8] si la suma es mayor que 10, muestra "suma alta", de lo contrario, muestra "suma baja"

# numeros = [4, 6, 2, 8]

# suma = numeros[0] + numeros[1]

# if suma > 10:
#     print("suma alta")
# else:
#     print("suma baja")

# #dada la lista ["Ana","luis","pedro","marta"], muestra el ultimo nombre si ese nombre es "marta", muestra "nombre correcto" si no "nombre diferente"
 
# nombres = ["Ana", "luis", "pedro", "marta"]

# ultimo = nombres[-1]  # obtiene el último elemento de la lista

# print(ultimo)

# if ultimo == "marta":
#     print("nombre correcto")
# else:
#     print("nombre diferente")

# #crea una lista con tres colores cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada

# colores = ["rojo", "azul", "verde"]

# if colores[1] == "azul":
#     colores[1] = "amarillo"  # cambio de ejemplo

# print(colores)


# #crea una tupla con los valores [5,8,12,20] si el primer valor es menor que el ultimo muestra "orden ascendente", si no "orden descendente"

# valores = (5, 8, 12, 20)

# if valores[0] < valores[-1]:
#     print("orden ascendente")
# else:
#     print("orden descendente")

# #dada la tupla (25,32,28), verifica si el segundo valor es mayor a 30. si lo es muestra "edad mayor a 30",si no, "edad menor o igual a 30"

# edades = (25, 32, 28)

# if edades[1] > 30:
#     print("edad mayor a 30")
# else:
#     print("edad menor o igual a 30")

# #convierte la tupla (1,2,3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convetirla a tupla y muestrala

# tupla_original = (1, 2, 3)

# # Convertir a lista
# lista = list(tupla_original)

# # Cambiar el segundo valor si es igual a 2
# if lista[1] == 2:
#     lista[1] = 10

# # Convertir nuevamente a tupla
# tupla_modificada = tuple(lista)

# # Mostrar la tupla final
# print(tupla_modificada)

# #dada la tupla (4,9), accede al segundo valor. si es mayor que 5, muestra "coordenada alta", si no, "coordenada baja"

# coordenadas = (4, 9)

# if coordenadas[1] > 5:
#     print("coordenada alta")
# else:
#     print("coordenada baja")


# #compara si las tuplas (3,4) y (3,5) son iguales, si lo son, muestra "tuplas iguales", si no, "tuplas diferente"

# tupla1 = (3, 4)
# tupla2 = (3, 5)

# if tupla1 == tupla2:
#     print("tuplas iguales")
# else:
#     print("tuplas diferentes")


# #crea un diccionario con {"nombre": "juan", "edad": 17}. si la edad es mayor o igual a 18, muestra "adulto", si no, muestra "menor de edad"

# persona = {"nombre": "juan", "edad": "17"}

# if int(persona["edad"]) >= 18:
#     print("adulto")
# else:
#     print("menor de edad")


# #crea un diccionario {"nombre": "lucia", "edad": 20}. si la edad es mayor a 18, cambia el valor edad a 21. luego muestra el diccionario

# persona = {"nombre": "lucia", "edad": 20}

# if persona["edad"] > 18:
#     persona["edad"] = 21

# print(persona)

# #crea un diccionario con {"nombre": "carlos"} si la clave "ciudad" no existe, agregala con el valor "bogota" y muestra el diccionario

# persona = {"nombre": "carlos"}

# if "ciudad" not in persona:
#     persona["ciudad"] = "bogota"

# print(persona)

# #dado el diccionario {"producto": "pan", "precio": 1200}, verifica si la clave "precio" existe. si existe, muestra su valor, si no, muestra "no hay precio"

# producto = {"producto": "pan", "precio": 1200}

# if "precio" in producto:
#     print(producto["precio"])
# else:
#     print("no hay precio")


# #crea un diccionario con {"pan": 1200, "leche": 2000}. si "pan" esta en el diccionario muestra su precio; si no muestra "producto no disponible"

# productos = {"pan": 1200, "leche": 2000}

# if "pan" in productos:
#     print(productos["pan"])
# else:
#     print("producto no disponible")
