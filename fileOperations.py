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

        # Closing file
        f.close()
        return data
    except:
        print("Got an error trying to read to #{filePath}.")    
