"""
Do the full thing with formatting
"""
import hashlib
import random

######################### DO NOT MODIFY THE FUNCTIONS BELOW ###########################


def render_row(symbols):
    for i in range(4):
        if len(symbols) == 4:
            print('\t\t', end='')
        elif len(symbols) == 2:
            print('\t\t\t', end='')
        elif len(symbols) == 1:
            print('\t\t\t\t\t\t\t    ', end='')
        for j, symbol in enumerate(symbols):
            if j == len(symbols) / 2:
                print('\t', end='')
                if len(symbols) == 4:
                    print('\t\t\t\t', end='')
                elif len(symbols) == 2:
                    print('\t\t\t\t\t\t', end='')
            if symbol[i] == '0':
                print('* *\t\t', end='')
            else:
                print(' *\t\t', end='')
        print()


def render_single(symbol):
    for char in symbol:
        if char == '0':
            print('* *')
        else:
            print(' *')


def get_seed(s):
    return int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) % 10 ** 8


def draw_lines():
    def _draw_line():
        line = list()
        for i in range(10):
            if random.randint(0, 2):
                line.append(' ')
            else:
                line.append('-')
        return ''.join(line)

    return [_draw_line() for _ in range(4)]

############################## COMPLETE THE FUNCTIONS BELOW THIS LINE ###########################
def markings_to_symbol(lines):
    """
    Function that accepts four lines of markings and returns a binary symbol as in question 2
    :param lines: a list of four strings, where each string consists of lines and spaces
    :return: a string representing the binary encoding of the symbol
    """
    #TODO
    Binary=""
    count = 0
    for lines in lines:
        count = 0
        for char in lines:
            if char == '-':
                count = count + 1
        if (count % 2) == 0:
            Binary = Binary + "0"
        else:
            Binary = Binary + "1"
    return Binary

def generate_below(symbols):
    """
    Given four symbols, generate the two below it, and then the single one below those two. Reuse parts of question 5 to
    achieve this.
    :param symbols: a list of four binary-encoded symbols
    :return: a list of three binary encoded symbols - the two directly below the row of four (left to right) and then
    the single symbol
    """
    #TODO
    A=symbols[0]
    B=symbols[1]
    C=symbols[2]
    D=symbols[3]
    def Add(x,y):
        output=""
        for i in range(0,4):
            if x[i]==y[i]:
                output=output+"0"
            else:
                output=output+"1" 
        return output
    E=Add(A,B)
    F=Add(C,D)
    G=Add(E,F)

    NewList=[]
    NewList.append(E)
    NewList.append(F)
    NewList.append(G)
    return NewList

def rotate(symbols):
    """
    Given a list of four symbols, generate four more symbols by reading them sideways, as in Question 4.
    :param symbols: a list of four binary-encoded symbols
    :return: a list of four new symbols
    """
    #TODO
    x=symbols[0]
    y=symbols[1]
    z=symbols[2]
    w=symbols[3]

    def SideWays(x, y, z, w, i):
        output=""
        output=x[i]+y[i]+z[i]+w[i]
        return output
    NewList=[]
    for i in range(0,4):
        NewList.append(SideWays(x,y,z,w,i))
    return NewList

def generate_judge(symbol_1, symbol_2):
    """
    Generate the judge symbol by combining the two symbols given (as in Question 3)
    :param symbol_1: a binary-encoded symbol
    :param symbol_2: another binary-encoded symbol
    :return: the new symbol formed by combining the two given ones
    """
    #TODO
    output=""
    for i in range(0,4):
        if symbol_1[i]==symbol_2[i]:
            output=output+"0"
        else:
            output=output+"1" 
    return output

def generate_reconciler(symbols):
    """
    Generate the final symbol given a list of all symbols generated so far. The final symbol is a combination of the first
    and last symbol
    :param symbols: a list of all symbols
    :return: the final symbol
    """
    #TODO
    x=symbols[0]
    y=symbols[14]
    output=""
    for i in range(0,4):
        if x[i]==y[i]:
            output=output+"0"
        else:
            output=output+"1" 
    return output

