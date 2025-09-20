
descuento=15
def calcular_descuento(monto, descuento):
    #print(f"¡monto, {monto}!")
    #print(f"¡descuento, {descuento}!")
    valor_descuento=monto*(descuento/100) #calculo del valor del descuento utilizando los parametros del monto y parametros que envia la funcion
    #print(f"¡descuento, {valor_descuento}!")
    return valor_descuento

descuento1=calcular_descuento(2500,descuento) #llamada 1 monto total de la compra
descuento2=calcular_descuento(5000,12) #llamada 2 monto total de la compra como el porcentaje de descuento
print(descuento1)
print(descuento2)


