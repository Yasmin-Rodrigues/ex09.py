#Faça um programa que leia o preço do produto e mostre seu novo preço com 5% de desconto
p =float(input('Informe o preço do produto: R$'))
d =p*0.05
pd =p-d
print('O valor do produto com desconto de 5% é de: R${}'.format(pd))
