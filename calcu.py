


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
          

def suma():
    digit = dig()
    res = 0
    for e in digit:
        res += e
    return res

def resta():
    digit = dig()
    res = digit[0]
    i = 0
    
    while i < len(digit):
        if i == 0:
            i += 1
        else:
            res -= digit[i]
            i += 1    
    return res

def mult():
    
    digit = dig()
    res = 1
    for e in digit:
        res *= e
    return res

def divi():
    digit = dig()
    res = digit[0]
    i = 0
    
    while i < len(digit):
        if i == 0:
            i += 1
        else:
            res /= digit[i]
            i += 1    
    return int(res)
    
def pot():
    print("Si quiere que la operacion solo tenga 1 exponente ")
    print("elija solo 2 digitos, los digitos ingresados despues ")
    print("del primero seran exponentes entre ellos")
    
    digit = dig()
    res = digit[0]
    i = 0
    
    while i < len(digit):
        if i == 0:
            i += 1
        else:
            res **= digit[i]
            i += 1    
    return res
       
def rc():
    print("Si quiere que la operacion solo tenga 1 radical ")
    print("elija solo 2 digitos, los digitos ingresados despues ")
    print("del primero seran radicales entre ellos")
    
    digit = dig()
    res = digit[0]
    i = 0
    
    while i < len(digit):
        if i == 0:
            i += 1
        else:
            res **= 1/digit[i]
            i += 1    
    return int(res)
    
    
    
     
            
print("W.I.P")    
  

def cal(c): 
    if c <=7:
        if c == 1 :
            return suma()
        elif c == 2 :
            return resta() 
        elif c == 3 :
            return mult()
        elif c == 4 :
            return divi()
        elif c == 5:
            return pot()
        elif c == 6:
            return rc() 
        elif c == 7:
            return

    else :
        print("el numero ingresado no es valido, por favor ingrese un numero entre el 1 y el 6")
        w = int(input())
        return cal(w)           
    return print(z)

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
    print (cal(c))


principal()