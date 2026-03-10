
def registro_ventas(nombre_producto,cantidad,valor_unitario,ventas_dia):
    actualizacion = {"nombre":nombre_producto,
         "cantidad vendida" : cantidad,
         "valor producto" : valor_unitario
         }
    ventas_dia.append(actualizacion)

def mostrar_resumen(ventas_dia):
    for i in range(len(ventas_dia)):
        print(f"{ventas_dia[i]['nombre']} \ncantidad vendida: {ventas_dia[i]['cantidad vendida']} \nprecio por unidad vendida: ${ventas_dia[i]['valor producto']}")
        print("--------------------")