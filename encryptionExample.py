from crypto import AES
import crypto
key = b'notsuchsecretkey' # 128 bit (16 bytes) key
iv = crypto.getrandbits(128) # hardware generated random IV (never reuse it)

cipher = AES(key, AES.MODE_CFB, iv)
msg = iv + cipher.encrypt(b'Attack at dawn')
