import shutil, os, glob

os.chdir(r'C:/RulesTester/_TESTING_DATA_/CMS_SkyRules_20190321_001/CMS_SkyRules_20200124_002_Original/')
myFiles = glob.glob('*.tar')
path = 'C:/RulesTester/_TESTING_DATA_/CMS_SkyRules_20190321_001/CMS_SkyRules_20200124_002_Original/'
#path2= 'C:/Users/AKR18/OneDrive - Sky/Documents/RTE/NewPack'
def moveAndCreateDir(sourcePath, dstDir):
    if os.path.isdir(dstDir) == False:
       os.makedirs(dstDir);
    shutil.move(sourcePath, dstDir);

for x in myFiles:
   #print(x)
   sourceFile = [f for f in glob.glob(path + x, recursive=True)]
   for f in sourceFile:
       print(f)
       destDir=f.replace('.tar', '')
       print(destDir)
       moveAndCreateDir(f, destDir)