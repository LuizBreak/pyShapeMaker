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
    fOps.jsonReader(filePath)
    finalShape = drawShape.ShapeController("*", "+", "", outputType, "Square", 1)
    print(finalShape)
    fOps.writeToFile("./data/orders/finalShape.txt", finalShape)
    return ""

lado = ""
centro = ""
outputType = "web"
flashOnScreen = ""
filePath = ""

main()