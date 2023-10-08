print("Hello World!")
print(10 * 2)

vendas = 2000
custo = 300
lucro = vendas - custo

print("Tiveram ", vendas, " vendas e ", custo, " de custo. ")
print("O lucro foi de: ", lucro)

if  vendas > 1000:
    print("Ganhou bônus.") 
else: 
    print("Não ganhou bônus.")    

listaprodutos = ["iphone", "ipad", "notebook"]
listaprecos = [1500, 5000, 5500]

for produto in listaprecos: #dobrar o valor do "produto"
    print(produto * 2) 

for i in range(10): # range repete o que está dentro do for quantas vezes vc pedir
    print("eita rapaiz")     
