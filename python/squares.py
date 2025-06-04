#Uma forma de importar uma função específica de um módulo
#from functions import quadrado
#print (f"O quadrado de {i} é {quadrado(i)}")


#importar todas as funções de um módulo
from functions import quadrado
for i in range(10):
    print (f"O quadrado de {i} é {quadrado(i)}")
    