import matplotlib.pyplot as plt
import numpy as np
import yaml
def LoadYaml(File):
    with open(File, 'r', encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
    return data

#Sort Dir List by class_key
def DataClass(DirList,class_key):
    data_class = {}
    for it in DirList:
        data_class[it[class_key]] = []
    for it in DirList:
        data_class[it[class_key]].append(it)
    return data_class

FilePath = '/home/fanzhibo/python/MyTool/DataBase.yaml'
Data = LoadYaml(FilePath)
data_class = DataClass(Data['ResultData'],'Parameter')
print(data_class)
print(len(data_class))
#plot data
x = [1, 3, 5, 6]
y = [1, 3, 5, 9]
plt.plot(x,y)
plt.savefig(fname = "pic2.jpg", figsize = (30,30), dpi = 300)