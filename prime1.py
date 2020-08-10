max_li = 1000000001

isPrime = []

def seive():
	for i in range(0, max_li):
		isPrime.append(True)
		# isPrime[i] = True
		
	for i in range(2, max_li / 2):
		if isPrime[i]:
			j = 2 * 1
			while j <= max_li:
				isPrime[j] = False
				j = j + i
				
			
		
	

if __name__ == "__main__":
	seive()
	t = int(input())
	for ii in range(0, t):
		m, n = [int(i) for i in input().split()]
		for i in range(m, n + 1):
			if isPrime[i]:
				print(i, "\n")