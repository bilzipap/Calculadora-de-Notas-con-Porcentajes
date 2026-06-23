import time

notas = []
porcentajes = []

def calcular_nota(notas, porcentajes):
    if len(notas) != len(porcentajes):
        return "El largo de notas no coincide al de porcentajes!!"
    total = 0
    for nota, porcentaje in zip(notas, porcentajes):
        total += nota*porcentaje
    return total

while True:
    print("""
    *-----------------------------*
    |                             |
    | 1. Agregar una nota         |
    | 2. Configurar porcentajes   | 
    | 3. Calcular notas           |
    | 4. Salir                    |  
    |                             |
    *-----------------------------*
    """)
    opcion = int(input("¿Qué deseas hacer?: "))
    match opcion:
        case 1:
            try:
                nuevanota = int(input("Indique su nota: "))
                notas.append(nuevanota)
                porcentaje = float(input("Indique su porcentaje(Formato: 0.3): "))
                porcentajes.append(porcentaje)
                print(f'Nota: {nuevanota} \nPorcentaje: {porcentaje}')
                time.sleep(3)
            except ValueError:
                print("Ingresa tu nota como un valor entero")
                time.sleep(2)
        case 2:
            count = 0
            for nota, porcentaje in zip(notas, porcentajes):
                count += 1
                print(f'{count}. {nota}: {porcentaje}%')
            confp = int(input(f'Cual es el porcentaje que quieres configurar?(Indicar por indice): '))
            try:
                porcentajes[confp - 1] = float(input("Ingresa nuevo porcentaje(Formato: 0.3/0.35): "))
            except IndexError:
                print("Indice seleccionado fuera del rango")
        case 3:
            print(f"Tu promedio es: {calcular_nota(notas, porcentajes)}")
            count = 0
            print("Con estas notas:")
            for nota, porcentaje in zip(notas, porcentajes):
                count += 1
                print(f'{count}. {nota}: {porcentaje}%')

            time.sleep(3)
        case 4:
            break