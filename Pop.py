'''Have a population of N= 100,000 people to start. Each person has a randome number of acquaintances  (sau between 0 and A =50)
For each acquaintance of each person, there is a probrability of contact in a given day. When an infected person comes into contact with a susceptible person, there is a prob. p of ease being transmitted.

A person with the disease will have it for 14 days if he lives. Then he cannot have it again. THe prob of transfer decreases based on the day. When a person has the disease, ther is a probability of death on each day that grows up to the 14th day.

OVERARCHING PARAMETERS
N = 100000?  #num of people
A = random.randint(0,50) 			#number of acquaintences per person
pc = random.uniform(0,1)			 #contact probaility
p_t = .56 -.4*d 					#transfer probability (days with disieas = d)
p_d = .001 *d   					#death prob. (d = days with disease.) 

each person is an object with attribute
each acq is an object with attributes id, pc
Simulation ends when there are no infected
'''
#how many days did that person have the disease

#CRAFTED BY MICHAEL ASANTE
####################################CLASS DEFINITION###################################################
import random
class person():
	"""Constructs one human being with parameters of num of aquaintances, prob of contact, transfer prob, and prob of death"""
	def __init__(self, idnt,age,status):
		self.idnt = idnt
		self.age = age 
		self.status = status
		#write a function to increment days
	def get_id(self):
		return self.id
	def get_age(self):
		return self.age
	def get_status():
		return self.status
def generate_age():
	return(random.randint(1,110))

def calc_contact():
	return(uniform(0,1))

def generate_aclist(N,pl):
	randomlist = [j for j in range(N)]
	return(randomlist)

###############################CREATING THE ACQ LIST##################################################
def setup_pairs(N,s):
	import itertools
	pairs = list(set(itertools.combinations(generate_aclist(N-1,s), 2)))
	random.shuffle(pairs)
	#print(pairs)
	filtered_p = []
	final_list = []
	#Check if i > j for i,j in N
	for i in range(len(pairs)):
		if pairs[i][0] > pairs[i][1]:
			pairs[i] = pairs[i][1],pairs[i][0]
	#check if i == j 
	for j in range(len(pairs)):
		if pairs[j][0] != pairs[j][1]:
			filtered_p.append(pairs[j])
	#checking for duplicates
	pairs = set([i for i in pairs])
	#making final dictionary for aquaintance list
	for k in range(len(filtered_p)):
		final_list.append({'pair': filtered_p[k], 'pc': random.uniform(0,1)})
	
	return final_list
def chances(prob):
	a = random.uniform(0,1) < prob
	return(a)
############DEATH FORMULA#########################################

def calculate_pd(ob, l):
	return(ob.status['days']/(100*l))

##############TRANSFER RATE FORMULA#####################################
def calculate_pt(p, L):
	return(L-p.status['days']/(20*L))

############BREAD AND BUTTER OF SPREAD#############################################################
def check_pair(pop,aq_t,s,r):
	check = False
	if((pop[aq_t[r]['pair'][0]].idnt != s) or (pop[aq_t[r]['pair'][1]].status['state'] == 'S')):
		if(pop[aq_t[r]['pair'][0]].status['state'] == 'S'):
			check = chances(aq_t[r]['pc'])
		elif(pop[aq_t[r]['pair'][1]].status['state'] == 'S'):
			check = chances(aq_t[r]['pc'])
	return(check)
################MAIN FUNTION#########################################

num = int(input("Please enter the population amount: "))
num1 = int(input("How many acquaintances per person?: "))
act = setup_pairs(num,num1)

pop = [None]*num
r_count = 0
d_count = 0
#CREATING OUT POPULATION
for x in range(num):
	pop[x] = person(x, random.uniform(0,100), {'state': 'S', 'days': None})
for a in random.sample(pop,len(pop)//25):
	a.status = {'state': 'I', 'days': 1}
inf_count = len(pop)//25
#SETTING OUR INITIAL PATIENT ZEROS
status_list = [pop[x].status['state'] for x in range(len(pop)) if pop[x].status['state'] == 'I']
day = 1
print("Running Simulation...")
#SIMULATING A DAY!
while 'I' in status_list:
	ti = 0
	tr = 0
	td = 0
	s = 1
	patients = [pop[x].idnt for x in range(len(pop)) if pop[x].status['state'] == 'I'] #GETS THE ID OF EACH PATIENT
	#NOW WE CHECK PAIRS AND SEE IF THEY TRANSFER
	for lop in range(len(patients)):
		acq_t=	[x for x in act if patients[lop] in x['pair']]#FILTERS TO SEE IF THEY ARE NOT QUARANTINED
		if not acq_t:#If they are quarantined
			continue #DO NO OPERATION
		elif(check_pair(pop,acq_t,patients[lop],lop)):#CAlling the function to see if they transfer
			if chances(calculate_pt(pop[patients[lop]],day)):
				if(pop[acq_t[lop]['pair'][0]].status['state'] == 'S'):
					pop[acq_t[lop]['pair'][0]].status['state'] ='I'
					pop[acq_t[lop]['pair'][0]].status['days'] = 1
				else:
						pop[acq_t[lop]['pair'][1]].status['state'] = 'I'
						pop[acq_t[lop]['pair'][1]].status['days'] = 1
	
				ti = ti +1
	#CHECKING LIKELIHOODS 
	for loop in range(len(pop)):
		if pop[loop].status['state'] == 'I':
			#ADD ONE MORE TO A DAY
			pop[loop].status['days'] = pop[loop].status['days'] + 1
			if pop[loop].status['days'] == 14:
				if chances(calculate_pd(pop[loop],day)):
					pop[loop].status['state'] ='D'#ASK WHY NO ONE IS DYING
					#print("Death :(")
					td = td + 1
					d_count = d_count+1
				else:
					pop[loop].status['state'] ='R'
					r_count = r_count +1
					tr = tr + 1
					#print("RECOVERY!")
	#PUT ALL THE NEW STATUSES INSIDE A LIST and ADD A DAY
	status_list = [pop[x].status['state'] for x in range(len(pop)) if pop[x].status['state'] == 'I']
	print("Day {0}. There were {1} infected, {2} recovered, and {3} died ".format(day,ti,tr,td))						
	day = day +1

print("It took {0} days for the pandemic to end. There were {1} infected, {2} recovered, and {3} died ".format(day,inf_count, r_count, d_count))



			

