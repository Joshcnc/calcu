print("Elija la operacion a realizar")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")
print("5.Potencia o exponente")
print("6.Raiz")
### print("7.Deteccion de propiedad") ###  esto se hara ejecutable en futuras versiones
c = int(input("la operacion se elije insertando el numero que le corresponde "))
if c < 7:
    x = int(input("ingrese el primer digito"))
    y = int(input("ingrese el segundo digito"))
else:
    ### este else se eliminara o corregira en futuras versiones 
    print("el numero ingresado es incorrecto, favor reiniciar e ingresar el nnumero correcto")   
###if c == 7 :
   ### x = int(input("ingrese el p"))
    
if c == 1 :
    z = x + y
elif c == 2 :
    z = x - y 
elif c == 3 :
    z = x * y
elif c == 4 :
    z = x / y
elif c == 5:
    z = x ** y
elif c == 6:
  z =  int( x ** (1/y)   ) 
        
       
print (z)        