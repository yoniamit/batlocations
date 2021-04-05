#Step2
#Puts the data in a new array, Divided into time units with mean location for each time unit.

#Defenitions
per_unit = 10
minimum_time = np.min(list_array[:,1])
maximum_time = np.max(list_array[:,1])
time_now = minimum_time
list_tag = np.unique(list_array[:,0])
main_data = np.zeros((len(list_tag),int((maximum_time-minimum_time)/per_unit), 2))
t = 0

print(list_array[:,1])
print(minimum_time, maximum_time)
print(type(list_tag[0]))

tagids  = list_array[:,0]
dates = list_array[:,1]



while time_now <= (maximum_time - per_unit):
  for a in range(len(list_tag)):
    main_data[a,t,:] = np.mean(list_array[(tagids == list_tag[a]) & (dates> time_now) & (dates< (time_now + per_unit)) ,2:4],axis = 0)
  t += 1  
  time_now += per_unit



print("Done! Part2!")
