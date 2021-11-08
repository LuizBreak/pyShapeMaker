import random
import sys
import os


def ShapeController(c1, c2, c3, outputType, shapeType, Ratio):
    return ""

def MakeCross(c1, c2, outputType, ratio):
    return ""

def MakeDiamond(c1, c2, outputType, ratio):
    return ""


def MakeSquare(c1, c2, outputType, ratio):

    columnas = round(24 * ratio)
    rows     = round(columnas * 0.25)
    tamanoDelCentro = round(columnas * 0.50)    # de columnas dentro del shape
    lateral = round(columnas * 0.25);              # de columnas afuera del shape

    Shape = ""
    lineFeed = "\n"

    CUERPOFINAL = (lateral * 2 + tamanoDelCentro)   

    if columnas < CUERPOFINAL:
        columnas = CUERPOFINAL
    elif columnas > CUERPOFINAL:
        tamanoDelCentro += (columnas - CUERPOFINAL) 

    
    headerFooter = Centro(columnas + 2, c1 ) +  lineFeed
    aperturaCierre = Izquierda(lateral, c1)  + Centro(tamanoDelCentro +2, "-") +  Derecha(lateral, c1) + lineFeed
    cuerpo = Izquierda(lateral, c1) + "|" + Centro(tamanoDelCentro, c2) + "|" + Derecha(lateral, c1) + lineFeed
  
    
    if outputType == "web":
        lineFeed = "<br>"
    else: 
        lineFeed = "\n"   
      
    limite = round((rows*2) * 0.3)
    limiteDeAbajo = rows*2 - limite

    Shape = "ratio: " + str(ratio)  +  ", columnas: " + str(columnas)  + ", rows: " +  str(rows * 2)  + ", lateral: " +  str(lateral)  + ", tamanoDelCentro: "  + str(tamanoDelCentro) +  ", limite: " + str(limite)  + lineFeed

    for i in range(0, rows*2):
     
        # Header de arriba
        if  i < limite - 1:
            Shape += headerFooter

        # limite de arriba
        # Apertura del Cuadrado
        elif (i == limite -1):
            Shape += aperturaCierre
            
        # Cierre del Cuadrado
        elif (i == limiteDeAbajo):
            Shape += aperturaCierre

        # limite de abajo
        elif ( i > limiteDeAbajo):
            Shape += headerFooter
        
        # Cuerpo del Cuadrado 
        else:
            Shape += cuerpo

        GetLineFeed(outputType)
       
    return Shape

def Makerhombus(c1, c2, outputType, ratio):
    return ""

def MakeEnvelope(c1, c2, outputType, ratio):
    return ""

def GetLineFeed (outputType):
    return ""

def Izquierda(Tamano, CaracterDeseado):
    return CaracterDeseado * Tamano

def Centro(Tamano, CaracterDeseado):
    return CaracterDeseado * Tamano

def Derecha(Tamano, CaracterDeseado):
    return CaracterDeseado * Tamano

def PonerLetras(Tamano, LetraDeseada):
    return LetraDeseada * Tamano