from jacycrypts import JacyCrypt

# Valores iniciais
valor_secreto = 'prova-ss'
mensagem_original = 'Jacyirice Silva Oliveira'
print('Mensagem original:', mensagem_original)

# Encriptar
jacycrypt = JacyCrypt(valor_secreto)
mensagem_encriptada = jacycrypt.encrypt(mensagem_original)
print('Mensagem encriptada:', mensagem_encriptada)

# Decriptar
jacycrypt = JacyCrypt(valor_secreto)
mensagem_decriptada, hash = jacycrypt.decrypt(mensagem_encriptada)
hash_new = jacycrypt.gerar_hash(mensagem_decriptada)
print('Mensagem decriptada:', mensagem_decriptada)
print('Hash da mensagem encriptada:', hash)
print('As hashs são iguais?', hash_new == hash)

