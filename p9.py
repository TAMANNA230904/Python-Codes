'''try:
	f1=open('newfile.txt','r')
except ZeroDivisionError:
	print('Exception 1')
except ValueError:
	print('Exception 2')
except Exception:
	print('Exception 3')
else:
	x=f1.read()
	print(f1.read())'''
import numpy as np
a1=np.array([[1,2,3],[4,5,6]])
print(a1.dtype)
print(a1.ndim)
print(a1.shape)