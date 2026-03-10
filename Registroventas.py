print("Bienvenido al sistema de registro de ventas")
continuar = "si"
recaudo_diario = 0
ventas_dia = []
while continuar == "si":

 nombre_producto = input("Agregue el nombre del producto a añadir: ")
 cantidad = int(input("Agregue la cantidad del producto a añadir: "))
 valor_unitario = float(input("Agregue el valor unitario del producto a añadir: "))
 def registro_ventas():
    actualizacion = {"nombre":nombre_producto,
         "cantidad vendida" : cantidad,
         "valor producto" : valor_unitario
         }
    ventas_dia.append(actualizacion)
 registro_ventas()
 
 recaudo_diario = recaudo_diario + (cantidad*valor_unitario)
 continuar = input("desea continuar registrando ventas? si/no: ")


def mostrar_resumen():
    for i in range(len(ventas_dia)):
        print(ventas_dia[i])
        print("--------------------")

mostrar_resumen()
    
print(recaudo_diario)
        
