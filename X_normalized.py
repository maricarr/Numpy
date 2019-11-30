import numpy as np
X=np.random.random((5,5))
m=np.mean(X)
sd=np.std(X)
Z=(X-m)/sd
np.save('X_normalized',Z)
