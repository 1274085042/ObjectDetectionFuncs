import os
import random
xmls_path="D:\owner_data\Pascal_Vehicle\Annotations"
BASE_DIR="D:\owner_data\Pascal_Vehicle\ImageSets"
sets={
"train":0.5,
"val":0.5,
#"test":0.1,
}

if __name__=="__main__":
    files=[]
    xmls=os.listdir(xmls_path)
    random.shuffle(xmls)
    for file in xmls:
        f,e=os.path.splitext(file)
        files.append(f)

    total=len(files)
    set_counter=0
    for (set_name,set_scale) in sets.items():
        with open(os.path.join(BASE_DIR,"Main",set_name+".txt"),'w') as st:
            tot=int(total*set_scale)
            for ith in range(set_counter,set_counter+tot):
                print("{}".format(files[ith]),file=st)
            set_counter+=tot

    with open(os.path.join(BASE_DIR,"Main","trainval.txt"),'w') as train_val:
        for setname in ("train","val"):
            for line in open(os.path.join(BASE_DIR,"Main",setname+".txt"),'r'):
                print(line,end="",file=train_val)



