d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
hmarks = (max(d['Marks']))
location = [i for i, t in enumerate(d['Marks']) if t==hmarks]
print(d['Student'][location[0]])



##########################################################################################################