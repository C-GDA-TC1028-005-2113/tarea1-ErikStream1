def main():

    #PROMEDIO DE 4 MATERIAS
    
    import math

    c1=float(input("Calificación de la materia: "))
    c2=float(input("Calificación de la materia: "))
    c3=float(input("Calificación de la materia: "))
    c4=float(input("Calificación de la materia: "))

    cals=[c1,c2,c3,c4]

    prom=(math.fsum(cals))/4
    print("El promedio es: "+ str(prom) )

if __name__ == '__main__':
    main()
