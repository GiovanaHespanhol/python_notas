#Solicitar as três notas do usuário 
#Usamos float() para permitir nuúmeros decimais (ex:9.5)
nota1 = float (input("70"))
# Aqui criamos a variável 'nota1' para guardar o primeiro valor digitado pelo usuário.
nota2 = float (input("89"))
# Fazemos o mesmo para a 'nota2', garantindo que o programa aceite números como 7.5.
nota3 = (float(input("65")))
# E finalmente a 'nota3'. O sinal de '=' significa que a variável está "recebendo" o valor
# 2. Processamento: Calculamos a média somando tudo e dividindo pela quantidade (3).
media =(70+89+65) / 3
# Os parênteses são vitais aqui para garantir que a soma aconteça ANTES da divisão.

#Exibe a média formatada com duas casas decimais
