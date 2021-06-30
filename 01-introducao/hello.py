print("Ola mundo!")

nome = "Anderson"
sobrenome = "Alves"

print ("Meu nome é", nome, "e meu sobrenome é", sobrenome)

x = 8
y = 2

print('x + y = ', x + y)
print('x - y = ', x - y)
print('x / y = ', x / y)
print('x * y = ', x * y)
print('x ** y = ', x ** y)

# Listas

nomes = ['Anderson', 'Regina']
nomes.append("Lúcia")
print('nomes', nomes)

nomesOrdenados = nomes.copy()
nomesOrdenados.sort()
print('nomes ordenados', nomesOrdenados)

nomes2 = ['Anderson', 'Regina', 'Lúcia']
print('nomes == nomes2', nomes == nomes2)
print('nomes is nomes2', nomes is nomes2)

nomes3 = nomes2

print('nomes2 is nomes3', nomes2 is nomes3)
nomes.clear();
print('nomes', nomes)
print('nomes2', nomes2)
print('nomes3', nomes3)

nomes2.append('Ademir')
print('nomes', nomes)
print('nomes2', nomes2)
print('nomes3', nomes3)