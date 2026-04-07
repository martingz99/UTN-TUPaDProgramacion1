nombre = input("Ingrese su nombre: ")
while not nombre.isalpha():
    print("Error: solo letras, sin espacios ni vacío")
    nombre = input("Ingrese su nombre: ")

cantidad = input("Ingrese la cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese un número entero mayor a 0")
    cantidad = input("Ingrese la cantidad de productos: ")

cantidad = int(cantidad)

total_sin_descuento = 0
total_con_descuento = 0

print(f"\nCliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")

for i in range(cantidad):
    print(f"\nProducto {i+1}")

    # vamos a pedir el dato al usuario, validarlo con .isdigit,
    # posteriormente convertirlo a int
    precio = input("Precio: ")
    while not precio.isdigit():
        print("Error: número inválido")
        precio = input("Precio: ")

    precio = int(precio)
    total_sin_descuento += precio

    # aca en cada vuelta validaremos el precio, la respuesta s/n
    # y aplicaremos el descuento correspondiente
    descuento = input("Descuento (S/N): ").lower()
    while descuento != "s" and descuento != "n":
        print("Error: ingrese S o N")
        descuento = input("Descuento (S/N): ").lower()

    precio_final = precio
    if descuento == "s":
        precio_final = precio * 0.9

    total_con_descuento += precio_final

    print(f"Producto {i+1} - Precio: {precio}  Descuento (S/N): {descuento}")

# aca intentare mostrar el total sin/con descuentos, ahorro total y promedio por producto
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

print("Gracias por comprar, vuelva pronto!")

#//////////////////////////////////////////////////////



# aca colocaremos la credenciales fijas que utilizaremos
usuario_correcto = "alumno"
clave_correcta = "python123"

acceso = False

# El usuario tendra un maximo de 3 intentos
for intento in range(1, 4):
    usuario = input(f"Intento {intento}/3 - Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")

# Si falla 3 veces le aparecera un mensaje de cuenta bloqueada
if not acceso:
    print("Cuenta bloqueada")

# Si entra bien le mostrara el menú
while acceso:
    print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
    opcion = input("Opción: ")

    # Validaremos que sea número
    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    # Luego validaremos el rango
    while opcion < 1 or opcion > 4:
        print("Error: opción fuera de rango.")
        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

    # Aca estan las opciones del menu
    if opcion == 1:
        print("Inscripto")

    elif opcion == 2:
        nueva_clave = input("Nueva clave: ")

        while len(nueva_clave) < 6:
            print("Error: mínimo 6 caracteres.")
            nueva_clave = input("Nueva clave: ")

        confirmacion = input("Confirmar clave: ")

        while confirmacion != nueva_clave:
            print("Error: las claves no coinciden.")
            confirmacion = input("Confirmar clave: ")

        clave_correcta = nueva_clave
        print("Clave cambiada correctamente.")

    elif opcion == 3:
        print("Seguí practicando, vas muy bien.")

    elif opcion == 4:
        print("Saliendo del sistema...")
        break

#////////////////////////////////////////////////////////

# primero pedimos el nombre del operador y verificamos que sean solo letras
operador = input("Ingrese el nombre del operador: ")
while not operador.isalpha():
    print("Error: solo letras.")
    operador = input("Ingrese el nombre del operador: ")

# acá definimos los turnos de cada día, arrancan todos vacíos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# este while es el menú principal, se repite hasta que el usuario decida salir
while True:
    print("\n--- MENÚ ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Opción: ")
# validamos que lo que ingrese sea un número
    while not opcion.isdigit():
        print("Error: ingrese un número.")
        opcion = input("Opción: ")

    opcion = int(opcion)
