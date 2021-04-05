#Step1
#Puts the data in a 3D array - Tag | Time (strptime) | x.y

#imports
import math
from datetime import datetime
import numpy as np

#Definations
xlb = 320.0  # x left basket
ylb = 410.0  # y left basket
xrb = 420.0  # x right basket
yrb = 60.0  # y right basket
basketradius = 40.0  # distance from the center of the basket which count as "IN"
accuracy_limit = 0.0  # Value for accuracy check #הוספתי
#data_read_path = "/content/drive/MyDrive/Python files/20210207-154302IrTimes.txt" #path_of data to read
data_read_path =  "/content/drive/MyDrive/Python files/20210223-205817IrTimes.txt"

data_write_path = "Filtered_Relevant_Data_Run_N.txt" #path of data to write
last_date = "0000"
day_number = 0
list_locations = []



data_write = open(data_write_path, "w")  # פתיחת קובץ חדש לרשימת הדאטה
f = open(data_read_path, "r")
data = Lines = f.readlines()

for line in data:
    columns = line.split(",")
    #print(columns[13] + " " + columns[14])

    xydata = columns[14].split(" ")
    xydata = [x for x in xydata if x]
    xy_accuracy_data = columns[15].split(" ")  # הוספתי
    xy_accuracy_data = [x for x in xy_accuracy_data if x]  # הוספתי
    if (len(xydata) != 2) or (len(xy_accuracy_data) != 2):  # הוספתי
        continue

    x_accuracy_data = (float(xy_accuracy_data[0].replace("[", "").replace("]", "")))  # הוספתי
    y_accuracy_data = (float(xy_accuracy_data[1].replace("[", "").replace("]", "")))  # הוספתי
    if (y_accuracy_data > accuracy_limit) or (x_accuracy_data > accuracy_limit):  # הוספתי
        continue

    x = (float(xydata[0].replace("[", "").replace("]", "")))
    y = (float(xydata[1].replace("[", "").replace("]", "")))
    dt = datetime.strptime(columns[0] + " " + columns[1] ,  "%Y%m%d %H%M%S").timestamp()  #20210104
    t = np.array([int(columns[13]), dt, x, y])
    list_locations += [t]

list_array = np.array(list_locations)

f.close()
data_write.close()
print("Done! Part1!")
