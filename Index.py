import math
class Index:
    gValues = [[]]
    yValues = []
    
    if __name__ == "__main__":
        
        pass

    @staticmethod
    def valueAtFuncton1(postion,variables):
        y = (postion**2)*variables[2] + postion*variables[1] + variables[0]
        return y

    @staticmethod
    def valueAtFunction2(postion,variables):
        y = variables[0]*Index.getGValue(postion,0) + variables[1]*Index.getGValue(postion,1) + variables[2]*Index.getGValue(postion,2) + variables[3]*Index.getGValue(postion,3)
        return y
        
    @staticmethod
    def readGDataFromFile(path,position):
        file = open(path,"r")
        line = file.readline()
        separetedValues = line.split("|")
        count = 0
        for x in separetedValues:
            Index.gValues[position][count] = x
            count += 1


    @staticmethod
    def getGValue(position,nfunction):
        paths = []
        if Index.gValues == None:
            Index.readGDataFromFile(paths[nfunction],nfunction)
        return Index.gValues[nfunction][position]
        

    @staticmethod
    def valueAtFunction3(position,variables):
        y = variables[0] + variables[1]*math.sin((math.pi/100)*position) + variables[2]*math.cos((math.pi/100)*position)
        return y

    @staticmethod
    def readYDataFromFile():
        file = open("path","r")
        line = file.readline()
        separetedValues = line.split("|")
        count = 0
        for x in separetedValues:
            Index.yValues[count] = x
            count += 1

    @staticmethod
    def distance(original,compared):
        return (original-compared)


