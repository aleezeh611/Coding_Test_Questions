import sys


#===============================================================================
#                               UTILITY FUNCTION
#===============================================================================
def formatContactNumber(num):
    format_num = num.replace(' ', "")
    format_num = format_num.replace('+', "")
    format_num = format_num.replace('-', "")
    format_num = format_num.replace('(', "")
    format_num = format_num.replace(')', "")
    return format_num

def numberToWord( dup):
    if dup == 1:
        return 'double'
    if dup == 2:
        return 'triple'
    if dup == 3:
        return  'quadruple'
    if dup == 4:
        return  'quintuple'
    if dup == 5:
        return  'sextuple'
    if dup == 6:
        return 'septuple'
    if dup == 7:
        return  'octuple'
    if dup == 8:
        return  'nonuple'
    if dup == 9:
        return  'decuple'
    else:
        return ""

def format_Number(num):
    str_num = ""
    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]

    dup = 0
    count = 0
    prevnum = 9999

    for i in num:
        count += 1

        if i == prevnum:
            dup += 1
            if count == len(num):
                word = numberToWord( dup)
                if word != "":
                    str_num += word + " "
                    str_num += single_digits[int(i)]
                else:
                    for j in range(dup+1):
                        if(j != dup):
                            str_num += single_digits[int(i)] + " "
                        else:
                            str_num += single_digits[int(i)]

        else:
            if dup > 0 and dup <= 10:
                str_num += numberToWord(dup) + " "
                str_num += single_digits[int(prevnum)] + " "
            elif dup > 10:
                for j in range(dup+1):
                    str_num += single_digits[int(prevnum)] + " "
            
            dup = 0
            if i != " " and i != '-' and i != '(' and i != ')' and i != '+':
                prevnum = i
                if count < len(num):
                    if num[count] != i :
                        str_num += single_digits[int(i)] + " "
                else:
                    str_num += single_digits[int(i)]
            else:
                prevnum = 9999

    return str_num

def format_Number2(num, first_space):
    str_num = ""
    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
    dup = 0
    count = 0
    prevnum = 9999
    for i in num:
        count += 1
        if i == prevnum and count != first_space+1:
            dup += 1
            if count == len(num):
                word = numberToWord( dup)
                if word != "":
                    str_num += word + " "
                    str_num += single_digits[int(i)]
                else:
                    for j in range(dup+1):
                        if(j != dup):
                            str_num += single_digits[int(i)] + " "
                        else:
                            str_num += single_digits[int(i)]

        else:
            if dup > 0 and dup <= 10:
                str_num += numberToWord( dup) + " "
                str_num += single_digits[int(prevnum)] + " "
            elif dup > 10:
                for j in range(dup+1):
                    str_num += single_digits[int(prevnum)] + " "

            dup = 0
            if count == (first_space):
                prevnum = 99999
            else:
                prevnum = i

            if count < len(num):
                if num[count] != i or count == first_space:
                    str_num += single_digits[int(i)] + " "
            else:
                str_num += single_digits[int(i)]
   
    return str_num

#===============================================================================
#                           MAIN FUNCTION
#===============================================================================
def googleassisstant():
    
    #Get the input from file using command line
    inFile = sys.argv[1]
    lines = open(inFile,'r').read().splitlines()

    store_num = []
    todisplay = {}
    for i in range(int(lines[0])):
        format_num = formatContactNumber(lines[i+1])
        if ')' in lines[i+1]:
            first_space = lines[i+1].index(')')
            first_space-=1
        elif ' ' in lines[i+1]:
            first_space = lines[i+1].index(' ')
        elif '-' in lines[i+1]:
            first_space = lines[i+1].index('-')
        else:
            first_space = -1
        format1 = format_Number(lines[i+1])
        format2 = format_Number2(format_num, first_space)
        if format1 not in store_num:
            store_num.append(format1)
            if format1 == format2:
                if format_num not in todisplay:
                    todisplay[format_num] = []
                todisplay[format_num].append(format1)
            else: 
                store_num.append(format2)
                if format_num not in todisplay:
                    todisplay[format_num] = []
                todisplay[format_num].append(format1)
                todisplay[format_num].append(format2)
        
    for i in todisplay:
        print(i)
        for j in todisplay[i]:
            print(j)

googleassisstant()
