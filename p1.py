print("hello world")
a=12
a+=12 # Assignment operatot
b=13
print(a,b)
print(id(a),id(b))
print(a+b) # Arthemetic operator
print(a==b) # Comparison operator
if(a>13 and b>14): # Logical operator

    print("true")
else:
    print("false")

if(a>13 or b>14): # logical operatator
    print("true")
    # in , not in : is the membership operator
    str="hello"
    print("y" in str ) # membership operator
    print("h" not in str)

    x=12
    y=13
    print(x is y) # identify operator : is , is not
    str1='''
    hello
    tanmay
    '''
    print(str1 , type(str1))


    l1=[1,2,3,'w1'] # list : we can change the data in the list after the initilization
    l1[2]=1
    print(l1)

    t1=(1,2,3,4,'w1') # tuple: we cannot change the data after the initilization
    # t1[0]=12
    print(t1)

    d1={'name':'tanmay',
        'age':'12',
        'city':'meerut'}  # dictionary
    d1[0]={'name':'rahul'}
    print(d1['name'])
    print(d1)


    set_1={'1','2','2','3'} # set : it removes duplicate data types automatically
    print(set_1)