def reorder_symbols(symbols):
    """
    Given the list of symbols in the order they were generated, reorder them so that they can be printed out
    from left to right one row at a time
    :param symbols: a list of all the symbols
    :return: a list of lists. Each element in the list is a row of symbols, and there should be five rows in total.
    The first row contains 8 symbols, the second 4, the third 2 and the fourth and fifth 1 each.
    """
    #TODO
    A=symbols[0]
    B=symbols[1]
    C=symbols[2]
    D=symbols[3]
    E=symbols[4]
    F=symbols[5]
    G=symbols[6]
    H=symbols[7]
    I=symbols[8]
    J=symbols[9]
    K=symbols[10]
    L=symbols[11]
    M=symbols[12]
    N=symbols[13]
    O=symbols[14]
    P=symbols[15]
    #NewList=[[K,J,I,H,D,C,B,A],[M,L,F,E],[N,G],[O],[P]]
    NewList=[[A,B,C,D,H,I,J,K],[E,F,L,M],[G,N],[O],[P]]
    return NewList
    
def show_table(symbols):
    """
    Given the list of symbols in the order they were generated, print out the table from Question 6.
    :param symbols: th elist of symbols.
    :return: no return
    """
    #TODO
    A=symbols[0]
    B=symbols[1]
    C=symbols[2]
    D=symbols[3]
    E=symbols[4]
    F=symbols[5]
    G=symbols[6]
    H=symbols[7]
    I=symbols[8]
    J=symbols[9]
    K=symbols[10]
    L=symbols[11]
    M=symbols[12]
    N=symbols[13]
    O=symbols[14]
    P=symbols[15]

    def SymbolTable(x):
        if x =="0000":
            output="People"
        elif x=="0001":
            output="Sorrow"
        elif x=="0010":
            output="White"
        elif x=="0011":
            output="Greater Fortune"
        elif x=="0100":
            output="Red"
        elif x=="0101":
            output="Gain"
        elif x=="0110":
            output="The Conjunction"
        elif x=="0111":
            output="Head of the Dragon"
        elif x=="1000":
            output="Joy"
        elif x=="1001":
            output="The Prison"
        elif x=="1010":
            output="Loss"
        elif x=="1011":
            output="The Girl"
        elif x=="1100":
            output="The Lesser Fortune"
        elif x=="1101":
            output="The Boy"
        elif x=="1110":
            output="Tail of the Dragon"
        elif x=="1111":
            output="The Way"
        return output

    HouseName=["Life","Riches","Brothers","Father","Sons","Health","Spouse","Death","Journeys","Kings","Good Fortune","Prison","Witness 1","Witness 2","Judge","Reconciler"]

    def Houselength(x):
        output=""
        if (len(HouseName[x])>=8):
            output = HouseName[x]+"\t"
        else:
            output = HouseName[x]+"\t\t"
        return output

    print("House\t\tName\t\tSymbol")
    print("1\t\t"+Houselength(0)+SymbolTable(K))
    print("2\t\t"+Houselength(1)+SymbolTable(J))
    print("3\t\t"+Houselength(2)+SymbolTable(I))
    print("4\t\t"+Houselength(3)+SymbolTable(H))
    print("5\t\t"+Houselength(4)+SymbolTable(D))
    print("6\t\t"+Houselength(5)+SymbolTable(C))
    print("7\t\t"+Houselength(6)+SymbolTable(B))
    print("8\t\t"+Houselength(7)+SymbolTable(A))
    print("9\t\t"+Houselength(8)+SymbolTable(M))
    print("10\t\t"+Houselength(9)+SymbolTable(L))
    print("11\t\t"+Houselength(10)+SymbolTable(F))
    print("12\t\t"+Houselength(11)+SymbolTable(E))
    print("13\t\t"+Houselength(12)+SymbolTable(N))
    print("14\t\t"+Houselength(13)+SymbolTable(G))
    print("15\t\t"+Houselength(14)+SymbolTable(O))
    print("16\t\t"+Houselength(15)+SymbolTable(P))
############################## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########################

question = input()
random.seed(get_seed(question))

initial_symbols = list()

for i in range(4):
    markings = draw_lines()
    initial_symbols.append(markings_to_symbol(markings))

left_symbols = generate_below(initial_symbols)
right_row = rotate(initial_symbols)
right_symbols = generate_below(right_row)
judge = generate_judge(left_symbols[-1], right_symbols[-1])
symbols = initial_symbols + left_symbols + right_row + right_symbols + [judge]
reconciler = generate_reconciler(symbols)
symbols.append(reconciler)

rows = reorder_symbols(symbols)

# print symbols nicely!
for i, row in enumerate(rows):
    if i != len(rows) - 1:
        render_row(row)
    else:
        render_single(row[0])
    print()

# show table from question 6
show_table(symbols)