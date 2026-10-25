import copy
english_freqs = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094,
    0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929,
    0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
    0.01974, 0.00074
]
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def numerate(word):
	result=[]
	for letter in word:
		result.append(alphabet.index(letter))
	return result
def denumerate(number):
	result=""
	for i in number:
		result+=alphabet[int(i)]
	return result
		
def encrypt(plain_text,key):
	cipher=""
	number_key=numerate(key)
	
	key_length=len(key)
	number_text=numerate(plain_text)
	for j in range(len(number_text)):
		
		cipher+=alphabet[(number_text[j]+number_key[j%key_length])%26]
	return cipher
def decrypt(cipher,key):
        plain=""
        number_key=numerate(key)
        key_length=len(key)
       	number_text=numerate(cipher)
        for j in range(len(number_text)):
                   
                plain+=alphabet[(number_text[j]-number_key[j%key_length])%26]
        return plain

def determine_key_size(cipher):
	counts=[]
	for length in range(1,len(cipher)):
		counter=0
	
		for i in range(len(cipher)-length):
			if cipher[i]==cipher[i+length]:
				counter+=1
		counts.append(counter)
	return counts

def total_probability(l1,l2):
	result=0
	for i in range(len(l1)):
		result+=(l1[i]*l2[i])
	return result
def best_key_guess(key_length,cipher):
	key=[]
	
	
	for element in range(key_length):
		calculated_probabilities=[]
		cipher_len=len(cipher)
		d=cipher_len-element
		boundary=(d+(-d)%key_length)/key_length
		print(boundary)
		ciphern=[(cipher[element+j*key_length]) for j in range(int(boundary))]
		calculated_probabilities=[(ciphern.count(letter)/len(ciphern)) for letter in alphabet]
		probabilities=[]
			
		
		probability=0
		for number in range(26):
			adjusted_frequency=copy.copy(english_freqs)
			for j in range(26):
				adjusted_frequency[j]=english_freqs[(j-number)%26]
			
			probabilities.append(total_probability(adjusted_frequency,calculated_probabilities))
			
		key.append(alphabet[probabilities.index(max(probabilities))])
	return key


			
		
	



