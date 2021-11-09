def writeToFile(fileName, fileContent):
    try:
        file = open(fileName, "a")
        file.write(fileContent)
        file.close()
    except:
        print("Got an error trying to write to #{fileName}.")