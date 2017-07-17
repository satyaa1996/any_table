no = input("Enter a No.: ")
mul = 1
try :
    no = int(no)
    while mul <= 10 :
        tbl = no * mul
        print (tbl)
        mul = mul + 1

except :
    while True:
        print ("invalid input")
        no = input("Enter a Valid No. : ")
        try :
            no = int(no)
            mul = 1
            while mul <= 10 :
                tbl = no * mul
                print (tbl)
                mul = mul + 1
            break    
        except :
            continue
