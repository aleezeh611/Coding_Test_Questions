import sys

def textencode():
    curr_row = 0
    curr_col = 0
    toreturn = ""

    #Get the input from file using command line
    inFile = sys.argv[1]
    with open(inFile,'r') as i:
        lines = i.readlines()

    #Complete matrix storing each alphabet
    alphabets_matrix = [
        ['A', 'B', 'C', 'D', 'E' ],
        ['F', 'G', 'H', 'I', 'J' ],
        ['K', 'L', 'M', 'N', 'O' ],
        ['P', 'Q', 'R', 'S', 'T' ],
        ['U', 'V', 'W', 'X', 'Y'],
        ['Z']
    ]

    #Run a loop to go over all the words in the file
    for line in lines:
        nextlinechar = 0

        #Traverse across keyboard to get the code of each alphabet/letter
        for letter in line:
            #for each word start from 0,0 in matrix
            if letter == ' ':
                curr_col = 0
                curr_row = 0
                nextlinechar = 0

            #Code should work on multiple lines, when reading from file next line is written as /n so code should ignore that
            if letter == '/':
                nextlinechar += 1
                pass
            if nextlinechar == 1:
                if(letter == 'n'):
                    nextlinechar += 1
                    pass
                else:
                    nextlinechar = 0
            
            #get the row and columnof the letter we are looking for
            row = -1
            for i, matrixrow in enumerate(alphabets_matrix):
                if letter in matrixrow:
                    row = i
                    col = matrixrow.index(letter)

            #If letter was not found that means there are special characters which need to be ignored so if row -1 then not a letter
            if(row != -1):
                move_ver = curr_row - row
                move_hor = curr_col - col

                if move_ver < 0:
                    for i in range(abs(move_ver)):
                        toreturn += 'd'
                elif move_ver > 0:
                    for i in range(move_ver):
                        toreturn += 'u'
                if move_hor < 0:
                    for i in range(abs(move_hor)):
                        toreturn += 'r'
                elif move_hor > 0:
                    for i in range(move_hor):
                        toreturn += 'l'
                toreturn += '#'

                curr_row = row
                curr_col = col

    return toreturn


print(textencode())