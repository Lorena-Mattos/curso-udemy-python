# Fazendo debug de código, clica na setinha de run e escolhe debug python file, não alterar configurações
# seleciona ao lado dos números que aparecem ao lado do código o breakpoint, clica na seta ver no painel esquerdo
# feito isso, aparecerar uma setinha circular, que significa que ele irá passar para a próxima linha de código

condicao1 = False # ou 10 == 10
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')

elif condicao3:
    print('Código para condição 3')

elif condicao4:
    print('Código para condição 4')

else:
    print('Nenhuma condição foi satisfeita')

if 10 == 10:
    print('Outro if')

print('Fora do if')    