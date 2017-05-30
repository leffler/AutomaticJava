import os

def selectionMenu():
    print("AutomaticJava Main Menu (and only menu for now...)")
    print("")
    print("+=+ Selection Menu +=+")
    print("|+|Compile Program-Option 1: ")
    print("|+|Run Program-Option 2: ")
    print("|+|Compile & Run Program-Option 3: ")
    print("|+|Exit AutomaticJava-Option 4: ")
    print("")

def compileProgram():
    print("Compiling your program...")
    compileCommand = "javac " + fileName
    os.system(compileCommand)

def runProgram():
    "Running your program..."
    fileNameNoExt = fileName[:len(fileName) - 5]
    runCommand = "java " + fileNameNoExt
    os.system(runCommand)

menuOpen = True
fileName = input("Name of file(include extension): ")
while menuOpen == True:
    selectionMenu()
    selection = int(input("Select an option: "))

    if selection == 1:
        compileProgram
    elif selection == 2:
        runProgram()
    elif selection == 3:
        compileProgram()
        runProgram()
    elif selection == 4:
        menuOpen = False
        print("GoodBye")
    else:
        print("invalid input")
