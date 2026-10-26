import numpy as np
import general_tools as tools

def encrypt(plain_text,key):
	n=len(key[0])
	
	p=plain_text
	
	p+=("X")*(n-(len(plain_text)%n))
	
	number_text=tools.numerate(p)
	row_vectors=np.array([number_text[i:i+n] for i in range(0,len(number_text),n)])
	
	cipher_matrix=row_vectors@key
	cipher_matrix%=26
	result=""
	for block in cipher_matrix:
		result+=tools.denumerate(block)
		
	return result
def decrypt(cipher,encryption_key):
	n=len(encryption_key[0])
	number_cipher=tools.numerate(cipher)
	row_vectors=np.array([number_cipher[i:i+n] for i in range(0,len(number_cipher),n)])
	det=int(np.linalg.det(encryption_key))
	
	c=tools.extended_eucledian(det,26)["modular_inverse"]
	if c<0:
		c+=26
	print(c)
	print(tools.adj(encryption_key))
	decryption_key=c*tools.adj(encryption_key)
	message_matrix=(row_vectors@decryption_key)%26
	message=""
	for r in message_matrix:
		message+=tools.denumerate(r)
	return message

	
