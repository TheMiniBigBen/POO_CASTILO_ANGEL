class Edificio:
    def __init__(self, nombre, numero_pisos, habitaciones_por_piso):
        self.nombre = nombre
        self.numero_pisos = numero_pisos
        self.habitaciones_por_piso = habitaciones_por_piso
        self.habitaciones = []

        for piso in range(1, numero_pisos + 1):
            for habitacion in range(1, habitaciones_por_piso + 1):
                self.habitaciones.append(Habitacion(habitacion, piso, self))

    def informacion_edificio(self):
        print("Información del edificio:")
        print("Nombre:", self.nombre)
        print("Número de pisos:", self.numero_pisos)
        print("Habitaciones por piso:", self.habitaciones_por_piso)
        print("Total de habitaciones:", len(self.habitaciones))

class Habitacion:
    def __init__(self, numero, piso, edificio):
        self.numero = numero
        self.piso = piso
        self.ocupado = False
        self.edificio = edificio

    def asignar_habitacion(self):
        self.ocupado = True

    def liberar_habitacion(self):
        self.ocupado = False

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Edificio: ",self.edificio, "Habitación número: #", self.numero, "en el piso número: #", self.piso, "Ocupado:", self.ocupado)

class PersonalMedico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def informacion_personal(self):
        print("Nombre:", self.nombre)
        print("Especialidad:", self.especialidad)

class Doctor(PersonalMedico):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre, especialidad)

class Enfermera(PersonalMedico):
    def __init__(self, nombre):
        self.nombre = nombre

    def informacion_enfermera(self):
        print("Nombre:", self.nombre)

class Paciente:
    def __init__(self, nombre, edad, padecimiento, habitacion, doctor, enfermera, comida):
        self.nombre = nombre
        self.edad = edad
        self.padecimiento = padecimiento
        self.habitacion = habitacion
        self.doctor = doctor
        self.enfermera = enfermera
        self.comida = comida

    def mostrar_informacion(self):
        print("Nombre:", self.nombre, "Edad:", self.edad, "padecimiento:", self.padecimiento)
        if self.habitacion:
            print("Habitación:", self.habitacion.numero, "Piso:", self.habitacion.piso, "Edificio:", self.habitacion.edificio.nombre)
        print("Doctor:", self.doctor.nombre)
        print("Enfermera:", self.enfermera.nombre)
        print("Comida:", self.comida.nombre)

class Visita:
    def __init__(self, nombre, relacion, paciente):
        self.nombre = nombre
        self.relacion = relacion
        self.paciente = paciente

    def informacion_visita(self):
        print("Nombre: ", self.nombre, "Relación: ", self.relacion, "Paciente: ", self.paciente.nombre)

class Comida:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def informacion_comida(self):
        print("Nombre: ", self.nombre,"Cantidad de raciones por día: ", self.cantidad)

class Hospital:
    def __init__(self, nombre, edificios):
        self.nombre = nombre
        self.edificios = edificios
        self.personal = []
        self.pacientes = []
        self.visitas = []

edificio1 = Edificio("Hospital A", 3, 5)
edificio2 = Edificio("Hospital B", 3, 5)
edificio3 = Edificio("Hospital C", 3, 5)

hospital_general = Hospital("Hospital General", [edificio1, edificio2, edificio3])

doctor1 = Doctor("Dr. Mauricio", "Cirijano")
doctor2 = Doctor("Dr. Juan", "Neurología")
doctor3 = Doctor("Dr. Pedro", "Oncología")
doctor4 = Doctor("Dr. Jose", "Pediatría")
doctor5 = Doctor("Dra. Maria", "Cardiología")

hospital_general.personal.append(doctor1)
hospital_general.personal.append(doctor2)
hospital_general.personal.append(doctor3)
hospital_general.personal.append(doctor4)
hospital_general.personal.append(doctor5)

enfermera1 = Enfermera("Enf. Martinez")
enfermera2 = Enfermera("Enf. Lopez")
enfermera3 = Enfermera("Enf. Rodriguez")
enfermera4 = Enfermera("Enf. Garcia")
enfermera5 = Enfermera("Enf. Perez")

