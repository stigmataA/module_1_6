my_dict = {'Den': 1978, 'Alex': 1980, 'Max': 2012}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Olga'))
my_dict. update({'Yan': 2001, 'Ben': 1999})
del my_dict['Den']
print(my_dict)

my_set = {1, 2, 3, 1, 5, 'string', True, 2}
print(my_set)
my_set.update({23, 'list'})
print(my_set. discard(3))
print(my_set)