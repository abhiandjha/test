largest = None
smallest = None

while True:
    try:
        num = input("Enter a number : ")
        if num == 'done':
            break
        n = int(num)
        largest = num if largest < num or largest == None else largest
        smallest = num if smallest > num or smallest == None else smallest 
    except:
        print("Enter a valid input")

print ("Maximum number is ", largest)
print ("Minimum number is ", smallest)