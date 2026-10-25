import general_tools as tools
import copy
#Encrytpts a given plain text using the affine cipher algorithm. In this algorithm, the key is a vector with 2 components:(a,b) and x gets encrypted to x---->ax+b(mod 26)
alphabet=tools.alphabet
#gcd(a,26) must be 1, otherwise the encryption wont be one to one and it will be impossible to decrypt even if we would know the key.
def encrypt(plain_text,key):
	number_text=tools.numerate(plain_text)
	encrypted_message=""
	for i in range(len(number_text)):
		encrypted_message+=(alphabet[(key[0]*number_text[i]+key[1])%26])
	return encrypted_message



#The best approach to attack such algorithm when we only know the cipher text would brute-forcing every possible key since there are only 312 of the. !Remember gcd(a,26) must  be 1 for such encryption.
def decrypt_cipher_only(c):
	cipher=tools.numerate(c)
	
	possible_a=[a for a in range(1,26) if tools.extended_eucledian(a,26)["gcd"]==1]
	b=range(0,26)
	possible_results=[]
	for a in possible_a:
		
		inverse_of_a=tools.extended_eucledian(a,26)["modular_inverse"]
		for b in range(26):
			possible_result=""
			for c in cipher:
				x=int(((c-b)*inverse_of_a)%26)
				possible_result+=alphabet[x]
			possible_results.append([possible_result,a,b])
	
	for b in range(26):
		possible_result=""
		for c in cipher:
			x=c-b
			possible_result+=alphabet[x]
		possible_results.append([possible_result,0,b])

	
	return possible_results
def decrypt_with_key(c,key):
	cipher=tools.numerate(c)
	a=key[0]
	b=key[1]
	result=""
	
	if(a==0):
		for number in cipher:
			x=number-b
			result+=alphabet[x]
		return result				
	inverse_of_a=tools.extended_eucledian(a,26)["modular_inverse"]
	for number in cipher:
		x=int((inverse_of_a*(number-b))%26)
		result+=alphabet[x]
	return result
	
							
		
		


message="MERHABABENSULEYMAN"
key=(7,3)
encrypted=encrypt(message,key)
print(encrypted)
decrypted=decrypt_with_key(encrypted,key)
print(decrypted)
