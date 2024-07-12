import random
import math
import csv

#
trabajadores = [
    {"Nombre": "Juan Perez", "cargo": "Programador"},
    {"Nombre": "Maria Garcia", "cargo": "Consultor TI"},
    {"Nombre": "Carlos Lopez", "cargo": "Programador"},
    {"Nombre": "Ana Martinez", "cargo": "Jefa"},
    {"Nombre": "Pedro Rodriguez", "cargo": "Analista"},
    {"Nombre": "Laura Hernandez", "cargo": "Trabajadora"},
    {"Nombre": "Miguel Sanchez", "cargo": "Programador"},
    {"Nombre": "Isabel Gomez", "cargo": "Analista"},
    {"Nombre": "Francisco Diaz", "cargo": "Consultor"},
    {"Nombre": "Elena Fernandez", "cargo": "Trabajadora"}
]

#Sueldos: Aleatorio entre $250.000 y $2.500.000
#Definir con el nombre de asignar_sueldos
sueldos=[]
def asignar_sueldos():
    global sueldos
    sueldos=[random.randint(300000,2500000) for _ in range(10)]
    print("Sueldos asignados ")

def clasificar_sueldos():
    print(" Clasificación de sueldos:")
    for trabajador, sueldo in zip(trabajadores, sueldos):
        print("Sueldos menores a $800.000", len([s for s in sueldos if s <=800000]))
        if sueldo<800000:
            print(f"Nombre Empleado:{trabajador['Nombre']} Cargo:{trabajador['cargo']} Sueldo:${sueldo}")

        print("Sueldo entre $800.000 y $2.0000.000", len([s for s in sueldos if 800000<=s <=2000000]))
        if 800000<=sueldo<=2000000 :
            print(f"Nombre Empleado:{trabajador['Nombre']} Cargo:{trabajador['cargo']} Sueldo:${sueldo}")
        
        print("Sueldos superiores a $2.000.000", len([s for s in sueldos if s>2000000]))
        if sueldo >2000000 :
            print(f"Nombre Empleado:{trabajador['Nombre']} Cargo:{trabajador['cargo']} Sueldo:${sueldo}")
    print("Total de sueldos", sum(sueldos))

#Hacer menu de estadisticas
def estadisticas():
    sueldo_max= max(sueldos)
    sueldo_min=min(sueldos)
    sueldo_promedio= sum(sueldos)/ len(sueldos)
    sueldo_geom=math.exp(sum(math.log (sueldo)for sueldo in sueldos) /len(sueldos))
    print(f"El sueldo maximo es:${sueldo_max} ")
    print(f"El sueldo mas bajo es:${sueldo_min}")
    print(f"El sueldo promedio es:${sueldo_promedio:.2f}")
    print(f"La media geometrica de sueldos es:{sueldo_geom:.2f}")
    
    
#Cosas terminadas:
#Lista[Hecha]
#Asignaciones de sueldos[Hecho]
#Clasificación de sueldos[Hecho]
#Estadisticas[Hecho]
#Reporte de sueldos[Hecho]
#Regla de negocio(Salud, AFP, Sueldo liquido)[Hecho]
#Cosas que hacer:
#Finalización de programa[Por terminar]
#
def reporte_sueldos():
    with open('Reporte_de_sueldos.csv','w', newline='')as archivo:
        escribir= csv.writer(archivo)
        escribir.writerow(["Nombre empleado|", "Cargo|", "Sueldo Base|", "Descuento Salud|", "Descuento AFP|", "Sueldo Liquido"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            desc_salud= round(sueldo*0.07,2)
            desc_afp= round(sueldo*0.12,2)
            sueldo_liquido=sueldo-desc_afp-desc_salud
            escribir.writerow([trabajador["Nombre"], trabajador["cargo"],sueldo,desc_salud,desc_afp,sueldo_liquido])
            print(f"Nombre empleado:{trabajador['Nombre']}Cargo:{trabajador['cargo']}Sueldo base:${sueldo} ")
    print("Reporte generado correctamente!")
    
def menu():
    while True:
        print("1.- Asignar sueldos aleatorios.")
        print("2.- Clasificar sueldos.")
        print("3.- Ver Estadisticas.")
        print("4.- Generar reporte de sueldos")
        print("5.- Finalizar programa.")
        opc=int(input("Ingrese su opción\n>>"))
        match opc:
            case 1:
                asignar_sueldos()
            case 2:
                clasificar_sueldos()
            case 3: 
                estadisticas()
            case 4:
                reporte_sueldos()
            case 5:
                print("finalizando el programa...")
                print("Desarrollado por Joshua Martinez")
                print("Rut: 21.962.909-5")
                break


menu()