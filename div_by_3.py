import numpy as np
A=np.array(range(1,101))
A.resize(10,10)
sqr=A**2
div=sqr[sqr%3==0]
np.save('div_by_3',div)


