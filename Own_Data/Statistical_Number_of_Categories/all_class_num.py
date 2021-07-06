import  os
import xml.etree.ElementTree as ET
import  matplotlib
import  matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文

category=("non-motor-vehicle,bicycle","non-motor-vehicle,electric-bicycle",
"motor-vehicle,van","motor-vehicle,bus","motor-vehicle,car","person,null",
"non-motor-vehicle,tricycle","non-motor-vehicle,motorcycle","motor-vehicle,truck")

own_data="D:\owner_data/Vehicle"
jpg_count = 0

xml_path=[]

def statistic(root_path):
    category_num={}
    bicycle = 0
    electric_bicycle = 0
    van = 0
    bus = 0
    car = 0
    person = 0
    tricycle = 0
    motorcycle = 0
    truck = 0

    global jpg_count
    for root,dirname,filenames in os.walk(root_path):
        for f in filenames:
            if f[-4:]==".xml":
                filepath=os.path.join(root,f)
                tree=ET.parse(filepath)
                ro=tree.getroot()
                for name in ro.iter("name"):
                    #print(name.text)
                    if name.text=="non-motor-vehicle,bicycle":
                        bicycle+=1
                    elif name.text=="non-motor-vehicle,electric-bicycle":
                        electric_bicycle+=1
                    elif name.text == "motor-vehicle,van":
                        van+=1
                    elif name.text == "motor-vehicle,bus":
                        bus+=1
                    elif name.text == "motor-vehicle,car":
                        car+=1
                    elif name.text == "person,null":
                        person+=1
                    elif name.text == "non-motor-vehicle,tricycle":
                        tricycle+=1
                    elif name.text == "non-motor-vehicle,motorcycle":
                        motorcycle+=1
                    elif name.text == "motor-vehicle,truck":
                        truck+=1
            elif f[-4:]==".jpg":
                jpg_count+=1

    print("bicycle:",bicycle)
    category_num["bicycle"]=bicycle
    print("electric_bicycle:",electric_bicycle)
    category_num["electric_bicycle"]=electric_bicycle
    print("van:",van)
    category_num["van"]=van
    print("bus:",bus)
    category_num["bus"]=bus
    print("car:",car)
    category_num["car"]=car
    print("person",person)
    category_num["person"]=person
    print("tricycle:",tricycle)
    category_num["tricycle"]=tricycle
    print("motorcycle:",motorcycle)
    category_num["motorcycle"]=motorcycle
    print("truck:",truck)
    category_num["truck"]=truck
    #Dprint(category_num)
    category_num=sorted(category_num.items(),key=lambda x:x[1],reverse=True)
    print(category_num)
    x_list=[i[0] for i in category_num]
    y_list = [i[1] for i in category_num]

    plt.bar(x=x_list,height=y_list,color='m')
    # 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
    for x, y in zip(x_list, y_list):
        plt.text(x, int(y) + 1, str(y), ha='center', va='bottom', fontsize=10)
    plt.xticks(fontsize=5)
    plt.yticks(fontsize=7)
    # plt.xlabel("类别")
    # plt.ylabel("数量")
    # plt.title("统计各个类别样本数量")
    plt.savefig("category_num.png")
    plt.show()

if __name__=="__main__":
    statistic(own_data)
    print("\nJPG count: ",jpg_count)