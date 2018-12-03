
terms = input("Upto how many terms ? ");
if terms == 'x':
    exit();
else:
    term = int(terms);
    a = 0;
    b = 1;
    count = 2;
    print();
    if term == 0:
        print("Please enter a number...exiting...");
    elif term < 0:
        print("Please enter a positive number...exiting..");
    elif term == 1:
        print(a);
    else:
        print(a,",",b,end=",");
        while count < term:
            c = a + b;
            print(c,end=",");
            a = b;
            b = c;
            count = count + 1;
