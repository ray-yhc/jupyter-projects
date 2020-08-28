#Copyright: Keehwan Nam 2013, Dept of physics, KAIST., Daejeon, South Korea.
#You may use this source without any payment in any purpose, if providing copyright information.
#Reference: arXiv:1304.3690
#Please let me know if you find error, miatake, fault, and whatever you think strange.
#E-mail: snowall@kaist.ac.kr / snowall@gmail.com
#Under Python 2.7.3

import numpy as np

initH=1./np.sqrt(2.)
initT=1./np.sqrt(2.)

init_coin = np.array([initH, initT])

latticeSize = 200
lattice = np.zeros((latticeSize+1,2))

lattice[latticeSize/2][0]=init_coin[0]
lattice[latticeSize/2][1]=init_coin[1]

Hadamard = np.array([[1,1j],[1j,1]])/np.sqrt(2.)

given_coinOP=Hadamard

def OPcoin(given_coin):
	return np.inner(given_coinOP, given_coin)

def coinFlip(psy):
	return map(OPcoin, psy)

def OPshift(psy):
	a= np.insert(psy[0][:-1],0,0)
	b= np.append(psy[1][1:],0)
	return (np.vstack((a,b))).transpose()

def OPu(psy):
	return OPshift(OPcoin(psy))

def PROJcoin(given_coin):
	return (np.conjugate(given_coin[0])*given_coin[0]+np.conjugate(given_coin[1])*given_coin[1]).real

def PROJ(psy):
	return map(PROJcoin, psy)

def QW(psy, it, per, fn):
	fdata = open(fn, "w")
	for k in range(it):
		if k%per==0:
			fdata.write(str(PROJ(psy))[1:-1]+"\n")
		psy = OPu(psy)

filename = '1dqw.csv'
QW(lattice, 100,1, filename)

plotopen=open(filename+".gpl","w")
plotopen.writelines("set terminal windows\n")
plotopen.writelines("set pm3d\n")
plotopen.writelines("splot \""+filename+"\" matrix w d" )
