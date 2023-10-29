d={
    'first name':'tanmay',
    'second name':'khatri',
    'qualifiaction':'btech',
    'branch':'computer science'
}
# print(d['first name'])
# for a in d:
    # print(a,":",d[a])
# print(d.get('first name'))
# print(type(d))

# dictionary function
    #get()
# a=d.get('first name')  # get() for print the value of the dictionary via keys
# print(a)


    # keys() : for print the keys of the dictionary
# a=d.keys()
#  or
# for a in d.keys():
    # print(a)


   #values() : for print the all values of the dictionary
# a=d.values()
   # or
# for a in d.values():
    # print(a)



    # items()  : for print the keys and values of the dictionary
# a=d.items()
   # or
# for a,b in d.items():
#     print(a,":",b)


    # del
# del d['first name']
# print(d)



   # pop()
# print(d.pop('first name'))
# print(d)


  # dict()  : use for create the dictionary
# a=dict(firstname='tanmay',
#     secondname='khatri',
#     age=21)
# print(a)


  # update()  : for update the dict
# d.update({'branch':'CSE'})
# print(d)



  #clear()
# d.clear()
# print(d)


  #insert
# d['age']=22
# print(d)


 # nested dictionary
course={
    'php':{'duration':'2 months','fees':15000},
    'java':{'duration':'2 months','fees':15000},
    'python':{'duration':'2 months','fees':15000}
}
# print(course)
  #get
# a=course.get('php')
# print(a)
# print(course['php']['fees'])



# update
# course.update( {'php':{'duration':'2 months','fees':10000}})
# print(course)
 # or
# course['java']['fees']=5000
# print(course)

#insert

# course['javascript']= {'duration':'2 months','fees':15000}
# print(course)


  #pop()
# course.pop('php')
# print(course)


  #items()
# for k,v in course.items():
#     print(k,v['duration'],v['fees'])