barcode = input("Type your 13 digit barcode number, or type x to exit: ")
while barcode != "x":
    total = 0
    
    #ensure correct length
    if len(barcode) != 13:  
        print("Invalid length")
        barcode = input("Type 13 digit barcode here: ")
        
    #ensure the barcode contains only numbers    
    try:                    
        barcode_int = int(barcode)
    except:
        print("Barcode should be all digits, and have no spaces")
        print()
        barcode = input("Type your 13 digit barcode number here: ")
        
    #adding the odd digits 
    for digit in barcode[0:13:2]:
        total += int(digit)
        
    #adding the even digits
    for digit in barcode[1:12:2]:
        total += 3 * int(digit)
        
    #calculate if valid and print result
    if total%10 == 0:
        print("Valid barcode")
    else:
        print("Invalid barcode")

    #repeat
    print()
    barcode = input("Type your 13 digit barcode number, or type x to exit: ")
    
