import json

def writeToFile(fileName, fileContent):
    try:
        file = open(fileName, "a")
        file.write(fileContent)
        file.close()
    except:
        print("Got an error trying to write to #{fileName}.")

def jsonReader(filePath):
    try:

        # Python program to read
        # json file

        # Opening JSON file
        f = open(filePath)

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Iterating through the json
        # list
        for i in data['Solicitudes']:
            
            print(i['nombre'])

            # print(i['tipoDeEntrega'])
            # print(i['correo'])
            # print(i['multipleFiles'])
            # print(i['numOfOrders'])
            #print(i)

        # Closing file
        f.close()
    except:
        print("Got an error trying to read to #{filePath}.")    
