import time

notas = []
porcentajes = []

def calcular_nota(notasl, porcentajesl):
    if len(notasl) != len(porcentajesl):
        return "El largo de notas no coincide al de porcentajes!!"
    total = 0
    for n, p in zip(notasl, porcentajesl):
        total += n*p
    return total

while True:
    print("""
    *-----------------------------*
    |                             |
    | 1. Agregar una nota         |
    | 2. Configurar porcentajes   | 
    | 3. Calcular notas           |
    | 4. Cuanto necesitas         |
    | 5. Salir                    |  
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
            nacumulado = sum(n*p for n, p in zip(notas, porcentajes))

            notadeseada = int(input("Ingrese la nota deseada: "))
            pfaltante = 0

            for p in porcentajes:
                pfaltante += p

            if pfaltante <= 0:
                print("Porcentaje máximo ya alcanzado(100%)")

            pacumulado = 1 - pfaltante
            puntosfaltantes = notadeseada - nacumulado
            notanecesaria = puntosfaltantes / pfaltante

            print(f"\n--- Resultados para nota objetivo: {notadeseada} ---")

            if notanecesaria <= 1.0:
                print("¡Ya aprobaste! Incluso sacando un 1.0 en todo lo que falta alcanzas tu meta.")
            elif notanecesaria > 7.0:
                print(f"Uf, matemáticamente imposible. Necesitarías promediar un {notanecesaria:.2f} en lo que falta.")
            else:
                print(
                    f"Necesitas promediar un **{notanecesaria:.2f}** en el {pacumulado * 100:.0f}% restante.")
            time.sleep(3)
        case 5:
            break
