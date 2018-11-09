#This program can be 
import argparse
parser = argparse.ArgumentParser(description = 'There is only one argument required to run this program, which is --path.\n\rYou can run this file with command like this in your command line:\n\rpython ICD_Yunze_Hao.py --path ./BMI500/ICD/2018_I10gem.txt')
parser.add_argument('--path', required = True, type = str)
args = parser.parse_args()
data=args.path
name=data[-10:-4]
if name[0]=='_':
    name=name[1:]
def ICD(data):
    pre={}
    no_map=0
    countm=0
    counto=0
    countline=0
    comb=0
    prec={}
    with open(data,'r') as f:
        line=f.readline()
        while line:
            line=line.split(' ')
            if len(line)!=3:
                while '' in line:
                    line.remove('')
            if line==[]:
                line=f.readline()
                continue
            if line[2][1]=='1':
                no_map+=1
                line=f.readline()
                continue
            if line[2][2]=='1':
                comb+=1
            countline+=1
            pre[line[0]]=pre.get(line[0],0)+1
            line=f.readline()
    for each in pre:
        if pre[each]>1:
            countm+=pre[each]
        elif pre[each]==1:
            counto+=1
    print(name,': No mappings',no_map)
    print(name,': One to many mappings',countm)
    print(name,': One to One mappings',counto)
    print(name,': Mappings that belong to a combination',comb)
ICD(data)