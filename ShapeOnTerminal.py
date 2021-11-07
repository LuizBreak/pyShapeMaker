import sys

# Run application: python ShapeOnTerminal.py terminal "./Data/json/shapesRequest.v4.json"

def main():
    # Article Reference: https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
    print ("No. of arguments passed is {}".format(len(sys.argv)))

    for idx, arg in enumerate(sys.argv):
        if idx == 2:
            outpuType = arg
            print("Argument #{} outpuType -> {}".format(idx, arg))
        elif idx == 3:
            filePath = arg
            print("Argument #{} filePath -> {}".format(idx, arg))

    if len(filePath)>0:
        processJsonRequests(filePath, outputType)
        sys.exit(0)
    else:
        print("Error: Json path not provided!")
        sys.exit(1)

def processJsonRequests(filePath, outputType):
    return ""

lado = ""
centro = ""
outputType = "web"
flashOnScreen = ""
filePath = ""

main()