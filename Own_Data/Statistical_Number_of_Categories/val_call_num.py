import  os
import  os
import xml.etree.ElementTree as ET

bicycle = 0
electric_bicycle = 0
van = 0
bus = 0
car = 0
person = 0
tricycle = 0
motorcycle = 0
truck = 0

xml_paths="D:\owner_data\Pascal_Vehicle\Annotations\\"
xml_name = []
for line in open("D:\owner_data\Pascal_Vehicle\ImageSets\Main/test.txt","r"): #设置文件对象并读取每一行文件
    xml_name.append(line[:-1])
xml_list=os.listdir(xml_paths)

for i in xml_list:
    if i[:-4] in xml_name:
        xmlpath=os.path.join(xml_paths,i)
        tree = ET.parse(xmlpath)
        ro = tree.getroot()
        for name in ro.iter("name"):
            # print(name.text)
            if name.text == "non-motor-vehicle,bicycle":
                bicycle += 1
            elif name.text == "non-motor-vehicle,electric-bicycle":
                electric_bicycle += 1
            elif name.text == "motor-vehicle,van":
                van += 1
            elif name.text == "motor-vehicle,bus":
                bus += 1
            elif name.text == "motor-vehicle,car":
                car += 1
            elif name.text == "person,null":
                person += 1
            elif name.text == "non-motor-vehicle,tricycle":
                tricycle += 1
            elif name.text == "non-motor-vehicle,motorcycle":
                motorcycle += 1
            elif name.text == "motor-vehicle,truck":
                truck += 1

print("bicycle:",bicycle)
print("electric_bicycle:",electric_bicycle)
print("van:",van)
print("bus:",bus)
print("car:",car)
print("person",person)
print("tricycle:",tricycle)
print("motorcycle:",motorcycle)
print("truck:",truck)

