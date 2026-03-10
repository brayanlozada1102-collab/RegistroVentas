from Registroventas import registro_ventas , mostrar_resumen

print("Bienvenido al sistema de registro de ventas ")
continuar = "si"
recaudo_diario = 0
ventas_dia = []
while continuar == "si":

 nombre_producto = input("Agregue el nombre del producto a añadir: ")
 cantidad = int(input("Agregue la cantidad del producto a añadir: "))
 valor_unitario = float(input("Agregue el valor unitario del producto a añadir: "))
 
 registro_ventas(nombre_producto,cantidad,valor_unitario,ventas_dia)
 
 recaudo_diario = recaudo_diario + (cantidad*valor_unitario)
 continuar = input("desea continuar registrando ventas? si/no: ")

mostrar_resumen(ventas_dia)
    
print(recaudo_diario)
        