def main():
    predictiveTable = {
        'E' : {
            'a' : "TQ",
            '(' : "TQ"},
        'Q' : {
            '+' : '+TQ',
            '-' : '-TQ',
            ')' : 'P',
            '$' : 'P'
        },
        'T' : {
            'a':'FR',
            '(': 'FR'
        },
        'R': {
            '+' : 'P',
            '-' : 'P',
            '*' : '*FR',
            '/' : '/FR',
            ')' : 'P',
            '$' : 'P'
        },
        'F' : {
            'a': 'a',
            '(': "(E)"
        }
}

    input = "(a+a)e$"
    stack = "$E"
    while input != '$':
        if(stack[-1] == input[0]):
            input = input[1:]
            stack = stack[:-1]
            continue
        try:
            tableLookup = predictiveTable[stack[-1]][input[0]]
        except:
                print("Not Valid input")
                print(stack)
                return 0
        
        if(tableLookup == 'P'):
            stack = stack[:-1]
            continue
        
        
        stack = stack[:-1]
        stack += tableLookup[::-1]
        

    print("Valid input!")
    print(stack)
    return 0

    


if __name__ == '__main__':
    main()