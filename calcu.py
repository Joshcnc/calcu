
def principal():
    print("Elija la operacion a realizar")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    print("5.Potencia o exponente")
    print("6.Raiz")
    ### print("7.Deteccion de propiedad") ###  esto se hara ejecutable en futuras versiones
    c = int(input("la operacion se elije insertando el numero que le corresponde "))
    

def dig():
    i = 1
    x = int(input("ingrese la cantidad de digitos"))
    if x > 10:
        print("El numero de digitos es muy alto, quiere continuar de todos modos?")
        print("1.Si")
        print("2.No")
        conf = int(input())
        if conf > 2 or conf <1:
            print("Confirmacion incorrecta, reiniciando numero de digitos")
            return dig()
        elif conf == 2:
            print("Confirmacion denegada, Reiniciando eleccion")
            return dig()
        else:
            dig_list = []
            while i <= x:
                y = int(input("ingrese su digito "))
                dig_list.append(y)
                i += 1
    else:             
        dig_list = []
        while i <= x:
            y = int(input("ingrese su digito "))
            dig_list.append(y)
            i += 1                 
    return dig_list            
            
            
    
    

def cal(c): 
    if c <=7:
        x = int(input("ingrese el primer digito "))
        y = int(input("ingrese el segundo digito "))
        
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
        z =  int( x ** (1/y) ) 
    elif c == 7:
        return

    else :
        print("el numero ingresado no es valido, por favor ingrese un numero entre el 1 y el 6")
        w = int(input())
        return cal(w)           
    return print(z)

print(dig())