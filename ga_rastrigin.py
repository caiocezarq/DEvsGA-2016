import random, string, math
from random import randint

#Geração da população
def randomPop(p):
	pop = [[0]*20 for x in range(p)]
	for i in range(p):
		for j in range(20):
			pop[i][j] = random.uniform(-5.12,5.12)
	return pop


#Funcao Rastrigin 20 variaveis
def func(x):
	total = 0
	for i in range(len(x)):
		total +=  (x[i]*x[i] - 10*math.cos(2*math.pi*x[i]) + 10)
	return total

#Funcao imprimi a população e retorna o F(x1,...,x20) de cada individuo bem como a soma
def fAndPrint(pop):
	ind=0
	best = 1000
	total = 0
	fpop = []
	for i in range(len(pop)):
		x=pop[i]
		fxy=func(x)
		fpop.insert(i,fxy)
		total += fxy
		print("Ind%i : %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f," %(i,x[0],x[1],x[2],x[3],x[4],x[5],x[6]), end='')
		print(" %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f," %(x[7],x[8],x[9],x[10],x[11],x[12],x[13]), end='')
		print(" %.2f, %.2f, %.2f, %.2f, %.2f, %.2f" %(x[14],x[15],x[16],x[17],x[18],x[19]), end='')
		print("  ---> f(Ind): %f" %(fxy))
		if fxy < best:
			best = fxy
			ind = i
	print("\n Melhor Individuo: %i = %f || Media: %f" %(ind,best,(total/len(pop))))
	return fpop, total

#Roleta
def choose(fpop, total):
	ptotal=0
	pb=[]
	for x in range(len(fpop)):
		pb.insert(x,math.exp(12*(1-(fpop[x]/total)))/100)
#		pb.insert(x,(fpop[x]/total))
	c=[]
	m=min(pb)
	#Ajuste da probabilidade (improviso)
	for x in range(len(pb)):
		pb[x] = pb[x] - (m/1.1)
	for x in range(len(pb)):
		ptotal += pb[x]
#	print("\nProb AND probTotal")
#	print(pb, ptotal)
	for x in range(2):
		z=0
		ran=random.uniform(0.0000,ptotal)
		for i in range(len(pb)):
			z += pb[i]
			if z > ran:
				break
		c.insert(x,i)
#	print("\nEscolhido:")
#	print(c)
	return c

#CrossOver Linear
def crossover(p1,p2):
	x0=0
	x1=0
	x2=0
	ind = 0
	best = 10000
	f_ind=[]
	y=[[0]*20 for i in range(3)]
#	print("\nP1 e P2: ")
#	print(p1)
#	print(p2)
	for i in range(20):
		y[0][i] = (0.5*p1[i] + 0.5*p2[i])
		y[1][i] = (1.5*p1[i] - 0.5*p2[i])
		y[2][i] =  (-0.5*p1[i] + 1.5*p2[i])
	for i in range(3):
		for j in range(20):
			if y[i][j]>5.12:
				y[i][j] = 5.12
			if y[i][j]<-5.12:
	                        y[i][j]=-5.12
#	print("\nFILHOS")
#	print(y[0])
#	print(y[1])
#	print(y[2])
	for i in range(3):
		f_ind.insert(i,func(y[i]))
		if f_ind[i] < best:
			best = f_ind[i]
			ind = i
#	print("ALL NEW F_ind: ")
#	print(f_ind)
#	print("\nbest: %i " %(ind))
#	print(y[ind])
	return y[ind]

#Mutação Linear
def mutation(pop):
	new=0
	pb=0
	for i in range(len(pop)):
		pb=random.uniform(0.0000,1.0000)
		for j in range(20):
			if pb <=0.02:
				pop[i][j] = random.uniform(-5.12,5.12)
	return pop

def main():
	print("\n------RASTRIGIN EM ALGORITMOS GENETICOS - 20 VARIAVEIS------")
	p = int(input("\nDigite o tamanho da Populacao:"))
	g = int(input("\nDigite o tamanho de Geracoes:"))
	pop = randomPop(p)
	print("\n Populacao Inicial:")
	for i in range(g):
		fpop,total = fAndPrint(pop)
		popnew=[[0]*20 for x in range(p)]
		for j in range(p):
			c = choose(fpop,total)
			popnew[j]=crossover(pop[c[0]],pop[c[1]])
		pop=popnew
		pop=mutation(pop)
		print("\nGeracao (%i): " % i)

if __name__ == "__main__": main()
