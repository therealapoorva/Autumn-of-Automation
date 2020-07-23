from numpy import *
def theta(x,y):
	if (array(x).shape == (20,20) and np.linalg.det(array(x))==1) and array(y).dtype == 'int32':
		x_t= x.T 
		output= (np.linalg.inv(x*x_t))*x_t
		return output*y



