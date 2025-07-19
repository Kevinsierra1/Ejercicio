import os
equipos = []
fechas = []
# Funciones de Gestión de Equipos
def agregar_equipo():
    # Permite al usuario ingresar el nombre de un nuevo equipo y lo añade a la lista de equipos.
    nombre = input("Ingrese el nombre del equipo: ").capitalize()
    # [Nombre, Lista Jugadores, Lista Cuerpo Técnico, Goles Favor, Goles Contra, PJ, PG, PP, PE]
    equipos.append([nombre, [], [], 0, 0, 0, 0, 0, 0]) 
    print(f"Equipo '{nombre}' registrado con éxito.")
    os.system('pause')
def buscar_equipo_y_gestionar_plantel():
    """Permite al usuario elegir un equipo y luego gestionar su plantel (jugadores o cuerpo técnico)."""
    os.system('cls' if os.name == 'nt' else 'clear')
    if not equipos:
        print("No hay equipos registrados. Por favor, registre un equipo primero.")
        os.system('pause')
        return
    print("--- Gestión de Plantel ---")
    print("Equipos disponibles:")
    for i, equipo in enumerate(equipos):
        print(f"{i+1}. {equipo[0]}") # equipo[0] es el nombre del equipo  
    nombre_equipo = input("\nIngrese el nombre del equipo cuyo plantel desea gestionar: ").capitalize()
    equipo_encontrado = None
    for equipo in equipos:
        if equipo[0] == nombre_equipo:
            equipo_encontrado = equipo
            break   
    if equipo_encontrado:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- Gestionando Plantel de {equipo_encontrado[0]} ---")
            print("1. Gestionar Jugadores")
            print("2. Gestionar Cuerpo Técnico")
            print("3. Regresar al Menú Principal")
            opcion_plantel = input("Seleccione una opción: ")
            match opcion_plantel:
                case '1':
                    menu_jugadores(equipo_encontrado)
                case '2':
                    menu_cuerpo_tecnico(equipo_encontrado)
                case '3':
                    break
                case _:
                    print("Opción no válida. Intente de nuevo.")
                    os.system('pause')
    else:
        print(f"Equipo '{nombre_equipo}' no encontrado.")
        os.system('pause')
def menu_jugadores(equipo: list):
    # """Muestra el menú para gestionar jugadores de un equipo específico."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"--- Gestión de Jugadores de {equipo[0]} ---")
        print("1. Agregar Jugador")
        print("2. Ver Jugadores")
        print("3. Regresar al menú de Plantel")
        opcion_jugador = input("Seleccione una opción: ")
        match opcion_jugador:
            case '1':
                agregar_jugador(equipo)
            case '2':
                ver_jugadores(equipo)
            case '3':
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
                os.system('pause')
def agregar_jugador(equipo: list):
    # """Permite ingresar los detalles de un nuevo jugador para un equipo."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--- Agregando Jugador a {equipo[0]} ---")
    nombre_jugador = input("Ingrese el nombre del jugador: ").capitalize()
    dorsal_str = input("Ingrese el dorsal del jugador: ")
    posicion = input("Ingrese la posición de juego (ej. Portero, Defensa, Medio, Delantero): ").capitalize()
    edad_str = input("Ingrese la edad del jugador: ")
    try:
        dorsal = int(dorsal_str)
        edad = int(edad_str)
        if dorsal <= 0 or edad <= 0:
            print("El dorsal y la edad deben ser números positivos. Intente de nuevo.")
            os.system('pause')
            return
    except ValueError:
        print("El dorsal y/o la edad deben ser números válidos. Intente de nuevo.")
        os.system('pause')
        return
    # equipo[1] es la lista de jugadores
    equipo[1].append([nombre_jugador, dorsal, posicion, edad])
    print(f"Jugador '{nombre_jugador}' agregado a {equipo[0]} con éxito.")
    os.system('pause')
def ver_jugadores(equipo: list):
    # """Muestra la lista de jugadores de un equipo específico."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--- Jugadores de {equipo[0]} ---")
    if not equipo[1]: # equipo[1] es la lista de jugadores
        print("No hay jugadores registrados en este equipo.")
    else:
        for i, jugador in enumerate(equipo[1]):
            print(f"{i+1}. Nombre: {jugador[0]}, Dorsal: {jugador[1]}, Posición: {jugador[2]}, Edad: {jugador[3]}")
    os.system('pause')
