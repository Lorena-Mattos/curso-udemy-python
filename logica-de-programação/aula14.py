# aprendendo usar a função format()
a = 'A'
b = 'B'
c = 1.1

string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
  nome1=a, nome2=b, nome3=c)
print(formato)

# nome3=c é chamado de parâmetro, tudo que vier depois de um parâmetro nomeado, PRECISA ser nomeado