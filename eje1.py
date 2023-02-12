"""1. Escribir un algoritmo que calcula el precio con todos los impuestos incluidos (TII) 
para un precio sin impuestos y un porcentaje de IVA dado."""
def precio_mas_impuestos():
    precio_sin_impuestos = float(input("Ingrese el precio sin impuestos: "))
    porcentaje_iva = float(input("Ingrese el porcentaje de IVA: "))
    precio_mas_impuestos = precio_sin_impuestos + (precio_sin_impuestos * porcentaje_iva / 100)
    print("El precio con todos los impuestos incluidos es: ", precio_mas_impuestos)
"""2. Escribir un algoritmo que calcula el importe de los intereses generados por un
capital invertido a un interés dado durante un tiempo dado, expresado en meses.
"""
def precio_a_lo_largo_de_un_tiempo():
    capital_invertido = float(input("Ingrese el capital invertido: "))
    interes = float(input("Ingrese el interés: "))
    tiempo = int(input("Ingrese el tiempo en meses: "))
    importe_intereses = capital_invertido * (interes / 100) * tiempo
    print("El importe de los intereses es: ", importe_intereses)

"""1. Escribir un algoritmo que calcula la media aritmética de tres números dados.
"""
def media_aritmetica(num1,num2,num3):
    media_aritmetica = (num1 + num2 + num3) / 3
    print("La media aritmética es: ", media_aritmetica)
def calcular_media_aritmetica():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    media_aritmetica(num1,num2,num3)
"""2. La misma pregunta para una media ponderada cuando se dan los números y los coeficientes de ponderación.
"""
def media_ponderada(num1,num2,num3,coef1,coef2,coef3):
    media_ponderada = (num1 * coef1 + num2 * coef2 + num3 * coef3) / (coef1 + coef2 + coef3)
    print("La media ponderada es: ", media_ponderada)
"""1. Escribir un algoritmo que calcula el área de un triángulo del que se da la 
medida de un lado y la de la altura relativa a este lado.
"""
def area_triangulo(lado,altura):
    area_triangulo = (lado * altura) / 2
    print("El área del triángulo es: ", area_triangulo)
"""2. ¿Se puede utilizar este algoritmo para un triángulo rectángulo si se dan las medidas de sus dos lados perpendiculares?
"""
def area_triangulo_rectangulo(lado1,lado2):
    area_triangulo_rectangulo = (lado1 * lado2) / 2
    print("El área del triángulo rectángulo es: ", area_triangulo_rectangulo)
"""El cálculo de una nómina tiene en cuenta el salario bruto asociado a las horas «normales» que
 debe hacer el empleado y las horas «extra» trabajadas en el mes. Las horas extra se remuneran
  según las siguientes normas administrativas:

Tarifa por hora aumentada en un 125 % para las horas entre la 36.ª y la 43.ª.

Tarifa por hora aumentada en un 150 % para las horas a partir de la 44.ª.

El aumento se realiza sobre la tarifa por hora normal, calculado a partir del salario mensual 
bruto para un año de 52 semanas repartidas en 12 meses, sobre la base de 35 horas trabajadas por semana.

Escribir el algoritmo que calcula el importe de las horas extra que hay que pagar, a partir 
del salario mensual bruto y de la cantidad de horas extra.

Se podrá suponer que el cálculo siempre se usa para una cantidad de horas superior a 8. El
 problema general supone el estudio previo del capítulo siguiente, que trata de la alternativa.
"""
def calcular_nomina(salario_mensual_bruto,horas_extra):
    tarifa_hora_normal = salario_mensual_bruto / 12 / 52 / 35
    if horas_extra > 35 and horas_extra <= 43:
        tarifa_hora_extra = tarifa_hora_normal * 1.25
    elif horas_extra > 43:
        tarifa_hora_extra = tarifa_hora_normal * 1.5
    importe_horas_extra = tarifa_hora_extra * horas_extra
    print("El importe de las horas extra es: ", importe_horas_extra)
"""Se considera las cuentas de depósitos alojadas en un banco por los clientes. Solo 
se permite hacer una retirada si el saldo que queda en la cuenta no es negativo.

1. Definir el tipo de datos CUENTA..

2. Definir las operaciones aplicables.

En determinadas circunstancias y para determinados clientes, la banca autoriza un descubierto limitado y temporal.

3. Volver a hacer las definiciones previas para permitir estos descubiertos.
"""
cuentas = {}
def crear_cuenta(nombre,saldo):
    cuentas[nombre] = saldo
def retirar(nombre,retirada):
    if cuentas[nombre] - retirada >= 0:
        cuentas[nombre] -= retirada
    else:
        print("No se puede retirar esa cantidad")
def depositar(nombre,deposito):
    cuentas[nombre] += deposito
def descubierto_lineal(nombre,descubierto):
    cuentas[nombre] -= descubierto
def programa():
    crear_cuenta("Juan",1000)
    retirar("Juan",500)
    depositar("Juan",200)
    descubierto_lineal("Juan",100)
    print(cuentas)
