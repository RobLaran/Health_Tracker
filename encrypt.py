from hashlib import blake2b
from hmac import compare_digest

class EncryptPassword:
    def __init__(self):
        pass
    
    """ 
    Secure and verify password
    """
    def securePassword(self, password):
        encrypt = blake2b(digest_size=12)
        encrypt.update(bytes(password, 'utf-8'))
        return encrypt.hexdigest()
        
    def verify(self, hash, password):
        encryptPassword = self.securePassword(password)
        return compare_digest(encryptPassword, hash)