def menu_cuerpo_tecnico(equipo: list):
    # """Muestra el menú para gestionar el cuerpo técnico de un equipo específico."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"--- Gestión de Cuerpo Técnico de {equipo[0]} ---")
        print("1. Agregar Miembro del Cuerpo Técnico")
        print("2. Ver Cuerpo Técnico")
        print("3. Regresar al menú de Plantel")
        opcion_cuerpo_tec = input("Seleccione una opción: ")
        match opcion_cuerpo_tec:
            case '1':
                agregar_miembro_cuerpo_tecnico(equipo)
            case '2':
                ver_cuerpo_tecnico(equipo)
            case '3':
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
                os.system('pause')
def agregar_miembro_cuerpo_tecnico(equipo: list):
    # """Permite ingresar los detalles de un nuevo miembro del cuerpo técnico para un equipo."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--- Agregando Miembro del Cuerpo Técnico a {equipo[0]} ---")
    nombre_miembro = input("Ingrese el nombre del miembro del cuerpo técnico: ").capitalize()
    cargo = input("Ingrese el cargo (ej. Entrenador, Asistente, Médico): ").capitalize()
    # equipo[2] es la lista de cuerpo técnico
    equipo[2].append([nombre_miembro, cargo])
    print(f"Miembro '{nombre_miembro}' ({cargo}) agregado a {equipo[0]} con éxito.")
    os.system('pause')
def ver_cuerpo_tecnico(equipo: list):
    # """Muestra la lista de miembros del cuerpo técnico de un equipo específico."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--- Cuerpo Técnico de {equipo[0]} ---")
    if not equipo[2]: # equipo[2] es la lista de cuerpo técnico
        print("No hay miembros del cuerpo técnico registrados en este equipo.")
    else:
        for i, miembro in enumerate(equipo[2]):
            print(f"{i+1}. Nombre: {miembro[0]}, Cargo: {miembro[1]}")
    os.system('pause')
# --- Funciones para la Gestión de la Liga ---
def programar_fecha():
    # """
    # Permite programar partidos para una nueva fecha de la liga.
    # Los partidos se almacenan con marcadores iniciales de -1 (no jugados).
    # """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Programar Fecha ---")
    if len(equipos) < 2:
        print("Necesita al menos dos equipos registrados para programar una fecha.")
        os.system('pause')
        return
    fecha_numero = len(fechas) + 1
    fecha_actual_partidos = [] # Lista para los partidos de esta fecha
    print(f"Programando Fecha {fecha_numero}")
    print("Equipos disponibles:")
    for i, equipo in enumerate(equipos):
        print(f"{i+1}. {equipo[0]}") # equipo[0] es el nombre del equipo
    # Crear una copia para manipular los equipos disponibles en la programación
    equipos_disponibles_nombres = [equipo[0] for equipo in equipos] 
    while len(equipos_disponibles_nombres) >= 2:
        print("\nSeleccione equipos para un partido:")
        print(f"Equipos restantes: {', '.join(equipos_disponibles_nombres) if equipos_disponibles_nombres else 'Ninguno'}")
        equipo_local = input("Ingrese el nombre del equipo local: ").capitalize()
        if equipo_local not in equipos_disponibles_nombres:
            print("Equipo local no válido o ya seleccionado. Intente de nuevo.")
            continue
        equipos_disponibles_nombres.remove(equipo_local)
        equipo_visitante = input("Ingrese el nombre del equipo visitante: ").capitalize()
        if equipo_visitante not in equipos_disponibles_nombres:
            print("Equipo visitante no válido o ya seleccionado. El equipo local será reingresado.")
            equipos_disponibles_nombres.append(equipo_local) # Devuelve el equipo local si el visitante no es válido
            continue
        equipos_disponibles_nombres.remove(equipo_visitante)
        # [Nombre Equipo Local, Nombre Equipo Visitante, Goles Local, Goles Visitante]
        fecha_actual_partidos.append([
            equipo_local,
            equipo_visitante,
            -1, # -1 indica que el partido aún no se ha jugado
            -1
        ])
        print(f"Partido {equipo_local} vs {equipo_visitante} agregado a la Fecha {fecha_numero}.")
    if fecha_actual_partidos:
        fechas.append([fecha_numero, fecha_actual_partidos])
        print(f"\nFecha {fecha_numero} programada con éxito.")
    else:
        print("No se programaron partidos para esta fecha.")
    os.system('pause')
