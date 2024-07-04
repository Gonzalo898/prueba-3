import os
os.system ("cls")
persona=[]


def grabar_datos():
    print("GRABAR DATOS")
    try :
        v_totaldeusuarios=None
        v_nif= input("ingrese su NIF :")    
        v_nombre=input("ingrese su nombre :")
        v_edad=int(input("ingrese sus edad :"))
        v_totaldeusuarios=(v_nif, v_nombre, v_edad)
        persona.append(v_totaldeusuarios)
        
    except:
        op=0
        
    #end try      
#end def grabar persona 

def buscar_persona():
    print("BUSCAR PERSONA")
    print(persona)

#end def buscar persona

def imprimir_certificado():
    
    print("IMPRIMIENDO CERTIFICADOS")
    
#end def imprimir certificado

def salir ():
    print('''
          saliendo del programa con exito
          Gonzalo Diaz
          ''')
    


while True:
    print('''
          1.-grabar datos personas con un nif : 
          2.-buscar a una persona por su nif  :
          3.-imprimir certificado :
          4.-salir :
        
          ''')
    
    try:
        op=int(input("escoge una opcion :"))
    except:
        op=0
    #end try
    if op < 1 or op > 4 :
        print("opcipn no valida")
    else:
        if op == 1:
            grabar_datos()
        elif op == 2 :
            buscar_persona()
        elif op == 3:
            imprimir_certificado()
        else:
            salir()
            break
        #fin if
    #fin if
#fin while
             
        