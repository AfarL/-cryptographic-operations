from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode
import hashlib
import time
from Cryptodome.Random import get_random_bytes


def encrypt(plain_text, password):
  t1 = time.perf_counter()
  # generate a random salt
  salt = get_random_bytes(AES.block_size)

  # use the Scrypt KDF to get a private key from the password
  private_key = hashlib.scrypt(
    password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

  # create cipher config
  cipher_config = AES.new(private_key, AES.MODE_GCM)

  # return a dictionary with the encrypted text
  cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
  t2 = time.perf_counter()
  print("Encrypt_time:", t2 - t1)
  print("cipher_text:", b64encode(cipher_text).decode('utf-8'))

  return {
    'cipher_text': b64encode(cipher_text).decode('utf-8'),
    'salt': b64encode(salt).decode('utf-8'),
    'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
    'tag': b64encode(tag).decode('utf-8'),
    'Encrypt_time': t2 - t1
  }

def decrypt(enc_dict, password):
  t3 = time.perf_counter()
  # decode the dictionary entries from base64
  salt = b64decode(enc_dict['salt'])
  cipher_text = b64decode(enc_dict['cipher_text'])
  nonce = b64decode(enc_dict['nonce'])
  tag = b64decode(enc_dict['tag'])

  # generate the private key from the password and salt
  private_key = hashlib.scrypt(
    password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

  # create the cipher config
  cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

  # decrypt the cipher text
  decrypted = cipher.decrypt_and_verify(cipher_text, tag)
  t4 = time.perf_counter()
  print("Dencrypt_time:", t4 - t3)
  print("plain_text:", decrypted)
  return t4 - t3

def main():
  sum_encrypt=0
  sum_dencrypt = 0
  for i in range(1000):
      Key=str(i)
      encrypted = encrypt("Secret", Key)
      sum_encrypt=sum_encrypt+encrypted['Encrypt_time']
      sum_dencrypt = sum_dencrypt+decrypt(encrypted, Key)
  print("Total time to encrypt 1000 times:", sum_encrypt)
  print("Average_encrypt_time:", sum_encrypt/1000)
  print("Total time to dencrypt 1000 times:", sum_dencrypt)
  print("Average_dencrypt_time:", sum_dencrypt / 1000)

main()


