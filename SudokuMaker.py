from os import system, name

def grid(n):
    clear()
    print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
    print("║ " + n[0] + " │ " + n[1] + " │ " + n[2] + " ║ " + n[3] + " │ " + n[4] + " │ " + n[5] + " ║ " + n[6] + " │ " + n[7] + " │ " + n[8] + " ║")
    print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
    print("║ " + n[9] + " │ " + n[10] + " │ " + n[11] + " ║ " + n[12] + " │ " + n[13] + " │ " + n[14] + " ║ " + n[15] + " │ " + n[16] + " │ " + n[17] + " ║")
    print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
    print("║ " + n[18] + " │ " + n[19] + " │ " + n[20] + " ║ " + n[21] + " │ " + n[22] + " │ " + n[23] + " ║ " + n[24] + " │ " + n[25] + " │ " + n[26] + " ║")
    print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
    print("║ " + n[27] + " │ " + n[28] + " │ " + n[29] + " ║ " + n[30] + " │ " + n[31] + " │ " + n[32] + " ║ " + n[33] + " │ " + n[34] + " │ " + n[35] + " ║")
    print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
    print("║ " + n[36] + " │ " + n[37] + " │ " + n[38] + " ║ " + n[39] + " │ " + n[40] + " │ " + n[41] + " ║ " + n[42] + " │ " + n[43] + " │ " + n[44] + " ║")
    print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
    print("║ " + n[45] + " │ " + n[46] + " │ " + n[47] + " ║ " + n[48] + " │ " + n[49] + " │ " + n[50] + " ║ " + n[51] + " │ " + n[52] + " │ " + n[53] + " ║")
    print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
    print("║ " + n[54] + " │ " + n[55] + " │ " + n[56] + " ║ " + n[57] + " │ " + n[58] + " │ " + n[59] + " ║ " + n[60] + " │ " + n[61] + " │ " + n[62] + " ║")
    print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
    print("║ " + n[63] + " │ " + n[64] + " │ " + n[65] + " ║ " + n[66] + " │ " + n[67] + " │ " + n[68] + " ║ " + n[69] + " │ " + n[70] + " │ " + n[71] + " ║")
    print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
    print("║ " + n[72] + " │ " + n[73] + " │ " + n[74] + " ║ " + n[75] + " │ " + n[76] + " │ " + n[77] + " ║ " + n[78] + " │ " + n[79] + " │ " + n[80] + " ║")
    print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")

def gridExport(n):
    f=open("puzzle.txt", "w+")
    for i in range(0, 81):
        f.write(str(n[i]))
    f.close
    print("\033[1;32;49mExport Successful!\033[0;0;0m")

def gridImport(arr):
    f=open("puzzle.txt", "r")
    arr.clear()
    try:
        #print("Opened file...")
        #print("arr length = " + str(len(arr)))
        for i in f:
            for y in i:
                if isValidNum(str(y)):
                    arr.append(str(y))
                #print("Appended" + str(y))
        #print("Returning array")
        #print("arr length = " + str(len(arr)))

        if len(arr) != 81:
            arr.clear()
            manualFill(arr)
        f.close()
        return arr
    except:
        f.close()
        manualFill(arr)
        return arr
    
def isValidNum(a):
    try:
        int(a)
    except:
        if a == " ":
            return True
        else:
            return False
    if int(a) != 0:
        return True
    else:
        return False

##def fillNums(arr):
##    print("Enter 81 numbers")
##    for i in range(0,82):
##        x = True
##        while x == True:
##            num = input("> ")
##            if isValidNum(num):
##                arr.append(num)
##                x = False
##            else:
##                print("Not a valid value, enter only a number between 1-9, or a space")
##    return arr

def manualFill(arr):
    row = 1
    while len(arr) < 81:
        print("Enter Row " + str(row) + " (9 numbers, or spaces)")
        inp = input("> ")
        if len(inp) == 9:
            for i in inp:
                if isValidNum(i):
                    arr.append(i)
                else:
                    print("All digits not valid")
                    break
            row = row + 1
        else:
            print("Invalid input, enter 9 numbers between 1-9 (or spaces)")
    return arr

def fillNums(arr):
    #print("fillnums")
    x = " "
    while x != "y" or x != "n":
        x = input("Import puzzle? (y/n)")
        if x == "y":
            arr = gridImport(arr)
            return arr
        elif x == "n":
            arr = manualFill(arr)
            return arr
        
                                    
##def edit(arr):
##    n = True
##    o = True
##    while n == True:
##        while o == True:
##            select = input("Select a cell in the format r#c## where the third number is your change, or e to exit edit mode\n> ")
##            if select == "e":
##                o = False
##                return arr
##
##            try:
##                x = int(select[1])
##                y = int(select[3])
##            except:
##                "Invalid selection, try again"
##            z = int(select[-1])
##            
##            cell = 9*(x-1) + (y-1)
##
##            arr[cell] = str(z)
##
##            n = False
##            grid(arr)
##        
##        return arr            
##            
##    print("null")
##    return null

def edit(arr):
    grid(arr)
    loop = True
    while loop == True:
        select = input("Select a cell in the format r#c## where the third number is your change, or e to exit edit mode\n> ")

        if select == "e":
            return arr
        else:
            try:
                x = select[1]
                y = select[3]
                z = str(select[-1])
            except:
                x = 10
                y = 10
                z = "f"

            if isValidNum(z):
                try:
                    cell = 9*(int(x)-1) + (int(y)-1)
                    arr[cell] = z
                    grid(arr)
                    
                except:
                    print("Invalid cell, select again (or e to exit)")
            else:
                print("Invalid value, enter a number between 1-9 or a space (or e to exit)")
    

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    

def main():
    numarray = list()
    numarray = fillNums(numarray)
    grid(numarray)
    x = True
    print("\nExit = e, Edit = d, Export = x, Import = i")
    while x == True:
        choice = input("> ")
        if choice == "d":
            numarray = edit(numarray)
            print("\n\n\n")
            grid(numarray)
            print("\nExit = e, Edit = d, Export = x, Import = i")
        elif choice == "e":
            x = False
        elif choice == "x":
            gridExport(numarray)
        elif choice == "i":
            gridImport(numarray)
            grid(numarray)
            print("\033[1;32;49mImport successful!\033[0;0;0m")
            print("\nExit = e, Edit = d, Export = x, Import = i")
    

main()

