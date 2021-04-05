#Step4
#Ceating two arrays:
#1 - Distance array - for each time unit and each bat  - calculating the mean distance between the bat to all the othe bats.
#2 - movment array - for each time unit and each bat -  calculating the distance between current location and the last location.
#Ploting some graphs - compering and correlating.

time_now = minimum_time
t = 0
distance_array = np.zeros((len(list_tag),int((maximum_time-minimum_time)/per_unit)))

while time_now <= (maximum_time - per_unit):
  for a in range(len(list_tag)):
    my_pos = main_data[a,t,:]
    all_pos = main_data[:,t,:]
    other_bats_pos = np.delete(all_pos,a, 0)
    dist = []
    for pos in other_bats_pos:
      dist += [np.mean(np.linalg.norm(my_pos - pos))]
    dist = np.array(dist)
    dist = np.mean(dist)
    distance_array[a,t] = dist
  t += 1  
  time_now += per_unit

print(distance_array)

time_now = minimum_time + per_unit
t = 1
movment_array = np.zeros((len(list_tag),int((maximum_time-minimum_time)/per_unit)))

while time_now <= (maximum_time - per_unit):
  for a in range(len(list_tag)):
    my_pos = main_data[a,t,:]
    mt_prev_pos = main_data[a,t -1,:]
    thedistance = np.linalg.norm(my_pos - mt_prev_pos)
    movment_array[a,t-1] = (thedistance )
  t += 1  
  time_now += per_unit

print(movment_array)
correlations = []
for a in range(len(list_tag)):
  correlations.append(np.correlate(movment_array[a,:],distance_array[a,:]))


correlations = np.array(correlations)
print(correlations)

import numpy as np
from sklearn.mixture import GaussianMixture
maindatashape = np.shape(main_data)
f = np.reshape([main_data[:,:,:] ] , (maindatashape[0]*maindatashape[1] , 2) )
gmmcomp = 5
gm = GaussianMixture(n_components=gmmcomp, random_state=0).fit( f )
print(gm.means_)
print(gm.weights_)

fig , axs= plt.subplots(len(list_tag) ,figsize=(20,20), sharey=True)
for a in range(len(list_tag)):
    gmpred = gm.predict(main_data[a,:,:])
    
    axs[a].set_title("dominance is : " + str(correlations[a]))
    axs[a].hist(gmpred , bins = range(gmmcomp+1))
fig.savefig('result1.png')


import matplotlib.pyplot as plt

fig= plt.figure()

f = np.array(range(gmmcomp))
for i, txt in enumerate(f):
    plt.annotate(txt, (gm.means_[i,0], gm.means_[i,1]))
    
plt.scatter(gm.means_[:, 0], gm.means_[:, 1])
plt.show()
fig.savefig('mapofplaces.png')

for a in range(len(list_tag)):
    fig = plt.figure()   
    gmpred = (gm.predict(main_data[a,8000:10000,:])   ).astype(int)
    plt.plot(gmpred )
    #plt.scatter(correlations[a] , len(gmpred[gmpred==1]))
    
fig.savefig('dominanceVsHome.png')

