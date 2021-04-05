#Step3
#Dealing with nan data. ploting graphs.

def nan_helper(y):
    return np.isnan(y), lambda z: z.nonzero()[0]


for a in range(len(list_tag)):
    y = main_data[a,:,:]
    nans, x= nan_helper(y)
    y[nans]= np.interp(x(nans), x(~nans), y[~nans])
    main_data[a,:,:] = y
print("Done! Part3!")

import matplotlib.pyplot as plt
batid=6
plt.figure()
plt.scatter(main_data[batid,:, 0], main_data[batid,:, 1])
plt.show()

import matplotlib.pyplot as plt

plt.figure()
plt.plot(main_data[6,:,0])
plt.show()
