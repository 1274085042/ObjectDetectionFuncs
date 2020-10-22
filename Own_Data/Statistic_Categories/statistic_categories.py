import  os
import xml.etree.ElementTree as ET

own_data="D:\owner_data/Vehicle"
jpg_count = 0
xml_count=0
xml_path=[]
category=set()

def statistic(root_path):
    global jpg_count
    for root,dirname,filenames in os.walk(root_path):
        for f in filenames:
            if f[-4:]==".xml":
                filepath=os.path.join(root,f)
                xml_path.append(filepath)
                #print(filepath)
                tree=ET.parse(filepath)
                ro=tree.getroot()
                for name in ro.iter("name"):
                    #print(name.text)
                    category.add(name.text)
            elif f[-4:]==".jpg":
                jpg_count+=1

if __name__=="__main__":
    statistic(own_data)
    print("XML count: ",len(xml_path))
    print("JPG count: ",jpg_count)
    print('\n')
    print('Category: ',len(category))
    for c in category:
        print(c)