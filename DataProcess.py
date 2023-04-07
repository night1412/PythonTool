import yaml

def LoadYaml(File):
    with open(File, 'r', encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
    return data
#Usage************************************************
#File = './DataBase.yaml'
#data = LoadYaml(File)
#for it in data['ResultData']:
    #print(it['SolveTime'])
    #print(type(it['SolveTime']))
#****************************************************


#Sort Dir List by class_key
def DataClass(DirList,class_key):
    data_class = {}
    for it in DirList:
        data_class[it[class_key]] = []
    for it in DirList:
        data_class[it[class_key]].append(it)
    return data_class
#Usage************************************************
# FilePath = '/home/fanzhibo/python/MyTool/DataBase.yaml'
# Data = LoadYaml(FilePath)
# data_class = DataClass(Data['ResultData'],'Parameter')
# print(data_class)
# print(len(data_class))
#****************************************************
    

