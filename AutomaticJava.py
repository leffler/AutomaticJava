import os

def selectionMenu():
    print("Automatic Java Main Menu (and only menu for now...)")
    print("")
    print("+=+ Selection Menu +=+")
    print("1. Compile Program ")
    print("2. Run Program")
    print("3. Compile & Run Program ")
    print("4. Exit AutomaticJava ")
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
