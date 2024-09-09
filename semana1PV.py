def calcular_pago():
    costo_nutricion = 10000
    costo_estetica = 5000

    estudios_nutricion = int(input("Ingrese la cantidad de estudios de Nutrición que desea: "))
    estudios_estetica = int(input("Ingrese la cantidad de estudios de Estetica que desea: "))

    total_nutricion = estudios_nutricion * costo_nutricion
    total_estetica = estudios_estetica * costo_estetica
    total = total_nutricion + total_estetica

    descuento = 0
    total_con_descuento = total
    if total > 80000:
        descuento = total * 0.2
        total_con_descuento = total - descuento
    else:
        total_con_descuento = total

    print(f"\nDetalle del pago para el paciente:")
    print(f"Total estudios de Nutrición: {total_nutricion} pesos")
    print(f"Total estudios de Estética: {total_estetica} pesos")
    print(f"Total sin descuento: {total} pesos")
    print(f"Descuento aplicado: {descuento} pesos")
    print(f"Total con descuento:  {total_con_descuento} pesos")

 
if __name__ == "__main__":
        calcular_pago()