hospital_general.personal.append(enfermera1)
hospital_general.personal.append(enfermera2)
hospital_general.personal.append(enfermera3)
hospital_general.personal.append(enfermera4)
hospital_general.personal.append(enfermera5)

comida1 = Comida("Vegetariana", 3)
comida2 = Comida("Infantil", 3)
comida3 = Comida("Normal", 4)
comida4 = Comida("0 Azucar", 5)

comidas = [comida1, comida2, comida3, comida4]

pacientes = []

visita = []

def agregar_paciente():
    nombre = input("Nombre del paciente: ")
    while True:
        try:
            edad = int(input("Edad del paciente: "))
            break
        except ValueError:
            print("Ingrese un número válido.")

    print("Edificios disponibles:")
    for i, edificio in enumerate(hospital_general.edificios):
        print(i + 1, ".", edificio.nombre) 
    edificio_elegido = hospital_general.edificios[int(input("Elija un edificio (1-3): ")) - 1]

    print()
    print("Pisos disponibles en", edificio_elegido.nombre, ":")
    for piso in range(1, edificio_elegido.numero_pisos + 1):
        print(piso, end=" ")
    print()

    piso_elegido = int(input("Elija un piso: "))

    print("Habitaciones disponibles en el piso", piso_elegido, ":")
    habitaciones_disponibles = []
    for habitacion in edificio_elegido.habitaciones:
        if habitacion.piso == piso_elegido and not habitacion.ocupado:
            habitaciones_disponibles.append(habitacion)
            print(habitacion.numero, end=" ")
    print()

    if not habitaciones_disponibles:
        print("No hay habitaciones disponibles en este piso.")
        return

    habitacion_elegida = int(input("Elija una habitación: "))

    print("Doctores disponibles:")
    for i, doctor in enumerate(hospital_general.personal):
        if isinstance(doctor, Doctor):
            print(str(i + 1) + ". " + doctor.nombre)
    doctor_elegido = int(input("Elija un doctor: ")) - 1
    doctor = hospital_general.personal[doctor_elegido]

    print("Enfermeras disponibles:")
    for i, enfermera in enumerate(hospital_general.personal):
        if isinstance(enfermera, Enfermera):
            print(str(i - 4) + ". " + enfermera.nombre)
    enfermera_elegida = int(input("Elija una enfermera: ")) - 4
    enfermera = hospital_general.personal[enfermera_elegida]

    print("Comidas disponibles:")
    for i, comida in enumerate(comidas):
        print(str(i + 1) + ". " + comida.nombre)
    comida_elegida = int(input("Elija una comida: ")) - 1
    comida = comidas[comida_elegida]

    habitacion_encontrada = None
    for habitacion in habitaciones_disponibles:
        if habitacion.numero == habitacion_elegida:
            habitacion_encontrada = habitacion
            break

    if habitacion_encontrada:
        habitacion_encontrada.ocupado = True
        paciente = Paciente(nombre, edad, padecimiento, habitacion_encontrada, doctor, enfermera, comida)
        hospital_general.pacientes.append(paciente)
        print("Paciente agregado exitosamente. Edificio:", edificio.nombre,
              ", Habitación:", habitacion_encontrada.numero, ", Piso:", piso_elegido)
    else:
        print("La habitación elegida no está disponible.")

def eliminar_paciente():
    
    if not hospital_general.pacientes:
        print("No hay pacientes registrados en el hospital.")
        return

    print("Pacientes registrados:")
    for i, paciente in enumerate(hospital_general.pacientes):
        print(i + 1, ".", paciente.nombre, "(Edificio:", paciente.habitacion.edificio.nombre, ", Habitación:", paciente.habitacion.numero, ",", "Piso:", paciente.habitacion.piso, ".)")
    
    while True: 
        try:
            paciente_elegido = int(input("Elija el número del paciente a eliminar: ")) - 1
            if 0 <= paciente_elegido < len(hospital_general.pacientes):
                break
            else:
                print("Opción inválida. Elija un número de paciente válido.")
        except ValueError:
            print("Ingrese un número válido.")

    paciente = hospital_general.pacientes.pop(paciente_elegido)
    paciente.habitacion.liberar_habitacion()
    print("Paciente", paciente.nombre, "eliminado exitosamente.")
    print("Habitación", paciente.habitacion.numero, "liberada.")