def registrar_marcador():
    # """
    # Permite registrar los marcadores de los partidos programados
    # y actualiza los goles a favor y en contra de los equipos,
    # así como las estadísticas de partidos jugados, ganados, perdidos y empatados.
    # """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Registrar Marcador ---")
    if not fechas:
        print("No hay fechas programadas para registrar marcadores.")
        os.system('pause')
        return
    print("Fechas disponibles:")
    for i, fecha_data in enumerate(fechas):
        print(f"{i+1}. Fecha {fecha_data[0]}") # fecha_data[0] es el número de la fecha
    try:
        fecha_idx = int(input("Seleccione el número de la fecha para registrar marcadores: ")) - 1
        if not (0 <= fecha_idx < len(fechas)):
            print("Selección de fecha no válida.")
            os.system('pause')
            return
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.")
        os.system('pause')
        return
    selected_fecha_data = fechas[fecha_idx] # [numero_fecha, [partidos]]
    print(f"\nPartidos en Fecha {selected_fecha_data[0]}:")
    for i, partido in enumerate(selected_fecha_data[1]): # selected_fecha_data[1] es la lista de partidos
        status = " (PENDIENTE)" if partido[2] == -1 else f" ({partido[2]}-{partido[3]})" # partido[2]=goles local, partido[3]=goles visitante
        print(f"{i+1}. {partido[0]} vs {partido[1]}{status}") # partido[0]=local, partido[1]=visitante
    try:
        partido_idx = int(input("Seleccione el número del partido para registrar el marcador: ")) - 1
        if not (0 <= partido_idx < len(selected_fecha_data[1])):
            print("Selección de partido no válida.")
            os.system('pause')
            return
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.")
        os.system('pause')
        return
    selected_partido = selected_fecha_data[1][partido_idx] # [nombre_local, nombre_visitante, goles_local, goles_visitante]
    if selected_partido[2] != -1:
        print("Este partido ya tiene un marcador registrado. Si desea modificarlo, ingrese los nuevos valores.")
    # Guardar los valores antiguos antes de modificarlos para la actualización de estadísticas
    old_goles_local = selected_partido[2]
    old_goles_visitante = selected_partido[3]
    try:
        goles_local = int(input(f"Ingrese los goles de {selected_partido[0]}: "))
        goles_visitante = int(input(f"Ingrese los goles de {selected_partido[1]}: "))
        if goles_local < 0 or goles_visitante < 0:
            print("Los goles no pueden ser números negativos.")
            os.system('pause')
            return
        # Buscar y obtener índices de los equipos en la lista 'equipos'
        idx_local = -1
        idx_visitante = -1
        for i, equipo in enumerate(equipos):
            if equipo[0] == selected_partido[0]: # equipo[0] es el nombre del equipo
                idx_local = i
            if equipo[0] == selected_partido[1]:
                idx_visitante = i
            # Si ambos equipos ya fueron encontrados, podemos salir del bucle
            if idx_local != -1 and idx_visitante != -1:
                break
        # Revertir estadísticas si el partido ya se había jugado previamente
        if old_goles_local != -1:
            # Revertir estadísticas del equipo local
            equipos[idx_local][3] -= old_goles_local # goles a favor
            equipos[idx_local][4] -= old_goles_visitante # goles en contra
            # Revertir resultados de partidos (PJ, PG, PP, PE)
            if old_goles_local > old_goles_visitante:
                equipos[idx_local][6] -= 1 # PG
            elif old_goles_local < old_goles_visitante:
                equipos[idx_local][7] -= 1 # PP
            else:
                equipos[idx_local][8] -= 1 # PE
            equipos[idx_local][5] -= 1 # PJ
            # Revertir estadísticas del equipo visitante
            equipos[idx_visitante][3] -= old_goles_visitante # goles a favor
            equipos[idx_visitante][4] -= old_goles_local # goles en contra
            # Revertir resultados de partidos
            if old_goles_visitante > old_goles_local:
                equipos[idx_visitante][6] -= 1 # PG
            elif old_goles_visitante < old_goles_local:
                equipos[idx_visitante][7] -= 1 # PP
            else:
                equipos[idx_visitante][8] -= 1 # PE
            equipos[idx_visitante][5] -= 1 # PJ
        # Actualizar los marcadores del partido
        selected_partido[2] = goles_local
        selected_partido[3] = goles_visitante
        # Actualizar estadísticas de los equipos con los nuevos resultados
        if idx_local != -1:
            equipos[idx_local][3] += goles_local # goles a favor
            equipos[idx_local][4] += goles_visitante # goles en contra
            if old_goles_local == -1: # Si el partido no se había jugado antes, incrementa PJ
                equipos[idx_local][5] += 1 # PJ
            if goles_local > goles_visitante:
                equipos[idx_local][6] += 1 # PG
            elif goles_local < goles_visitante:
                equipos[idx_local][7] += 1 # PP
            else:
                equipos[idx_local][8] += 1 # PE
        if idx_visitante != -1:
            equipos[idx_visitante][3] += goles_visitante # goles a favor
            equipos[idx_visitante][4] += goles_local # goles en contra
            if old_goles_local == -1: # Si el partido no se había jugado antes, incrementa PJ
                equipos[idx_visitante][5] += 1 # PJ
            if goles_visitante > goles_local:
                equipos[idx_visitante][6] += 1 # PG
            elif goles_visitante < goles_local:
                equipos[idx_visitante][7] += 1 # PP
            else:
                equipos[idx_visitante][8] += 1 # PE
        print("Marcador registrado con éxito y estadísticas actualizadas.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese números para los goles.")
    os.system('pause')
