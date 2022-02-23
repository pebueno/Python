dictionary = {'name':"Danilo", 'age': 36, 'height': 1.80, 'fruits':['maça', 'banana']} # Criação do dicionário
me = {'name': 'Pedro', 'age': '25', 'address': 'Sao Paulo', 'height': '1.80'}
print(dict(me))
print(type(me))
print(dictionary['name'])
dictionary['name'] = "Marcelo"
del dictionary['name']
dictionary.pop('height', None)

print(dictionary)
# dictionary1 = {'feira':['banana', 'maça', 'uva'], 'name': 'Danilo'}
# lista = ["Danilo", 35, 1.80] 
# dictionary['cpf'] = 40454545 # Adicionando um novo item
# dictionary.pop('height', None) # Remoção
# del dictionary['age'] # Remoção
# print(dictionary)
# print(dictionary1)
# print(dictionary['name'], dictionary['cpf'] )