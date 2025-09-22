tiene_boleto = False
edad = 15

if tiene_boleto:
    print("Verificación de boleto: OK.")
    if edad >= 18:
        print("Verificación de edad: OK.")
        print("Acceso permitido al área restringida.")
    else:
        print("Verificación de edad: Fallida.")
        print("Acceso denegado. No cumples con la edad mínima.")
        
else:
    print("Acceso denegado. No tienes boleto.")
