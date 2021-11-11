import sys
import time
import drawShape
import fileOperations as fOps


# Run application: python ShapeOnTerminal.py terminal "./Data/json/shapesRequest.v4.json"
# Aritcle Reference: Great python snippets for day to day stuff: https://therenegadecoder.com/code/python-code-snippets-for-everyday-problems/
# Arielle 

def main():

    start_time = time.time()

    # Article Reference: https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
    print ("No. of arguments passed is {}".format(len(sys.argv)))

    for idx, arg in enumerate(sys.argv):
        if idx == 1:
            outputType = arg
            print("Argument #{} outpuType -> {}".format(idx, arg))
        elif idx == 2:
            filePath = arg
            print("Argument #{} filePath -> {}".format(idx, arg))

    if len(filePath)>0:
        processJsonRequests(filePath, outputType)

    else:
        print("Error: Json path not provided!")
        sys.exit(1)

    end_time = time.time()
    time_taken = end_time - start_time
    print("Time: #{}".format(time_taken))
    sys.exit(0)

def processJsonRequests(filePath, outputType):

    numOfShapes = 0 

    data = fOps.jsonReader(filePath)

    print('P1:')
    print(data)
    
    # Iterating through the json list
    for solicitude in data['Solicitudes']:
        
        nombre = solicitude['nombre'] 
        tipoDeEntrega = solicitude['tipoDeEntrega']
        correo = solicitude['correo'] 
        multipleFiles = solicitude['multipleFiles'] 
        allOrders = solicitude['orders']

        fileContent = ""

        j = 0
        for order in allOrders:

            print(order['shape'])

            j += 1
            cantidad = order['cantidad']
            lado = order['lado']
            centro = order['centro'] 
            ratio = order['ratio'] 
            shape = order['shape']
            # columnas = order['columnas']  

            if (multipleFiles == True):
                fileContent = ""
                fileName = "./Data/orders/" + nombre + "." + order['shape'] + ".order[" +  str(j) + "].txt"            
            else:
                fileName = "./Data/orders/" + nombre + ".txt"

            #producir e imprimir solo un shape en la pantalla
            #tempFileContent = Shaper.ShapeController(lado , centro, fill, outpuType, shape, flashOnScreen, ratio);

            tempFileContent = ""
            tempFileContent = drawShape.ShapeController(lado, centro, "", outputType, shape, ratio)
            print(tempFileContent)
            # fOps.writeToFile("./data/orders/finalShape.txt", tempFileContent)    
      
            for j in range(0, cantidad):

                #  acumular shapes
                fileContent += tempFileContent
                numOfShapes += 1

            fOps.writeToFile(fileName, fileContent)


                
    return ""

lado = ""
centro = ""
outputType = "web"
flashOnScreen = ""
filePath = ""

main()