from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import DES3
import hashlib

class JacyCrypt:
    BLOCK_SIZE = 32
    
    def __init__(self, valor_secreto):
        self.valor_secreto = valor_secreto
        self.key = hashlib.md5(valor_secreto.encode()).digest()

    def encrypt(self, mensagem):
        hash = self.gerar_hash(mensagem)
        cipher = DES3.new(self.key, DES3.MODE_ECB)
        msg_pad = pad(f'{mensagem}{hash}'.encode(), self.BLOCK_SIZE)
        msg = cipher.encrypt(msg_pad)
        return msg
    
    def decrypt(self,mensagem):
        cipher = DES3.new(self.key, DES3.MODE_ECB)
        msgd_pad = cipher.decrypt(mensagem)
        msgdhash = unpad(msgd_pad, self.BLOCK_SIZE).decode()
        
        # Separa a mensagem da hash, considerando que o MD5 tem 128 bits
        hash = msgdhash[-32:]
        msgd = msgdhash[:-32]
        return msgd, hash

    def gerar_hash(self, mensagem):
        mensagem = f'{mensagem}{self.valor_secreto}'.encode()
        hash = hashlib.md5(mensagem).hexdigest()
        return hash
