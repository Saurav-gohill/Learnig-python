first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info,'\n')


num_int = 10
print('num_int:', num_int)
num_float = float(num_int)
print('num_float:', num_float,'\n')

# int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str,'\n')   

# str to list
first_name = 'Asabeneh'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)

for char in first_name_to_list:
    print(char, end='')

print('\n')

first_name = 'Asabeneh'
a=10
print(f"First name: {first_name}")
print(f"Value of a: {a}")

