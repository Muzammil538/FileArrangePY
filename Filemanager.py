import os , shutil

download = '../../../Downloads'
documents = '../../../Documents'
desktop = '../../../Desktop'
path = int(input("Enter Path:\n1.Downloads\n2.Documents\n3.Desktop\nEnter the option : "))
if(path == 1):
    finalPath = download

elif (path == 2):
    finalPath = documents

elif (path == 3):
    finalPath = desktop

files = os.listdir(finalPath)

for file in files:
    name , ext = os.path.splitext(file)
    ext = ext[1:]

    if os.path.exists(finalPath+'/'+ext):
        shutil.move(finalPath+'/'+file , finalPath+'/'+ext+'/'+file)
    else:
        os.mkdir(finalPath+'/'+ext)
        shutil.move(finalPath+'/'+file , finalPath+'/'+ext+'/'+file)
