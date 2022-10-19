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

#Funcao imprimi a população e retorna o F(x1,...,x20) de cada individuo
def PrintPop(pop):
	ind=0
	best = 1000000
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


#Crossover entre a população mutante e a atual
def crossover(pop_x,pop_v):
	pop_u=[[0]*20 for x in range(len(pop_x))]
	for i in range(len(pop_x)):
		for j in range(20):
			cr = random.uniform(0.0000,1.0000)
			ji =  randint(0,19)
			if cr <= 0.9 or ji == j:
				pop_u[i][j] = pop_v[i][j]
			else:
				pop_u[i][j] = pop_x[i][j]
	return pop_u


#Criação da população Mutante
def mutation(pop):
	popv=[[0]*20 for x in range(len(pop))]
	r2=0
	r3=0
	for i in range(len(pop)):
		r2=randint(0,19)
		r3=randint(0,19)
		for j in range(20):
			popv[i][j] = pop[i][j] + 0.8*(pop[r2][j]-pop[r3][j])
	return popv

#Selecionar entre a população antiga e a nova
def selection(pop_x, pop_u):
	pop=[[0]*20 for x in range(len(pop_x))]
	for i in range(len(pop_x)):
		if (func(pop_u[i]) < func(pop_x[i])):
			pop[i] = pop_u[i]
		else:
			pop[i] = pop_x[i]
	return pop

def main():
	print("\n------RASTRIGIN EM EVOLUCAO DIFERENCIAL - 20 VARIAVEIS------")	
	p = int(input("\nDigite o tamanho da Populacao:"))
	g = int(input("\nDigite o tamanho de Geracoes:"))
	pop = randomPop(p)				#inicializa a população
	print("\n Populacao Inicial:")
	for i in range(g):
		PrintPop(pop)
		pop_u=[[0]*20 for x in range(p)]
		pop_u=crossover(pop,mutation(pop))	#cria a população mutante e faz crossover
		pop=selection(pop,pop_u)		#seleciona entre old or new individuos
		print("Geracao (%i): " % i)

if __name__ == "__main__": main()
