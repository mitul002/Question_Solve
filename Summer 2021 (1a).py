def check():
    day=str(input())
    if day == 'Friday':
        print('Today is holiday')
    else:
        print('Working day')


lst = ['Saturday','sunday','Tuesday','Thursday','Friday']
lst.insert(2,'Monday')
lst.insert(4,'Wednesday')


for i in lst:
  check()