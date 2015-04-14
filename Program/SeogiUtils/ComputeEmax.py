import numpy as np

def computeEmax(time, eEM, mesh):
	ntime = time.size
	eEM_CC = mesh.aveE2CCV*eEM
	eabs = (eEM_CC)**2
	Eabs = np.zeros((mesh.nC, ntime))
	for i in range(ntime):
    	Eabs[:,i] = (np.reshape(eabs[:,i], (mesh.nC, 3), order = 'F')).sum(axis = 1)
	indEmax = np.argmax(Eabs, axis = 1)
	indEmax_e = (mesh.aveE2CC.T*indEmax).astype(int)
	IndEmax_e = Utils.sub2ind((eEM).shape, np.c_[np.arange((eEM).shape[0]), indEmax_e])
	eEM_max = Utils.mkvc(eEM)[IndEmax_e]
	eEM_max_CC = mesh.aveE2CCV*eEM_max
    	
	return eEM_max, eEM_max_CC