# validamos que esté dentro del rango del menú
    while opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número.")
            opcion = input("Opción: ")

        opcion = int(opcion)

    # opción 1: reservar turno
    if opcion == 1:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")

        paciente = input("Ingrese nombre del paciente: ")
        # validamos nombre del paciente
        while not paciente.isalpha():
            print("Error: solo letras.")
            paciente = input("Ingrese nombre del paciente: ")

        if dia == "1":
            # Verificar repetido
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: ese paciente ya tiene turno en Lunes.")
            else:
                # Guardar en el primer espacio libre
                if lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado en Lunes - Turno 1")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado en Lunes - Turno 2")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado en Lunes - Turno 3")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado en Lunes - Turno 4")
                else:
                    print("No hay turnos disponibles en Lunes.")

        else:
            # mismo proceso pero para martes
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: ese paciente ya tiene turno en Martes.")
            else:
                # Guardar en el primer espacio libre
                if martes1 == "":
                    martes1 = paciente
                    print("Turno reservado en Martes - Turno 1")
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado en Martes - Turno 2")
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado en Martes - Turno 3")
                else:
                    print("No hay turnos disponibles en Martes.")

     # opción 2: cancelar turno
    elif opcion == 2:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")

        paciente = input("Ingrese nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            print("Error: solo letras.")
            paciente = input("Ingrese nombre del paciente a cancelar: ")
# mostramos los turnos, indicando si están libres
        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""
                print("Turno cancelado en Lunes - Turno 1")
            elif lunes2 == paciente:
                lunes2 = ""
                print("Turno cancelado en Lunes - Turno 2")
            elif lunes3 == paciente:
                lunes3 = ""
                print("Turno cancelado en Lunes - Turno 3")
            elif lunes4 == paciente:
                lunes4 = ""
                print("Turno cancelado en Lunes - Turno 4")
            else:
                print("Ese paciente no tiene turno en Lunes.")
        else:
            if martes1 == paciente:
                martes1 = ""
                print("Turno cancelado en Martes - Turno 1")
            elif martes2 == paciente:
                martes2 = ""
                print("Turno cancelado en Martes - Turno 2")
            elif martes3 == paciente:
                martes3 = ""
                print("Turno cancelado en Martes - Turno 3")
            else:
                print("Ese paciente no tiene turno en Martes.")

    # 3. Ver agenda del día
    elif opcion == 3:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("\nAgenda del Lunes")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("\nAgenda del Martes")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    # 4. Ver resumen general
    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        libres_lunes = 4 - ocupados_lunes
        libres_martes = 3 - ocupados_martes

        print("\n--- RESUMEN GENERAL ---")
        print(f"Lunes -> Ocupados: {ocupados_lunes} | Libres: {libres_lunes}")
        print(f"Martes -> Ocupados: {ocupados_martes} | Libres: {libres_martes}")
# vemos qué día tiene más turnos ocupados
        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Día con más turnos: Empate")

    # opción 5: salir del sistema
    elif opcion == 5:
        print("Sistema cerrado.")
        break  


#////////////////////////////////////////////////////////////////////

# valores iniciales del juego
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0
bloqueado = False

# pedimos el nombre del agente y validamos que sean solo letras
agente = input("Ingrese el nombre del agente: ")
while not agente.isalpha():
    print("Error: solo letras.")
    agente = input("Ingrese el nombre del agente: ")

# este while es el juego en sí, se repite mientras no perdamos ni ganemos
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print("\n--- ESTADO DE LA BÓVEDA ---")
    print(f"Agente: {agente}")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'ON' if alarma else 'OFF'}")
    print(f"Código parcial: {codigo_parcial}")

    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Elegí una opción: ")

    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Elegí una opción: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango.")
        opcion = input("Elegí una opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Elegí una opción: ")

        opcion = int(opcion)

    if opcion == 1:
        forzar_seguidas += 1

        energia -= 20
        tiempo -= 2

        if forzar_seguidas == 3:
            alarma = True
            print("La cerradura se trabó por forzar 3 veces seguidas.")
            print("Se activó la alarma.")
        else:
            if energia < 40:
                riesgo = input("Energía baja. Elegí un número del 1 al 3: ")

                while not riesgo.isdigit():
                    print("Error: ingrese un número válido.")
                    riesgo = input("Energía baja. Elegí un número del 1 al 3: ")

                while riesgo != "1" and riesgo != "2" and riesgo != "3":
                    print("Error: debe ser 1, 2 o 3.")
                    riesgo = input("Energía baja. Elegí un número del 1 al 3: ")

                    while not riesgo.isdigit():
                        print("Error: ingrese un número válido.")
                        riesgo = input("Energía baja. Elegí un número del 1 al 3: ")

                if riesgo == "3":
                    alarma = True
                    print("¡Se activó la alarma!")

            if not alarma and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("Abriste una cerradura.")

# opcion 2: hackear panel

    elif opcion == 2:
        forzar_seguidas = 0  # se corta la racha de forzar

        energia -= 10
        tiempo -= 3

        print("Iniciando hackeo...")
         # usamos un for para simular el progreso
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 - Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("El hackeo abrió automáticamente una cerradura.")

    elif opcion == 3:
        # también corta la racha
        forzar_seguidas = 0

        energia += 15
        if energia > 100:
            energia = 100 # no puede pasar el maximo

        tiempo -= 1
# si la alarma está prendida, descansar te perjudica
        if alarma:
            energia -= 10
            print("La alarma consume energía extra mientras descansás.")

        print("Descansaste.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True
        print("El sistema se bloqueó por alarma.")

print("\n--- RESULTADO FINAL ---")

if cerraduras_abiertas == 3:
    print("VICTORIA: abriste la bóveda.")
elif bloqueado:
    print("DERROTA: la bóveda quedó bloqueada por la alarma.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA: te quedaste sin energía o sin tiempo.")



#//////////////////////////////////////////////////////////////////////////


# bienvenido a la arena
print("--- BIENVENIDO A LA ARENA ---")

# primero pedimos el nombre y validamos que tenga solo letras
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# aca arrancan las estadisticas del juego
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print("=== INICIO DEL COMBATE ===")

# el combate sigue mientras los dos tengan vida
while vida_jugador > 0 and vida_enemigo > 0:

    # mostramos como va el turno
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    # primero validamos que sea numero
    while not opcion.isdigit():
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    # despues validamos que esté entre 1 y 3
    while opcion < 1 or opcion > 3:
        print("Error: Opción fuera de rango.")
        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

    # opcion 1: ataque pesado
    if opcion == 1:
        danio_final = danio_pesado

        # si el enemigo tiene menos de 20 de vida, el golpe sale critico
        if vida_enemigo < 20:
            danio_final = danio_pesado * 1.5

        vida_enemigo -= danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

    # opcion 2: rafaga veloz
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")

        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

            if vida_enemigo <= 0:
                break

    # opcion 3: curar
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100:
                vida_jugador = 100
            pociones -= 1
            print("¡Usaste una poción y recuperaste 30 de vida!")
        else:
            print("¡No quedan pociones!")

    # si el enemigo sigue vivo, te pega
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

# mostramos el final de la pelea
print("\n=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")