def equipo_mas_goles_en_contra():
    """Encuentra y muestra el equipo o equipos con la mayor cantidad de goles en contra."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Equipo con Más Goles en Contra ---")
    if not equipos:
        print("No hay equipos registrados.")
        os.system('pause')
        return
    max_goals_against = -1
    teams_with_max_goals_against = [] # Para manejar empates
    for equipo in equipos:
        # equipo[4] es 'Goles en Contra'
        if equipo[4] > max_goals_against:
            max_goals_against = equipo[4]
            teams_with_max_goals_against = [equipo[0]] # Nueva máxima, reinicia la lista con el nombre del equipo
        elif equipo[4] == max_goals_against and max_goals_against != -1: # Si hay empate y ya se han registrado goles
            teams_with_max_goals_against.append(equipo[0]) # Añade a la lista
    if teams_with_max_goals_against:
        if len(teams_with_max_goals_against) == 1:
            print(f"El equipo con más goles en contra es: {teams_with_max_goals_against[0]} con {max_goals_against} goles.")
        else:
            print(f"Los equipos con más goles en contra (empatados con {max_goals_against} goles) son: {', '.join(teams_with_max_goals_against)}.")
    else:
        print("No se han registrado goles en contra todavía o todos los equipos tienen 0 goles.")
    os.system('pause')
def equipo_mas_goles_a_favor():
    """Encuentra y muestra el equipo o equipos con la mayor cantidad de goles a favor."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Equipo con Más Goles a Favor ---")
    if not equipos:
        print("No hay equipos registrados.")
        os.system('pause')
        return
    max_goals_for = -1
    teams_with_max_goals_for = [] # Para manejar empates
    for equipo in equipos:
        # equipo[3] es 'Goles a Favor'
        if equipo[3] > max_goals_for:
            max_goals_for = equipo[3]
            teams_with_max_goals_for = [equipo[0]] # Nueva máxima, reinicia la lista
        elif equipo[3] == max_goals_for and max_goals_for != -1: # Si hay empate y ya se han registrado goles
            teams_with_max_goals_for.append(equipo[0]) # Añade a la lista
    if teams_with_max_goals_for:
        if len(teams_with_max_goals_for) == 1:
            print(f"El equipo con más goles a favor es: {teams_with_max_goals_for[0]} con {max_goals_for} goles.")
        else:
            print(f"Los equipos con más goles a favor (empatados con {max_goals_for} goles) son: {', '.join(teams_with_max_goals_for)}.")
    else:
        print("No se han registrado goles a favor todavía o todos los equipos tienen 0 goles.")
    os.system('pause')
# --- Menús de la Aplicación ---
def menu_liga()-> int:
    """Muestra el menú principal de la Liga BetPlay y retorna la opción seleccionada."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--- Menú Liga BetPlay ---')
    print('1. Registrar equipo')
    print('2. Gestionar plantel (Jugadores y Cuerpo Técnico)')
    print('3. Programar fecha')
    print('4. Registrar marcador')
    print('5. Equipo con más goles en contra')
    print('6. Equipo con más goles a favor')
    print('7. Salir')
    try: 
        opcion = int(input("Seleccione una opción: "))
        if 1 <= opcion <= 7:
            return opcion
        else:
            print("Opción no válida. Intente de nuevo.")
            os.system('pause')
            return menu_liga()
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.")
        os.system('pause')
        return menu_liga()
# --- Bloque de Ejecución Principal ---
if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Bienvenido a la Liga BetPlay')
        opcion = menu_liga()
        match opcion:
            case 1:
                agregar_equipo()  
            case 2:
                buscar_equipo_y_gestionar_plantel()   
            case 3:
                programar_fecha() 
            case 4:
                registrar_marcador()
            case 5:
                equipo_mas_goles_en_contra()
            case 6: 
                equipo_mas_goles_a_favor()
            case 7:
                print("¡Gracias por usar la Liga BetPlay! 👋")
                break
            case _: # Esto no debería ocurrir si el menú valida bien
                print('Opción no válida. Intente de nuevo.')
                os.system('pause')
