import subprocess

IMG_PATH = r'sample-assets\itaots-heartbaby-profilepic.jpg'
EXE_PROCESS = "hachoir-metadata"
infoDict = {}
process = subprocess.Popen([EXE_PROCESS, IMG_PATH], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

for tag in process.stdout:
    line = tag.strip().split(':')
    infoDict[line[0].strip()] = line[-1].strip()

for k,v in infoDict.items():
    print(k,':', v)
