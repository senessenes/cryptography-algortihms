def encrypt(binary_text,key):
	result=""
	for i in range(0,len(binary_text)):
		result+=str((int(binary_text[i])+int(key[i]))%2)
	sliced_binary_array= [result[i:i+8] for i in range(0,len(result),8)]
	
	return  result
def decrypt(binary_text,key):
	result=""              
	for i in range(0,len(binary_text)):
		result+=str((int(binary_text[i])+int(key[i]))%2)
	sliced_binary_array= [result[i:i+8] for i in range(0,len(result),8)]
                        
	return  result

			
