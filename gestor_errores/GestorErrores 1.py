# -*- coding: utf-8 -*-
class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            print "la pila esta vacia"
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

variables=[]


def postfijo(lista):
    print lista
    p=Pila()
    tam=len(lista)
    for x in range(tam):
        var=lista[x]
        if (esOperador(var)==True):
            print var
            p.apilar(int(operar(lista[x],p.desapilar(),p.desapilar())))
        if (esVariable(var)==True):
            pos=buscar(var)
            var=int(variables[pos+1])
            p.apilar(int(var))
            print pos
        else:
            if (esNumero(var)==True):
                p.apilar(int(var))
        
            
    return p.desapilar()

def esOperador(v):
    if v=="+":
        return True
    if v=="-":
        return True
    if v=="/":
        return True
    if v=="*":
        return True
    return False
    
def esNumero(v):
    return v.isdigit()

def esVariable(v):
    if (esNumero(v)==False):
        if (esOperador(v)==False):
            return True

    
def operar(o, y, x):
    if o=="+":
        z=x+y
    if o=="-":
        z=x-y
    if o=="*":
        z=x*y
    if o=="/":
        z=x/y
    return z

def agregarVariable(var,val):
    variables.append(var)
    variables.append(val)

def buscar(v):
    tam=len(variables)
    for i in range(tam):
        if v == variables[i]:
            return i

def comprobar(lista):
    tam=len(lista)
    if lista[tam-1]=='=':
        if esVariable(lista[tam-2])==True:
            agregarVariable(lista[tam-2], postfijo(lista[0:tam-2]))
        else:
            return "algún dato es erroneo"
            
def start ():
    f=open('algo.txt','r')
    lista=[y.split(' ') for y in [x.strip('\n') for x in (f.readlines())]]
    print lista
    for i in range(len(lista)):
        comprobar(lista[i])
    print variables    
start()
