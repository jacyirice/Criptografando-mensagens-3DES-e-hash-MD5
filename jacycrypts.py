from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import DES3
import hashlib

class JacyCrypt:
    BLOCK_SIZE = 32

    HASHS = {
        'MD5': {'f': hashlib.md5, 'tam': 32},
        'SHA256': {'f': hashlib.sha256, 'tam': 64},
    }

    def __init__(self, valor_secreto, type_hash='MD5'):
        type_hash = type_hash.upper()
        self.valor_secreto = valor_secreto
        self.type_hash = self.HASHS[type_hash]
        self.key = self.generate_key(valor_secreto, type_hash)

    def encrypt(self, mensagem):
        hash = self.generate_hash(mensagem)
        cipher = DES3.new(self.key, DES3.MODE_ECB)
        msg_pad = pad(f'{mensagem}{hash}'.encode(), self.BLOCK_SIZE)
        msg = cipher.encrypt(msg_pad)
        return msg

    def decrypt(self, mensagem):
        cipher = DES3.new(self.key, DES3.MODE_ECB)
        msgd_pad = cipher.decrypt(mensagem)
        msgdhash = unpad(msgd_pad, self.BLOCK_SIZE).decode()
        
        # Separa a mensagem da hash, considerando que os bytes da hash
        tam_hash = self.type_hash['tam']
        hash = msgdhash[-tam_hash:]
        msgd = msgdhash[:-tam_hash]
        return msgd, hash

    def generate_hash(self, mensagem):
        mensagem = f'{mensagem}{self.valor_secreto}'.encode()
        hash = self.type_hash['f'](mensagem).hexdigest()
        return hash

    def generate_key(self, valor, type_hash):
        hash = self.type_hash['f'](valor.encode()).digest()[:24]
        return hash

    def verify_hash(self, mensagem, hash):
        hash_new = self.generate_hash(mensagem)
        return hash_new == hash
