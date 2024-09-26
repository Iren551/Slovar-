my_dict = {'Ira': 1989, 'Vanya': 1991, 'Katya': 1988}
print(my_dict)
print(my_dict['Ira'])
my_dict ['Vika'] = 1995
print(my_dict)
my_dict.update({'Max': 1985,
                'Alex': 1987})
del my_dict ['Katya']
print(my_dict)

my_set = {5 , 5, 'cat', 'cat', 4.6}
print(my_set)
my_set.update([7, 'dog'])
my_set.discard(5)
print(my_set)