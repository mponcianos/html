# INDICE STRING

texto = "Você está no curso de Recuperação de Informação; com Linguagem Python"

# CRIA LISTA DE PALAVRAS - considerando espaço em branco para o split()
print(texto.split())

# SEPARA ONDE HOUVER PONTO E VÍRGULA
print(texto.split(";"))


nome = "MARIA-MADALENA-RATINBUM-DE-JESUS"
print(nome.split("-"))

# MOSTRA O TAMANHO DO SPLIT: contagem de palavras separadas
print(len(nome.split("-")))

# TROCAR (replace) ONDE EXISTIR "-", SERÁ TROCADO POR espaço em branco
print(nome.replace("-"," "))



