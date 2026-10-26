import numpy as np
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
def extended_eucledian(a,n):
        remainders=[]
        coefficients=[]
        a1=a
        b1=n


        while True:
                r=a1%b1

                q=(a1-r)/b1
                remainders.append(r)
                coefficients.append(q)
                a1=b1
                b1=r

                if r==0:
                        break
        coefficient_of_a=1
        l=len(remainders)
        ca1=1
        ca2=-coefficients[1]
        a_coefficients=[ca1,ca2]
        for remainder in range(2,l-1):
                coefficient_of_a=a_coefficients[remainder-2]-coefficients[remainder]*a_coefficients[remainder-1]
                a_coefficients.append(coefficient_of_a)






        gcd=remainders[l-2]
        return {"gcd":gcd,"modular_inverse":(a_coefficients[l-2]) if gcd==1 else "no inverse"}
def adj(A):
	cofactor_matrix = np.zeros_like(A, dtype=float)
	
	for i in range(0,len(A)):
		for x in range(0,len(A[i])):
		
			M1=np.delete(A,i,axis=0)
			
			cofactor=((-1)**(x+i))*round(np.linalg.det(np.delete(M1,x,axis=1)))
			cofactor_matrix[i][x]=cofactor
	return cofactor_matrix.T
			
			
	