def agregar_visita():
    if not hospital_general.pacientes:
        print("No hay pacientes registrados en el hospital.")
        return

    print("Pacientes registrados:")
    for i, paciente in enumerate(hospital_general.pacientes):
        print(i + 1, ".", paciente.nombre)

    while True:
        try:
            paciente_elegido = int(input("Elija el número del paciente a visitar: ")) - 1
            if 0 <= paciente_elegido < len(hospital_general.pacientes):
                break
            else:
                print("Opción inválida. Elija un número de paciente válido.")
        except ValueError:
            print("Ingrese un número válido.")

    paciente = hospital_general.pacientes[paciente_elegido]

    nombre_visitante = input("Ingrese el nombre del visitante: ")
    relacion = input("Ingrese la relación con el paciente: ")

    visita = Visita(nombre_visitante, relacion, paciente)
    hospital_general.visitas.append(visita)
    print("Visita de " + nombre_visitante + " (" + relacion + ") agregada para el paciente " + paciente.nombre + ".")

def eliminar_visita():
    if not hospital_general.visitas:
        print("No hay visitas registradas en el hospital.")
        return

    print("Visitas registradas:")
    for i, visita in enumerate(hospital_general.visitas):
        print(i + 1, ".", visita.nombre, "(", visita.relacion, ") visitando a", visita.paciente.nombre)

    while True:
        try:
            visita_elegida = int(input("Elija el número de la visita a eliminar: ")) - 1
            if 0 <= visita_elegida < len(hospital_general.visitas):
                break
            else:
                print("Opción inválida. Elija un número de visita válido.")
        except ValueError:
            print("Ingrese un número válido.")

    visita = hospital_general.visitas.pop(visita_elegida)
    print("Visita de " + visita.nombre + " (" + visita.relacion + ") eliminada.")

#MENU
def menuprincipal():
    while True:
        print("Menu Principal")
        print("1. Agregar Paciente")
        print("2. Eliminar Pacientes")
        print("3. Agregar Visita")
        print("4. Eliminar Visita")
        print("5. Mostrar Más Información")
        print("6. Salir")
        opcion = int(input("Ingrese una opción: "))
        try:
            opcion = int(input("Ingrese una opción: "))
            break  
        except ValueError:
            print("Ingrese un número válido.")
        if opcion == 1:
            agregar_paciente()
        elif opcion == 2:
            eliminar_paciente()
        elif opcion == 3:
            agregar_visita()
        elif opcion == 4:
            eliminar_visita()
        elif opcion == 5:
            while True:
                print("Desea ver la Información de:")
                print("1. Pacientes")
                print("2. Visita")
                print("3. Doctores")
                print("4. Enfermeras")
                print("5. Edificios")
                print("6. Comidas")
                print("8. Volver al Menú Principal")
                opcion2 = int(input("Ingrese una opción: "))
                try:
                    opcion2 = int(input("Ingrese una opción: "))
                    break  
                except ValueError:
                    print("Ingrese un número válido.")
                
                if opcion2 == 1:
                    for paciente in hospital_general.pacientes:
                        paciente.mostrar_informacion() 
                        print("--------------------")
                elif opcion2 == 2:
                    for visita in hospital_general.visitas:
                        visita.informacion_visita()
                        print("--------------------")
                elif opcion2 == 3:
                    for personal in hospital_general.personal:
                        if isinstance(personal, Doctor):
                            personal.informacion_personal() 
                            print("--------------------")
                elif opcion2 == 4:
                    for personal in hospital_general.personal:
                        if isinstance(personal, Enfermera):
                            personal.informacion_enfermera()
                            print("--------------------")
                elif opcion2 == 5:
                    for edificio in hospital_general.edificios:
                        edificio.informacion_edificio()
                        print("--------------------")
                elif opcion2 == 6:
                    for comida in hospital_general.comidas:
                        comida.informacion_comida()
                        print("--------------------")
                elif opcion2 == 8:
                    break
                else:
                    print("Opción no válida.")
                    
        elif opcion == 6:
            break
        else:
            print("Opción no válida.")

menuprincipal()