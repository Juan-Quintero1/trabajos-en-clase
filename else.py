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

lista = [5,10,23,10,3]

if lista[2] > 10:
    print("mayor a 10")
else:
    print("menor o igual a 10")

# verifica si el numero 7 esta en la lista [3, 5, 7, 9] si esta, muestra "Esta en la lista", si no, muestra "No esta en la lista".















