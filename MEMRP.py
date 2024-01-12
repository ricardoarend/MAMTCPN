# Mapeamento entre Esquemas Moise para Redes de Petri

import xml.etree.ElementTree as ET
import xml.dom.minidom
import random

#Leitura do documento xml

doc_name = str(input("Digite o nome do arquivo xml: "))

doc_name += '.xml'

# doc_name = "wp-os.xml"  # Arquivo Write Paper XML
# doc_name = "arvore3.xml" # Arquivo da Miriam
# doc_name = "st-os.xml" # Arquivo Soccer Team XML

document = xml.dom.minidom.parse(doc_name)

curr_mission = 'BOOL'
stored_mission = ''

# Função que limpa os nós de texto e novas linhas deixando só os nodos de interesse [goals e plans]

def clear_node(branch):
    i = 0
    while i < len(branch):
        if branch[i].nodeName == "#text":
            branch[i].parentNode.removeChild(branch[i])
        i+=1
    return branch

class Missions():
    def __init__(self, data):
        self.data = data 
        self.mission = None

def find_node_mission(goal):
    
    mission = ""
    for i in range(0, len(goals_missions)):
        for j in range(0, len(goals_missions[i])):   
            if goals_missions[i][j].data.getAttribute("id") == goal.getAttribute("id"):
                # print(" Mission: ", goals_missions[i][j].mission)
                mission = goals_missions[i][j].mission
    if mission == "":
        return "BOOL"
    else:
        return mission

def find_mission(goal):
    global curr_type
    global curr_mission
    global stored_mission
    stored_mission = curr_mission
    mission = ""
    for i in range(0, len(goals_missions)):
        for j in range(0, len(goals_missions[i])):   
            if goals_missions[i][j].data.getAttribute("id") == goal.getAttribute("id"):
                # print(" Mission: ", goals_missions[i][j].mission)
                mission = goals_missions[i][j].mission[:4]
                curr_mission = goals_missions[i][j].mission
    if mission == "":
        curr_mission = "BOOL"
        curr_type = "BOOL"
        return str(goal.getAttribute("id"))
    else:
        curr_type = "RG"
        return str(goal.getAttribute("id") + "\n(" + mission + ")")
    
struct_spec = []

for i in range(0, len(document.getElementsByTagName("group-specification"))):
    roles = document.getElementsByTagName("group-specification")[i]
    clear_node(roles.childNodes)
    group = [roles.getAttribute("id")]
    roles = roles.childNodes[0] 
    clear_node(roles.childNodes)
    for j in range(0, len(roles.childNodes)):
        role = roles.childNodes[j].getAttribute("id")
        if role not in group:
            group.append(role)
    struct_spec.append(group)
    
# print(f'struct_spec = {struct_spec}')

# roles = document.getElementsByTagName("group-specification")[0]

# group = roles.getAttribute("id")

# clear_node(roles.childNodes)

# roles = roles.childNodes[0]

# clear_node(roles.childNodes)

# for i in range(len(roles.childNodes)):
#     role = roles.childNodes[i].getAttribute("id")
#     if role not in struct_spec:
#         struct_spec.append(role)
        
n_missions = []
        
norm = document.getElementsByTagName("normative-specification")[0]

clear_node(norm.childNodes)
        
for i in range(len(norm.childNodes)):
    normative = norm.childNodes[i].getAttribute("mission")
    if normative not in n_missions:
        n_missions.append(normative)
    
missions = document.getElementsByTagName("mission") # Pega todos os nodos mission

elipse_x = '0'
elipse_y = '250'
arc_y  = '200'
trans_y = '0'
trans_x = '0'

t14 = ''

x = 0

id = ''

y1 = ''
x1 = ''

permit_trans = True
is_decendant = False
has_operator = False
had_operator = False

trans_pos = '0'

start_choice_x = '0'

parallel_x = '0'
parallel_y = '0'

choice_x = '0'
choice_y = '0'

is_first_child = True
is_last_child = False

last_choice_y = '0'
end_choice_x = '0'

created = False

elipse_id = ''
trans_id = ''
trans_choice = []

choice_trans_arc = False

curr_operator = False
curr_type = 'BOOL'

op = -1
main_operator = [['',False, '', '']]

trans_1 = '0'
trans_2 = '0'

trans_1_x = '0'
trans_1_y = '0'
horizontal_x = '0'

transitions = 1
node = ''

functions = []
# short_functions = []

root = ET.Element("workspaceElements")
name = "wtitle"
type = "RG"

def update_arc():
    global arc_y
    arc_y = int(float(arc_y)) - 100
    arc_y = str(arc_y)

def update_y():
    global elipse_y
    elipse_y = int(float(elipse_y)) - 100
    elipse_y = str(elipse_y)
    # print('y: ' + elipse_y)

def update_choice_y():
    global choice_y
    choice_y = int(float(choice_y)) - 100
    choice_y = str(choice_y)

def update_x():
    global horizontal_x
    horizontal_x = float(horizontal_x) + 150
    horizontal_x = str(horizontal_x)

def update_parallel_x():
    global parallel_x
    global x
    parallel_x = int(float(parallel_x)) + x
    parallel_x = str(parallel_x)

def update_choice_x():
    global x
    global choice_x
    choice_x = int(float(choice_x)) + x
    choice_x = str(choice_x)
    
def update_start_choice_x():
    global x
    global start_choice_x
    start_choice_x = int(float(start_choice_x)) + x
    start_choice_x = str(start_choice_x)

def update_elipse(id):
    global elipse_id
    elipse_id = id

def update_trans(id):
    global trans_id
    trans_id = id

def create_id():
    id = "ID" + str(random.randint(1000000000, 9999999990))
    return id

def update_id(id):
    last_two_digits = id[-2:]
    if last_two_digits == '99':
        id = id[:-2] + '00'
    else:
        id = id[:-1] + str(int(id[-1]) + 1)
    return id

def create_elipse(name, type, use_horizontal):
    
    global id
    global elipse_y
    global y1
    global x1
    
    id = create_id()
    
    # print(f"Use_horizontal == {use_horizontal}")
    
    if use_horizontal == False:
        y1 = elipse_y
        y1 = str(y1)
        y2 = int(elipse_y) - 30
        y2 = str(y2)
        y3 = int(elipse_y) + 27
        y3 = str(y3)

        x1 = elipse_x
        x1 = str(x1)
        x2 = int(elipse_x) + 32.5
        x2 = str(x2)
        x3 = int(elipse_x) + 56
        x3 = str(x3)
    else:
        y1 = trans_1_y
        y1 = str(y1)
        y2 = int(trans_1_y) - 30
        y2 = str(y2)
        y3 = int(trans_1_y) + 27
        y3 = str(y3)

        x1 = horizontal_x
        x1 = str(x1)
        x2 = float(horizontal_x) + 32.5
        x2 = str(x2)
        x3 = float(horizontal_x) + 56
        x3 = str(x3)
    
    p1 = ET.SubElement(b37, "place")
    p1.set('id', id)
    p2 = ET.SubElement(p1, "posattr")
    p2.set('x', x1)
    p2.set('y', y1)
    p3 = ET.SubElement(p1, "fillattr")
    p3.set('colour', 'White')
    p3.set('pattern', '')
    p3.set('filled', 'false')
    p4 = ET.SubElement(p1, "lineattr")
    p4.set('colour', 'Black')
    p4.set('thick', '1')
    p4.set('type', 'solid')
    p5 = ET.SubElement(p1, "textattr")
    p5.set('colour', 'Black')
    p5.set('bold', 'false')
    p6 = ET.SubElement(p1, "text")
    p6.text = name
    p7 = ET.SubElement(p1, "ellipse")
    p7.set('w', '75.000000')
    p7.set('h', '40.000000')
    p8 = ET.SubElement(p1, "token")
    p8.set('x', '-10.000000')
    p8.set('y', '0.000000')
    p9 = ET.SubElement(p1, "marking")
    p9.set('x', '0.000000')
    p9.set('y', '0.000000')
    p9.set('hidden', 'true')
    p10 = ET.SubElement(p9, "snap")
    p10.set('snap_id', '0')
    p10.set('anchor.horizontal', '0')
    p10.set('anchor.vertical', '0')

    update_elipse(id)
    
    id = update_id(id)
    
    p11 = ET.SubElement(p1, "type")
    p11.set('id', id)
    p12 = ET.SubElement(p11, "posattr")
    p12.set('x', x2)
    p12.set('y', y2)
    p13 = ET.SubElement(p11, "fillattr")
    p13.set('colour', 'White')
    p13.set('pattern', 'Solid')
    p13.set('filled', 'false')
    p14 = ET.SubElement(p11, "lineattr")
    p14.set('colour', 'Black')
    p14.set('thick', '0')
    p14.set('type', 'Solid')
    p15 = ET.SubElement(p11, "textattr")
    p15.set('colour', 'Black')
    p15.set('bold', 'false')
    p16 = ET.SubElement(p11, "text")
    p16.set('tool', 'CPN Tools')
    p16.set('version', '4.0.1')
    p16.text = type

    id = update_id(id)

    p17 = ET.SubElement(p1, "initmark")
    p17.set('id', id)
    p18 = ET.SubElement(p17, "posattr")
    p18.set('x', x3)
    p18.set('y', y3)
    p19 = ET.SubElement(p17, "fillattr")
    p19.set('colour', 'White')
    p19.set('pattern', 'Solid')
    p19.set('filled', 'false')
    p20 = ET.SubElement(p17, "lineattr")
    p20.set('colour', 'Black')
    p20.set('thick', '0')
    p20.set('type', 'Solid')
    p21 = ET.SubElement(p17, "textattr")
    p21.set('colour', 'Black')
    p21.set('bold', 'false')
    p22 = ET.SubElement(p17, "text")
    p22.set('tool', 'CPN Tools')
    p22.set('version', '4.0.1')
    if name == 'start':
        p22.text = '1`true'

    if use_horizontal == False:
        update_y()
    else:
        update_x()

def create_parallel_elipse(name, type, att):
    
    global main_operator
    global op
    global id
    global has_operator
    global y1
    global x1
    
    id = create_id()
    
    if has_operator == False:
        y1 = main_operator[op][5]
        y2 = int(main_operator[op][5]) - 30
        y2 = str(y2)
        y3 = int(main_operator[op][5]) + 27
        y3 = str(y3)

        x1 = main_operator[op][4]
        x2 = int(float(main_operator[op][4])) + 32.5
        x2 = str(x2)
        x3 = int(float(main_operator[op][4])) + 56
        x3 = str(x3)
    else:
        y1 = parallel_y
        y2 = float(parallel_y) - 30
        y2 = str(y2)
        y3 = float(parallel_y) + 27
        y3 = str(y3)

        x1 = parallel_x
        x2 = float(parallel_x) + 32.5
        x2 = str(x2)
        x3 = float(parallel_x) + 56
        x3 = str(x3)
    
    # print(f"parallel_x elipse = {trans_1_x}")

    pe1 = ET.SubElement(b37, "place")
    pe1.set('id', id)
    pe2 = ET.SubElement(pe1, "posattr")
    pe2.set('x', x1)
    pe2.set('y', y1)
    pe3 = ET.SubElement(pe1, "fillattr")
    pe3.set('colour', 'White')
    pe3.set('pattern', '')
    pe3.set('filled', 'false')
    pe4 = ET.SubElement(pe1, "lineattr")
    pe4.set('colour', 'Black')
    pe4.set('thick', '1')
    pe4.set('type', 'solid')
    pe5 = ET.SubElement(pe1, "textattr")
    pe5.set('colour', 'Black')
    pe5.set('bold', 'false')
    pe6 = ET.SubElement(pe1, "text")
    pe6.text = name
    pe7 = ET.SubElement(pe1, "ellipse")
    pe7.set('w', '75.000000')
    pe7.set('h', '40.000000')
    pe8 = ET.SubElement(pe1, "token")
    pe8.set('x', '-10.000000')
    pe8.set('y', '0.000000')
    pe9 = ET.SubElement(pe1, "marking")
    pe9.set('x', '0.000000')
    pe9.set('y', '0.000000')
    pe9.set('hidden', 'true')
    pe10 = ET.SubElement(pe9, "snap")
    pe10.set('snap_id', '0')
    pe10.set('anchor.horizontal', '0')
    pe10.set('anchor.vertical', '0')

    update_elipse(id)
    
    id = update_id(id)
    
    pe11 = ET.SubElement(pe1, "type")
    pe11.set('id', id)
    pe12 = ET.SubElement(pe11, "posattr")
    pe12.set('x', x2)
    pe12.set('y', y2)
    pe13 = ET.SubElement(pe11, "fillattr")
    pe13.set('colour', 'White')
    pe13.set('pattern', 'Solid')
    pe13.set('filled', 'false')
    pe14 = ET.SubElement(pe11, "lineattr")
    pe14.set('colour', 'Black')
    pe14.set('thick', '0')
    pe14.set('type', 'Solid')
    pe15 = ET.SubElement(pe11, "textattr")
    pe15.set('colour', 'Black')
    pe15.set('bold', 'false')
    pe16 = ET.SubElement(pe11, "text")
    pe16.set('tool', 'CPN Tools')
    pe16.set('version', '4.0.1')
    pe16.text = type

    id = update_id(id)

    pe17 = ET.SubElement(pe1, "initmark")
    pe17.set('id', id)
    pe18 = ET.SubElement(pe17, "posattr")
    pe18.set('x', x3)
    pe18.set('y', y3)
    pe19 = ET.SubElement(pe17, "fillattr")
    pe19.set('colour', 'White')
    pe19.set('pattern', 'Solid')
    pe19.set('filled', 'false')
    pe20 = ET.SubElement(pe17, "lineattr")
    pe20.set('colour', 'Black')
    pe20.set('thick', '0')
    pe20.set('type', 'Solid')
    pe21 = ET.SubElement(pe17, "textattr")
    pe21.set('colour', 'Black')
    pe21.set('bold', 'false')
    pe22 = ET.SubElement(pe17, "text")
    pe22.set('tool', 'CPN Tools')
    pe22.set('version', '4.0.1')

    if att == True:
        update_y()
    if has_operator == False:
        update_parallel_x()

def create_choice_elipse(name, type, att):
    
    global id
    
    id = create_id()
    
    y2 = int(choice_y) - 30
    y2 = str(y2)
    y3 = int(choice_y) + 27
    y3 = str(y3)

    x2 = int(float(choice_x)) + 32.5
    x2 = str(x2)
    x3 = int(float(choice_x)) + 56
    x3 = str(x3)

    pe1 = ET.SubElement(b37, "place")
    pe1.set('id', id)
    pe2 = ET.SubElement(pe1, "posattr")
    if has_operator == False:
        pe2.set('x', choice_x)
    else:
        pe2.set('x', horizontal_x)
    pe2.set('y', choice_y)
    pe3 = ET.SubElement(pe1, "fillattr")
    pe3.set('colour', 'White')
    pe3.set('pattern', '')
    pe3.set('filled', 'false')
    pe4 = ET.SubElement(pe1, "lineattr")
    pe4.set('colour', 'Black')
    pe4.set('thick', '1')
    pe4.set('type', 'solid')
    pe5 = ET.SubElement(pe1, "textattr")
    pe5.set('colour', 'Black')
    pe5.set('bold', 'false')
    pe6 = ET.SubElement(pe1, "text")
    pe6.text = name
    pe7 = ET.SubElement(pe1, "ellipse")
    pe7.set('w', '75.000000')
    pe7.set('h', '40.000000')
    pe8 = ET.SubElement(pe1, "token")
    pe8.set('x', '-10.000000')
    pe8.set('y', '0.000000')
    pe9 = ET.SubElement(pe1, "marking")
    pe9.set('x', '0.000000')
    pe9.set('y', '0.000000')
    pe9.set('hidden', 'true')
    pe10 = ET.SubElement(pe9, "snap")
    pe10.set('snap_id', '0')
    pe10.set('anchor.horizontal', '0')
    pe10.set('anchor.vertical', '0')

    update_elipse(id)
    
    id = update_id(id)
    
    pe11 = ET.SubElement(pe1, "type")
    pe11.set('id', id)
    pe12 = ET.SubElement(pe11, "posattr")
    pe12.set('x', x2)
    pe12.set('y', y2)
    pe13 = ET.SubElement(pe11, "fillattr")
    pe13.set('colour', 'White')
    pe13.set('pattern', 'Solid')
    pe13.set('filled', 'false')
    pe14 = ET.SubElement(pe11, "lineattr")
    pe14.set('colour', 'Black')
    pe14.set('thick', '0')
    pe14.set('type', 'Solid')
    pe15 = ET.SubElement(pe11, "textattr")
    pe15.set('colour', 'Black')
    pe15.set('bold', 'false')
    pe16 = ET.SubElement(pe11, "text")
    pe16.set('tool', 'CPN Tools')
    pe16.set('version', '4.0.1')
    pe16.text = type

    id = update_id(id)

    pe17 = ET.SubElement(pe1, "initmark")
    pe17.set('id', id)
    pe18 = ET.SubElement(pe17, "posattr")
    pe18.set('x', x3)
    pe18.set('y', y3)
    pe19 = ET.SubElement(pe17, "fillattr")
    pe19.set('colour', 'White')
    pe19.set('pattern', 'Solid')
    pe19.set('filled', 'false')
    pe20 = ET.SubElement(pe17, "lineattr")
    pe20.set('colour', 'Black')
    pe20.set('thick', '0')
    pe20.set('type', 'Solid')
    pe21 = ET.SubElement(pe17, "textattr")
    pe21.set('colour', 'Black')
    pe21.set('bold', 'false')
    pe22 = ET.SubElement(pe17, "text")
    pe22.set('tool', 'CPN Tools')
    pe22.set('version', '4.0.1')

    if att == True:
        update_choice_y()

def create_trans(name, use_horizontal, guard):
    
    global id
    global transitions
    global y1
    global x1
    global trans_y
    global trans_x
    global curr_mission
    global t14
    
    id = create_id()

    if use_horizontal == False:
        if has_operator == False:
            y1 = elipse_y
            y2 = int(elipse_y) - 30
            y2 = str(y2)
            y3 = int(elipse_y) + 27
            y3 = str(y3)

            x1 = elipse_x
            x2 = int(elipse_x) + 32.5
            x2 = str(x2)
            x3 = int(elipse_x) + 56
            x3 = str(x3)
        else:
            y1 = trans_1_y
            y2 = float(trans_1_y) - 30
            y2 = str(y2)
            y3 = float(trans_1_y) + 27
            y3 = str(y3)
            
            x1 = horizontal_x
            x2 = float(trans_1_x) + 32.5
            x2 = str(x2)
            x3 = float(trans_1_x) + 56
            x3 = str(x3)
            
    elif use_horizontal == True or has_operator == True:
        y1 = trans_1_y
        y2 = int(trans_1_y) - 30
        y2 = str(y2)
        y3 = int(trans_1_y) + 27
        y3 = str(y3)

        x1 = horizontal_x
        x2 = float(horizontal_x) + 32.5
        x2 = str(x2)
        x3 = float(horizontal_x) + 56
        x3 = str(x3)
        
        # num = len(parent.childNodes)
        # print(num)

    t1 = ET.SubElement(b37, "trans")
    t1.set('id', id)
    t2 = ET.SubElement(t1, "posattr")
    t2.set('x', x1)
    t2.set('y', y1)
    t3 = ET.SubElement(t1, "fillattr")
    t3.set('colour', 'White')
    t3.set('pattern', '')
    t3.set('filled', 'false')
    t4 = ET.SubElement(t1, "lineattr")
    t4.set('colour', 'Black')
    t4.set('thick', '1')
    t4.set('type', 'solid')
    t5 = ET.SubElement(t1, "textattr")
    t5.set('colour', 'Black')
    t5.set('bold', 'false')
    t6 = ET.SubElement(t1, "text")
    t6.text = name
    t7 = ET.SubElement(t1, "box")
    t7.set('w', '60.000000')
    t7.set('h', '40.000000')
    t8 = ET.SubElement(t1, "binding")
    t8.set('x', '7.200000')
    t8.set('y', '-3.000000')

    update_trans(id)

    id = update_id(id)

    t9 = ET.SubElement(t1, "cond")
    t9.set('id', id)
    t10 = ET.SubElement(t9, "posattr")
    if use_horizontal == False:
        t10.set('x', '130.000000')
        t10.set('y', y1)
    else:
        t10.set('x', horizontal_x)
        t10.set('y', str(float(y1)+30))
    t11 = ET.SubElement(t9, "fillattr")
    t11.set('colour', 'White')
    t11.set('pattern', 'Solid')
    t11.set('filled', 'false')
    t12 = ET.SubElement(t9, "lineattr")
    t12.set('colour', 'Black')
    t12.set('thick', '0')
    t12.set('type', 'Solid')
    t13 = ET.SubElement(t9, "textattr")
    t13.set('colour', 'Black')
    t13.set('bold', 'false')
    t14 = ET.SubElement(t9, "text")
    t14.set('tool', 'CPN Tools')
    t14.set('version', '4.0.1')
    # if transitions == 1:
    #     t14.text = functions[-1]
    # else:
    #     t14.text = guard

    id = update_id(id)

    t15 = ET.SubElement(t1, "time")
    t15.set('id', id)
    t16 = ET.SubElement(t15, "posattr")
    t16.set('x', x3)
    t16.set('y', y3)
    t17 = ET.SubElement(t15, "fillattr")
    t17.set('colour', 'White')
    t17.set('pattern', 'Solid')
    t17.set('filled', 'false')
    t18 = ET.SubElement(t15, "lineattr")
    t18.set('colour', 'Black')
    t18.set('thick', '0')
    t18.set('type', 'Solid')
    t19 = ET.SubElement(t15, "textattr")
    t19.set('colour', 'Black')
    t19.set('bold', 'false')
    t20 = ET.SubElement(t15, "text")
    t20.set('tool', 'CPN Tools')
    t20.set('version', '4.0.1')

    id = update_id(id)

    t21 = ET.SubElement(t1, "code")
    t21.set('id', id)
    t22 = ET.SubElement(t21, "posattr")
    t22.set('x', '80.000000')
    t22.set('y', '0.000000')
    t23 = ET.SubElement(t21, "fillattr")
    t23.set('colour', 'White')
    t23.set('pattern', 'Solid')
    t23.set('filled', 'false')
    t24 = ET.SubElement(t21, "lineattr")
    t24.set('colour', 'Black')
    t24.set('thick', '0')
    t24.set('type', 'Solid')
    t25 = ET.SubElement(t21, "textattr")
    t25.set('colour', 'Black')
    t25.set('bold', 'false')
    t26 = ET.SubElement(t21, "text")
    t26.set('tool', 'CPN Tools')

    id = update_id(id)

    t27 = ET.SubElement(t1, "priority")
    t27.set('id', id)
    t28 = ET.SubElement(t27, "posattr")
    t28.set('x', '80.000000')
    t28.set('y', '0.000000')
    t29 = ET.SubElement(t27, "fillattr")
    t29.set('colour', 'White')
    t29.set('pattern', 'Solid')
    t29.set('filled', 'false')
    t30 = ET.SubElement(t27, "lineattr")
    t30.set('colour', 'Black')
    t30.set('thick', '0')
    t30.set('type', 'Solid')
    t31 = ET.SubElement(t27, "textattr")
    t31.set('colour', 'Black')
    t31.set('bold', 'false')
    t32 = ET.SubElement(t27, "text")
    t32.set('tool', 'CPN Tools')
    t32.set('version', '4.0.1')
    
    transitions += 1
    trans_y = y1
    trans_x = x1

    if use_horizontal == False:
        update_y()
    else:
        update_x()

def create_choice_trans(name, save):
    
    global id
    global t14
    global transitions
    global trans_y
    global trans_x
    global x
    
    id = create_id()
    
    y2 = int(choice_y) - 30
    y2 = str(y2)

    y3 = int(choice_y) + 27
    y3 = str(y3)
    
    print(f'choice_x = {choice_x}')
    text_x = str(int(float(choice_x)) * 2.5)
    print(f'text_x = {text_x}')

    t1 = ET.SubElement(b37, "trans")
    t1.set('id', id)
    t2 = ET.SubElement(t1, "posattr")
    t2.set('x', choice_x)
    t2.set('y', choice_y)
    t3 = ET.SubElement(t1, "fillattr")
    t3.set('colour', 'White')
    t3.set('pattern', '')
    t3.set('filled', 'false')
    t4 = ET.SubElement(t1, "lineattr")
    t4.set('colour', 'Black')
    t4.set('thick', '1')
    t4.set('type', 'solid')
    t5 = ET.SubElement(t1, "textattr")
    t5.set('colour', 'Black')
    t5.set('bold', 'false')
    t6 = ET.SubElement(t1, "text")
    t6.text = name
    t7 = ET.SubElement(t1, "box")
    t7.set('w', '60.000000')
    t7.set('h', '40.000000')
    t8 = ET.SubElement(t1, "binding")
    t8.set('x', '7.200000')
    t8.set('y', '-3.000000')
    
    if save == True:
        main_operator[op][8].append(id)
    update_trans(id)

    id = update_id(id)

    t9 = ET.SubElement(t1, "cond")
    t9.set('id', id)
    t10 = ET.SubElement(t9, "posattr")
    t10.set('x', text_x)
    t10.set('y', choice_y)
    t11 = ET.SubElement(t9, "fillattr")
    t11.set('colour', 'White')
    t11.set('pattern', 'Solid')
    t11.set('filled', 'false')
    t12 = ET.SubElement(t9, "lineattr")
    t12.set('colour', 'Black')
    t12.set('thick', '0')
    t12.set('type', 'Solid')
    t13 = ET.SubElement(t9, "textattr")
    t13.set('colour', 'Black')
    t13.set('bold', 'false')
    t14 = ET.SubElement(t9, "text")
    t14.set('tool', 'CPN Tools')
    t14.set('version', '4.0.1')

    id = update_id(id)

    t15 = ET.SubElement(t1, "time")
    t15.set('id', id)
    t16 = ET.SubElement(t15, "posattr")
    t16.set('x', '56.000000')
    t16.set('y', y3)
    t17 = ET.SubElement(t15, "fillattr")
    t17.set('colour', 'White')
    t17.set('pattern', 'Solid')
    t17.set('filled', 'false')
    t18 = ET.SubElement(t15, "lineattr")
    t18.set('colour', 'Black')
    t18.set('thick', '0')
    t18.set('type', 'Solid')
    t19 = ET.SubElement(t15, "textattr")
    t19.set('colour', 'Black')
    t19.set('bold', 'false')
    t20 = ET.SubElement(t15, "text")
    t20.set('tool', 'CPN Tools')
    t20.set('version', '4.0.1')

    id = update_id(id)

    t21 = ET.SubElement(t1, "code")
    t21.set('id', id)
    t22 = ET.SubElement(t21, "posattr")
    t22.set('x', '80.000000')
    t22.set('y', '0.000000')
    t23 = ET.SubElement(t21, "fillattr")
    t23.set('colour', 'White')
    t23.set('pattern', 'Solid')
    t23.set('filled', 'false')
    t24 = ET.SubElement(t21, "lineattr")
    t24.set('colour', 'Black')
    t24.set('thick', '0')
    t24.set('type', 'Solid')
    t25 = ET.SubElement(t21, "textattr")
    t25.set('colour', 'Black')
    t25.set('bold', 'false')
    t26 = ET.SubElement(t21, "text")
    t26.set('tool', 'CPN Tools')

    id = update_id(id)

    t27 = ET.SubElement(t1, "priority")
    t27.set('id', id)
    t28 = ET.SubElement(t27, "posattr")
    t28.set('x', '80.000000')
    t28.set('y', '0.000000')
    t29 = ET.SubElement(t27, "fillattr")
    t29.set('colour', 'White')
    t29.set('pattern', 'Solid')
    t29.set('filled', 'false')
    t30 = ET.SubElement(t27, "lineattr")
    t30.set('colour', 'Black')
    t30.set('thick', '0')
    t30.set('type', 'Solid')
    t31 = ET.SubElement(t27, "textattr")
    t31.set('colour', 'Black')
    t31.set('bold', 'false')
    t32 = ET.SubElement(t27, "text")
    t32.set('tool', 'CPN Tools')
    t32.set('version', '4.0.1')
    
    trans_y = choice_y
    trans_x = choice_x
    transitions += 1

def create_arc(is_place_to_trans, operator):
    global node
    global transitions
    global curr_mission
    global elipse_id
    global trans_id
    global elipse_y
    global arc_y
    global arc_x
    global id
    global main_operator
    global op
    
    id = create_id()
    
    # print("\nCREATING NORMAL ARC\n")
    
    # print(f"ARC CURR MISSION = {curr_mission}")
    
    if operator == 'choice':
        arc_x = int(float(choice_x))
        arc_x = str(arc_x)
        arc_y = int(float(choice_y)) + 55
        arc_y = str(arc_y)
    else:
        arc_x = '0'
        arc_y = float(elipse_y) + 150
        arc_y = str(arc_y)

    if curr_mission == 'BOOL':
        if is_place_to_trans == True:
            aux = 'b'
        else:
            aux = '1`true'
    else:
        index = n_missions.index(curr_mission)
        aux = str(functions[index])
                
    # if is_place_to_trans == True:
    #     print(f'\ncreating arc between {node.getAttribute('id')} and t{transitions-1}')
    # else:
    #     print(f'\ncreating arc between t{transitions-1} and {node.getAttribute('id')}')
        
    # print(f'curr_mission = {curr_mission} and text = {aux}\n')
        
    # arc_x += (len(aux)*3)
    # arc_x = str(arc_x)

    a1 = ET.SubElement(b37, "arc")
    a1.set('id', id)
    if is_place_to_trans == True:
        a1.set('orientation', 'PtoT')
    else:
        a1.set('orientation', 'TtoP')
    a1.set('order', '1')
    a2 = ET.SubElement(a1, "posattr")
    a2.set('x', '0.000000')
    a2.set('y', '0.000000')
    a3 = ET.SubElement(a1, "fillattr")
    a3.set('colour', 'White')
    a3.set('pattern', '')
    a3.set('filled', 'false')
    a4 = ET.SubElement(a1, "lineattr")
    a4.set('colour', 'Black')
    a4.set('thick', '1')
    a4.set('type', 'solid')
    a5 = ET.SubElement(a1, "textattr")
    a5.set('colour', 'Black')
    a5.set('bold', 'false')
    a6 = ET.SubElement(a1, "arrowattr")
    a6.set('headsize', '1.200000')
    a6.set('currentcyckle', '2')
    a7 = ET.SubElement(a1, "transend")
    a7.set ('idref', trans_id)
    a8 = ET.SubElement(a1, "placeend")
    a8.set('idref', elipse_id)

    id = update_id(id)

    a9 = ET.SubElement(a1, "annot")
    a9.set('id', id)
    a10 = ET.SubElement(a9, "posattr")
    a10.set('x', arc_x)
    a10.set('y', arc_y)
    a11 = ET.SubElement(a9, "fillattr")
    a11.set('colour', 'White')
    a11.set('pattern', 'Solid')
    a11.set('filled', 'false')
    a12 = ET.SubElement(a9, "lineattr")
    a12.set('colour', 'Black')
    a12.set('thick', '0')
    a12.set('type', 'Solid')
    a13 = ET.SubElement(a9, "textattr")
    a13.set('colour', 'Black')
    a13.set('bold', 'false')
    a14 = ET.SubElement(a9, "text")
    a14.set('tool', 'CPN Tools')
    a14.set('version', '4.0.1')
    a14.text = aux
    
    update_arc()

def create_first_choice_arc():
    global transitions
    global elipse_id
    global trans_id
    global elipse_y
    global arc_y
    global arc_x
    global id
    global main_operator
    global op
    
    id = create_id()
    
    # print("\nCREATING NORMAL ARC\n")
    
    # print(f"ARC CURR MISSION = {curr_mission}")
    
    arc_x = int(float(choice_x))
    arc_x = str(arc_x)
    arc_y = int(float(choice_y)) + 55
    arc_y = str(arc_y)

    # print(f'\ncreating first choice arc between {stored_node.getAttribute('id')} and t{transitions-1}')

    stored_node_mission = find_node_mission(stored_node)

    if stored_node_mission == 'BOOL':
        aux = 'b'
    else:
        index = n_missions.index(stored_node_mission)
        aux = str(functions[index])
        
    # print(f"\nSTORED NODE ({stored_node.getAttribute('id')}) MISSION = {stored_node_mission} FUNCTION = {aux}\n")
        
    # arc_x += (len(aux)*3)
    # arc_x = str(arc_x)

    a1 = ET.SubElement(b37, "arc")
    a1.set('id', id)
    a1.set('orientation', 'PtoT')
    a1.set('order', '1')
    a2 = ET.SubElement(a1, "posattr")
    a2.set('x', '0.000000')
    a2.set('y', '0.000000')
    a3 = ET.SubElement(a1, "fillattr")
    a3.set('colour', 'White')
    a3.set('pattern', '')
    a3.set('filled', 'false')
    a4 = ET.SubElement(a1, "lineattr")
    a4.set('colour', 'Black')
    a4.set('thick', '1')
    a4.set('type', 'solid')
    a5 = ET.SubElement(a1, "textattr")
    a5.set('colour', 'Black')
    a5.set('bold', 'false')
    a6 = ET.SubElement(a1, "arrowattr")
    a6.set('headsize', '1.200000')
    a6.set('currentcyckle', '2')
    a7 = ET.SubElement(a1, "transend")
    a7.set ('idref', trans_id)
    a8 = ET.SubElement(a1, "placeend")
    a8.set('idref', elipse_id)

    id = update_id(id)

    a9 = ET.SubElement(a1, "annot")
    a9.set('id', id)
    a10 = ET.SubElement(a9, "posattr")
    a10.set('x', arc_x)
    a10.set('y', arc_y)
    a11 = ET.SubElement(a9, "fillattr")
    a11.set('colour', 'White')
    a11.set('pattern', 'Solid')
    a11.set('filled', 'false')
    a12 = ET.SubElement(a9, "lineattr")
    a12.set('colour', 'Black')
    a12.set('thick', '0')
    a12.set('type', 'Solid')
    a13 = ET.SubElement(a9, "textattr")
    a13.set('colour', 'Black')
    a13.set('bold', 'false')
    a14 = ET.SubElement(a9, "text")
    a14.set('tool', 'CPN Tools')
    a14.set('version', '4.0.1')
    a14.text = aux
    
    update_arc()

def create_first_arc(operator):
    global curr_mission
    global elipse_id
    global trans_1
    global trans_1_x
    global arc_y
    global parallel_x
    global id
    global had_operator
    global y1
    global x1
    
    
    # if main_operator[op-1][0].getAttribute('operator') == 'parallel':
    #     print(f"IF MAIN_OPERATOR[{op}][2] = {main_operator[op][2]}")
    #     trans_1 = main_operator[op-1][2]
    #     print(f"\nNEW MAIN OPERATOR COMING FROM main_operator[{op-1}][2] = {trans_1}")
    # else:
    if main_operator[op][2] != 'trans_1_id':
        trans_1 = main_operator[op][2]
        # print(f"\nNEW ELSE OPERATOR COMING FROM main_operator[{op}][2] = {trans_1}")
    
    id = create_id()
    
    if curr_mission == 'BOOL':
        aux = 'b'
    else:
        index = n_missions.index(curr_mission)
        aux = str(functions[index])

    if has_operator == False:
        par_arc_y = int(float(main_operator[op][5])) + 55
        par_arc_y = str(par_arc_y)
    else:
        par_arc_y = trans_y
        trans_1_x = trans_x

    # print(f"parallel_x arc = {trans_1_x}")

    af1 = ET.SubElement(b37, "arc")
    af1.set('id', id)
    af1.set('orientation', 'TtoP')
    af1.set('order', '1')
    af2 = ET.SubElement(af1, "posattr")
    af2.set('x', '0.000000')
    af2.set('y', '0.000000')
    af3 = ET.SubElement(af1, "fillattr")
    af3.set('colour', 'White')
    af3.set('pattern', '')
    af3.set('filled', 'false')
    af4 = ET.SubElement(af1, "lineattr")
    af4.set('colour', 'Black')
    af4.set('thick', '1')
    af4.set('type', 'solid')
    af5 = ET.SubElement(af1, "textattr")
    af5.set('colour', 'Black')
    af5.set('bold', 'false')
    af6 = ET.SubElement(af1, "arrowattr")
    af6.set('headsize', '1.200000')
    af6.set('currentcyckle', '2')
    af7 = ET.SubElement(af1, "transend")
    if (had_operator == True) and (operator == 'sequence' or operator == 'parallel'):
        af7.set ('idref', trans_id)
        had_operator = False
        # print(f"\nCREATING FIRST ARC FROM {trans_id} TO {elipse_id}\n")
    else:
        af7.set ('idref', trans_1)
        # print(f"\nCREATING FIRST ARC FROM {trans_1} TO {elipse_id}\n")
    af8 = ET.SubElement(af1, "placeend")
    af8.set('idref', elipse_id)

    id = update_id(id)

    af9 = ET.SubElement(af1, "annot")
    af9.set('id', id)
    af10 = ET.SubElement(af9, "posattr")
    af10.set('x', trans_1_x)
    af10.set('y', par_arc_y)
    af11 = ET.SubElement(af9, "fillattr")
    af11.set('colour', 'White')
    af11.set('pattern', 'Solid')
    af11.set('filled', 'false')
    af12 = ET.SubElement(af9, "lineattr")
    af12.set('colour', 'Black')
    af12.set('thick', '0')
    af12.set('type', 'Solid')
    af13 = ET.SubElement(af9, "textattr")
    af13.set('colour', 'Black')
    af13.set('bold', 'false')
    af14 = ET.SubElement(af9, "text")
    af14.set('tool', 'CPN Tools')
    af14.set('version', '4.0.1')
    af14.text = aux
    
    update_arc()

def create_second_arc():
    global elipse_id
    global id
    global main_operator
    global op
    global parallel_x
    
    id = create_id()
    
    if curr_mission == 'BOOL':
        aux = 'b'
    else:
        index = n_missions.index(curr_mission)
        aux = str(functions[index])
    
    par_arc_y = int(float(main_operator[op][5])) - 55
    par_arc_y = str(par_arc_y)
    
    # print(f"\nCREATING FIRST ARC FROM {elipse_id} TO {main_operator[op][3]}\n")

    as1 = ET.SubElement(b37, "arc")
    as1.set('id', id)
    as1.set('orientation', 'PtoT')
    as1.set('order', '1')
    as2 = ET.SubElement(as1, "posattr")
    as2.set('x', '0.000000')
    as2.set('y', '0.000000')
    as3 = ET.SubElement(as1, "fillattr")
    as3.set('colour', 'White')
    as3.set('pattern', '')
    as3.set('filled', 'false')
    as4 = ET.SubElement(as1, "lineattr")
    as4.set('colour', 'Black')
    as4.set('thick', '1')
    as4.set('type', 'solid')
    as5 = ET.SubElement(as1, "textattr")
    as5.set('colour', 'Black')
    as5.set('bold', 'false')
    as6 = ET.SubElement(as1, "arrowattr")
    as6.set('headsize', '1.200000')
    as6.set('currentcyckle', '2')
    as7 = ET.SubElement(as1, "transend")
    as7.set ('idref', main_operator[op][3])
    as8 = ET.SubElement(as1, "placeend")
    as8.set('idref', elipse_id)

    id = update_id(id)

    as9 = ET.SubElement(as1, "annot")
    as9.set('id', id)
    as10 = ET.SubElement(as9, "posattr")
    as10.set('x', trans_1_x)
    as10.set('y', par_arc_y)
    as11 = ET.SubElement(as9, "fillattr")
    as11.set('colour', 'White')
    as11.set('pattern', 'Solid')
    as11.set('filled', 'false')
    as12 = ET.SubElement(as9, "lineattr")
    as12.set('colour', 'Black')
    as12.set('thick', '0')
    as12.set('type', 'Solid')
    as13 = ET.SubElement(as9, "textattr")
    as13.set('colour', 'Black')
    as13.set('bold', 'false')
    as14 = ET.SubElement(as9, "text")
    as14.set('tool', 'CPN Tools')
    as14.set('version', '4.0.1')
    as14.text = aux

    update_arc()
    update_x()

def create_choice_arc():
    global curr_mission
    global elipse_id
    global trans_choice
    global id
    global start_choice_x
    global arc_x
    
    id = create_id()

    arc_y = int(float(last_choice_y)) - 55
    arc_y = str(arc_y)

    trans = str(trans_choice[len(trans_choice)-1])
    
    # print(f"\nCREATING CHOICE ARC FROM {trans} TO {elipse_id}\n")
    trans_choice.pop()
    
    # print(f'elipse_id = {elipse_id}')
    # print(f'trans = {trans}')

    a1 = ET.SubElement(b37, "arc")
    a1.set('id', id)
    a1.set('orientation', 'TtoP')
    a1.set('order', '1')
    a2 = ET.SubElement(a1, "posattr")
    a2.set('x', '0.000000')
    a2.set('y', '0.000000')
    a3 = ET.SubElement(a1, "fillattr")
    a3.set('colour', 'White')
    a3.set('pattern', '')
    a3.set('filled', 'false')
    a4 = ET.SubElement(a1, "lineattr")
    a4.set('colour', 'Black')
    a4.set('thick', '1')
    a4.set('type', 'solid')
    a5 = ET.SubElement(a1, "textattr")
    a5.set('colour', 'Black')
    a5.set('bold', 'false')
    a6 = ET.SubElement(a1, "arrowattr")
    a6.set('headsize', '1.200000')
    a6.set('currentcyckle', '2')
    a7 = ET.SubElement(a1, "transend")
    a7.set ('idref', trans)
    a8 = ET.SubElement(a1, "placeend")
    a8.set('idref', elipse_id)

    id = update_id(id)

    a9 = ET.SubElement(a1, "annot")
    a9.set('id', id)
    a10 = ET.SubElement(a9, "posattr")
    a10.set('x', str(start_choice_x))
    a10.set('y', arc_y)
    a11 = ET.SubElement(a9, "fillattr")
    a11.set('colour', 'White')
    a11.set('pattern', 'Solid')
    a11.set('filled', 'false')
    a12 = ET.SubElement(a9, "lineattr")
    a12.set('colour', 'Black')
    a12.set('thick', '0')
    a12.set('type', 'Solid')
    a13 = ET.SubElement(a9, "textattr")
    a13.set('colour', 'Black')
    a13.set('bold', 'false')
    a14 = ET.SubElement(a9, "text")
    a14.set('tool', 'CPN Tools')
    a14.set('version', '4.0.1')
    if curr_mission == 'BOOL':
        a14.text = '1`true'
    else:
        index = n_missions.index(curr_mission)
        a14.text = str(functions[index])

def create_variables():
    v1 = ET.SubElement(b10, "color")
    id = create_id()
    v1.set('id', id)
    v2 = ET.SubElement(v1, "id")
    v2.text = 'R'
    v3 = ET.SubElement(v1, "enum")
    string = 'colset R = with '
    # print(struct_spec)
    for i in range(0, len(struct_spec)):
        for j in range(len(struct_spec[i])):
            if j > 0:
                v4 = ET.SubElement(v3, "id")
                v4.text = str(struct_spec[i][j])
                if (j > 1):
                    string += ' | '
                string += str(struct_spec[i][j])
    string += ';'
    v5 = ET.SubElement(v1, "layout")

    v5.text = string
    v6 = ET.SubElement(b10, "color")
    id = create_id()
    v6.set('id', id)
    v7 = ET.SubElement(v6, "id")
    v7.text = 'G'
    v8 = ET.SubElement(v6, "enum")
    for i in range(0, len(struct_spec)):
        v9 = ET.SubElement(v8, "id")
        v9.text = struct_spec[i][0]
    v10 = ET.SubElement(v6, "layout")
    string = 'colset G = with '
    for i in range(0, len(struct_spec)):
        string += struct_spec[i][0]
        if i != len(struct_spec)-1:
            string += ' | '
    string += ';'    
    v10.text = string
    
    v100 = ET.SubElement(b10, "color")
    id = create_id()
    v100.set('id', id)
    v101 = ET.SubElement(v100, "id")
    v101.text = 'ROLES'
    v102 = ET.SubElement(v100, "list")
    v103 = ET.SubElement(v102, "id")
    v103.text = 'R'
    v104 = ET.SubElement(v100, "layout")
    v104.text = 'colset ROLES = list R;'

    v11 = ET.SubElement(b10, "color")
    id = create_id()
    v11.set('id', id)
    v12 = ET.SubElement(v11, "id")
    v12.text = "RG"
    v13 = ET.SubElement(v11, "product")
    v14 = ET.SubElement(v13, "id")
    v14.text = "R"
    v15 = ET.SubElement(v13, "id")
    v15.text = "G"
    v16 = ET.SubElement(v11, "layout")
    v16.text = "colset RG = product R * G ;"

    v17 = ET.SubElement(b10, "var")
    id = create_id()
    v17.set('id', id)
    v18 = ET.SubElement(v17, "type")
    v19 = ET.SubElement(v18, "id")
    v19.text = "RG"
    string = "var "
    cont = 0
    for i in range(0, len(struct_spec)):
        for j in range(0, len(struct_spec[i])):
            if i == 0 and j == 1:
                string += "r" + str(cont+1)
                v20 = ET.SubElement(v17, "id")
                v20.text = "r" + str(cont+1)
                cont += 1
            elif j > 0:
                string += ", r" + str(cont+1)
                v20 = ET.SubElement(v17, "id")
                v20.text = "r" + str(cont+1)
                cont += 1
    string += " : RG;"
    v21 = ET.SubElement(v17, "layout")
    v21.text = string
    
    v22 = ET.SubElement(b10, "var")
    id = create_id()
    v22.set('id', id)
    v23 = ET.SubElement(v22, "type")
    v24 = ET.SubElement(v23, "id")
    v24.text = "BOOL"
    v25 = ET.SubElement(v22, "id")
    v25.text = "b"
    v26 = ET.SubElement(v22, "layout")
    v26.text = "var b : BOOL;"
    
    for i in range(0, len(struct_spec)):
        for j in range(0, len(struct_spec[i])):
            v27 = ET.SubElement(b10, "ml")
            id = create_id()
            v27.set('id', id)
            v27.text = "val N" + struct_spec[i][j] + " = 1;"
            v28 = ET.SubElement(v27, "layout")
            v28.text = "val N" + struct_spec[i][j] + " = 1;"
        
    for i in range(0, len(n_missions)):
        v29 = ET.SubElement(b10, "ml")
        id = create_id()
        v29.set('id', id)
        v29.text = "val Cmax_" + str(n_missions[i][:4] + " = 1;")
        v30 = ET.SubElement(v29, "layout")
        v30.text = "val Cmax_" + str(n_missions[i][:4] + " = 1;")
        
        v31 = ET.SubElement(b10, "ml")
        id = create_id()
        v31.set('id', id)
        v31.text = "val Cmin_" + str(n_missions[i][:4] + " = 1;")
        v32 = ET.SubElement(v31, "layout")
        v32.text = "val Cmin_" + str(n_missions[i][:4] + " = 1;")
        
def create_functions():
    normatives = document.getElementsByTagName("normative-specification")[0]
    clear_node(normatives.childNodes)

    for i in range(0, len(normatives.childNodes)):
        cont = 1
        stop = False
        for j in range(0, len(struct_spec)):
            for k in range(1, len(struct_spec[j])):
                if struct_spec[j][k] == normatives.childNodes[i].getAttribute('role'):
                    # print(f'normatives.childNodes[{i}].getAttribute("role") = {normatives.childNodes[i].getAttribute("role")}')
                    stop = True
                if stop == False:
                    cont += 1
        v1 = ET.SubElement(b10, "ml")
        id = create_id()
        v1.set('id', id)
        string = 'fun Fm' + str(i+1) + "(r" + str(cont) + ") = if N" + normatives.childNodes[i].getAttribute('role') + " <= Cmax_" + normatives.childNodes[i].getAttribute('mission')[:4] + " then N" + normatives.childNodes[i].getAttribute('role') + "`r" + str(cont) + " else Cmax_" + normatives.childNodes[i].getAttribute('mission')[:4] + "`r" + str(cont) + ";"
        v1.text = string
        v2 = ET.SubElement(v1, "layout")
        v2.text = string
        string = "Fm" + str(i+1) + "(r" + str(cont) + ")"
        # print(short_functions)
        functions.append(string)
        # short_functions.append(string)
    
    string = ''
    for i in range(0, len(n_missions)):
        if i == 0:
            string = "Tmin_" + n_missions[i][:4] + "() andalso"
        else:
            string += "\nTmin_" + n_missions[i][:4] + "() andalso"
            
    functions.append(string)

    repeat = []

    for i in range(0, len(normatives.childNodes)):
        v3 = ET.SubElement(b10, "ml")
        id = create_id()
        v3.set('id', id)
        if normatives.childNodes[i].getAttribute('mission')[:4] not in repeat:
            
            repeat.append(normatives.childNodes[i].getAttribute('mission')[:4])
            string = 'fun Tmin_' + normatives.childNodes[i].getAttribute('mission')[:4] + '() = N' + normatives.childNodes[i].getAttribute('role') + ' >= Cmin_' + normatives.childNodes[i].getAttribute('mission')[:4] + ';'
        else:
            aux = normatives.childNodes[i].getAttribute('mission')[:4]
            for j in range(len(aux)):
                if aux[j].isnumeric() == True:
                    aux = aux.replace(aux[j], str(i+1))
            string = 'fun Tmin_' + aux + '() = N' + normatives.childNodes[i].getAttribute('role') + ' >= Cmin_' + normatives.childNodes[i].getAttribute('mission')[:4] + ';'
        v3.text = string
        v4 = ET.SubElement(v3, "layout")
        v4.text = string
#----#

def create_body():
    #---#

    b39 = ET.SubElement(m2, "instances")

    b40 = ET.SubElement(b39, "instance")
    b40.set('id', 'ID2149')
    b40.set('page', 'ID6')

    #---#

    b41 = ET.SubElement(m2, "options")

    #---#

    b42 = ET.SubElement(b41, "option")
    b42.set('name', 'realtimestamp')

    b43 = ET.SubElement(b42, "value")

    b44 = ET.SubElement(b43, "boolean")
    b44.text = "false"

    #---#

    b45 = ET.SubElement(b41, "option")
    b45.set('name', 'fair_be')

    b46 = ET.SubElement(b45, "value")

    b47 = ET.SubElement(b46, "boolean")
    b47.text = "false"

    #---#

    b48 = ET.SubElement(b41, "option")
    b48.set('name', 'global_fairness')

    b49 = ET.SubElement(b48, "value")

    b50 = ET.SubElement(b49, "boolean")
    b50.text = "false"

    #---#

    b51 = ET.SubElement(b41, "option")
    b51.set('name', 'outputdirectory')

    b52 = ET.SubElement(b51, "value")

    b53 = ET.SubElement(b52, "text")
    b53.text = "&lt;same as model&gt;"

    #---#

    b54 = ET.SubElement(b41, "option")
    b54.set('name', 'extensions.10002.enable')

    b55 = ET.SubElement(b54, "value")

    b56 = ET.SubElement(b55, "boolean")
    b56.text = "true"

    #---#

    b57 = ET.SubElement(b41, "option")
    b57.set('name', 'extensions.10005.enable')

    b58 = ET.SubElement(b57, "value")

    b59 = ET.SubElement(b58, "boolean")
    b59.text = "true"

    #---#

    b60 = ET.SubElement(b41, "option")
    b60.set('name', 'extensions.10003.enable')

    b61 = ET.SubElement(b60, "value")

    b62 = ET.SubElement(b61, "boolean")
    b62.text = "true"

    #---#

    b63 = ET.SubElement(b41, "option")
    b63.set('name', 'extensions.10006.enable')

    b64 = ET.SubElement(b63, "value")

    b65 = ET.SubElement(b64, "boolean")
    b65.text = "true"

    #---#

    b66 = ET.SubElement(b41, "option")
    b66.set('name', 'extensions.10001.enable')

    b67 = ET.SubElement(b66, "value")

    b68 = ET.SubElement(b67, "boolean")
    b68.text = "true"

    #---#

    b69 = ET.SubElement(b41, "option")
    b69.set('name', 'repavg')

    b70 = ET.SubElement(b69, "value")

    b71 = ET.SubElement(b70, "boolean")
    b71.text = "true"

    #---#

    b72 = ET.SubElement(b41, "option")
    b72.set('name', 'repciavg')

    b73 = ET.SubElement(b72, "value")

    b74 = ET.SubElement(b73, "boolean")
    b74.text = "true"

    #---#

    b300 = ET.SubElement(b41, "option")
    b300.set('name', 'repcount')

    b301 = ET.SubElement(b300, "value")

    b302 = ET.SubElement(b301, "boolean")
    b302.text = "false"

    #---#

    b75 = ET.SubElement(b41, "option")
    b75.set('name', 'repfirstval')

    b76 = ET.SubElement(b75, "value")

    b77 = ET.SubElement(b76, "boolean")
    b77.text = "false"

    #---#

    b78 = ET.SubElement(b41, "option")
    b78.set('name', 'replastval')

    b79 = ET.SubElement(b78, "value")

    b80 = ET.SubElement(b79, "boolean")
    b80.text = "false"

    #---#

    b81 = ET.SubElement(b41, "option")
    b81.set('name', 'repmax')

    b82 = ET.SubElement(b81, "value")

    b83 = ET.SubElement(b82, "boolean")
    b83.text = "true"

    #---#

    b84 = ET.SubElement(b41, "option")
    b84.set('name', 'repmin')

    b85 = ET.SubElement(b84, "value")

    b86 = ET.SubElement(b85, "boolean")
    b86.text = "true"

    #---#

    b87 = ET.SubElement(b41, "option")
    b87.set('name', 'repssquare')

    b88 = ET.SubElement(b87, "value")

    b89 = ET.SubElement(b88, "boolean")
    b89.text = "false"

    #---#

    b90 = ET.SubElement(b41, "option")
    b90.set('name', 'repsquare')

    b91 = ET.SubElement(b90, "value")

    b92 = ET.SubElement(b91, "boolean")
    b92.text = "false"

    #---#

    b93 = ET.SubElement(b41, "option")
    b93.set('name', 'repssqdev')

    b94 = ET.SubElement(b93, "value")

    b95 = ET.SubElement(b94, "boolean")
    b95.text = "false"

    #---#

    b96 = ET.SubElement(b41, "option")
    b96.set('name', 'repstddev')

    b97 = ET.SubElement(b96, "value")

    b98 = ET.SubElement(b97, "boolean")
    b98.text = "true"

    #---#

    b99 = ET.SubElement(b41, "option")
    b99.set('name', 'repsum')

    b100 = ET.SubElement(b99, "value")

    b101 = ET.SubElement(b100, "boolean")
    b101.text = "false"

    #---#

    b102 = ET.SubElement(b41, "option")
    b102.set('name', 'repvariance')

    b103 = ET.SubElement(b102, "value")

    b104 = ET.SubElement(b103, "boolean")
    b104.text = "false"

    #---#

    b105 = ET.SubElement(b41, "option")
    b105.set('name', 'avg')

    b106 = ET.SubElement(b105, "value")

    b107 = ET.SubElement(b106, "boolean")
    b107.text = "true"

    #---#

    b108 = ET.SubElement(b41, "option")
    b108.set('name', 'ciavg')

    b109 = ET.SubElement(b108, "value")

    b110 = ET.SubElement(b109, "boolean")
    b110.text = "false"

    #---#

    b111 = ET.SubElement(b41, "option")
    b111.set('name', 'count')

    b112 = ET.SubElement(b111, "value")

    b113 = ET.SubElement(b112, "boolean")
    b113.text = "true"

    #---#

    b114 = ET.SubElement(b41, "option")
    b114.set('name', 'firstval')

    b115 = ET.SubElement(b114, "value")

    b116 = ET.SubElement(b115, "boolean")
    b116.text = "false"

    #---#

    b117 = ET.SubElement(b41, "option")
    b117.set('name', 'lastval')

    b118 = ET.SubElement(b117, "value")

    b119 = ET.SubElement(b118, "boolean")
    b119.text = "false"

    #---#

    b120 = ET.SubElement(b41, "option")
    b120.set('name', 'max')

    b121 = ET.SubElement(b120, "value")

    b122 = ET.SubElement(b121, "boolean")
    b122.text = "true"

    #---#

    b123 = ET.SubElement(b41, "option")
    b123.set('name', 'min')

    b124 = ET.SubElement(b123, "value")

    b125 = ET.SubElement(b124, "boolean")
    b125.text = "true"

    #---#

    b126 = ET.SubElement(b41, "option")
    b126.set('name', 'ssquare')

    b127 = ET.SubElement(b126, "value")

    b128 = ET.SubElement(b127, "boolean")
    b128.text = "false"

    #---#

    b129 = ET.SubElement(b41, "option")
    b129.set('name', 'ssqdev')

    b130 = ET.SubElement(b129, "value")

    b131 = ET.SubElement(b130, "boolean")
    b131.text = "false"

    #---#

    b132 = ET.SubElement(b41, "option")
    b132.set('name', 'stddev')

    b133 = ET.SubElement(b132, "value")

    b134 = ET.SubElement(b133, "boolean")
    b134.text = "false"

    #---#

    b135 = ET.SubElement(b41, "option")
    b135.set('name', 'sum')

    b136 = ET.SubElement(b135, "value")

    b137 = ET.SubElement(b136, "boolean")
    b137.text = "false"

    #---#

    b138 = ET.SubElement(b41, "option")
    b138.set('name', 'variance')

    b139 = ET.SubElement(b138, "value")

    b140 = ET.SubElement(b139, "boolean")
    b140.text = "false"

    #---#

    b141 = ET.SubElement(b41, "option")
    b141.set('name', 'firstupdate')

    b142 = ET.SubElement(b141, "value")

    b143 = ET.SubElement(b142, "boolean")
    b143.text = "false"

    #---#

    b144 = ET.SubElement(b41, "option")
    b144.set('name', 'interval')

    b145 = ET.SubElement(b144, "value")

    b146 = ET.SubElement(b145, "boolean")
    b146.text = "false"

    #---#

    b147 = ET.SubElement(b41, "option")
    b147.set('name', 'lastupdate')

    b148 = ET.SubElement(b147, "value")

    b149 = ET.SubElement(b148, "boolean")
    b149.text = "false"

    #---#

    b150 = ET.SubElement(b41, "option")
    b150.set('name', 'untimedavg')

    b151 = ET.SubElement(b150, "value")

    b152 = ET.SubElement(b151, "boolean")
    b152.text = "true"

    #---#

    b153 = ET.SubElement(b41, "option")
    b153.set('name', 'untimedciavg')

    b154 = ET.SubElement(b153, "value")

    b155 = ET.SubElement(b154, "boolean")
    b155.text = "false"

    #---#

    b156 = ET.SubElement(b41, "option")
    b156.set('name', 'untimedcount')

    b157 = ET.SubElement(b156, "value")

    b158 = ET.SubElement(b157, "boolean")
    b158.text = "true"

    #---#

    b159 = ET.SubElement(b41, "option")
    b159.set('name', 'untimedfirstval')

    b160 = ET.SubElement(b159, "value")

    b161 = ET.SubElement(b160, "boolean")
    b161.text = "false"

    #---#

    b162 = ET.SubElement(b41, "option")
    b162.set('name', 'untimedlastval')

    b163 = ET.SubElement(b162, "value")

    b164 = ET.SubElement(b163, "boolean")
    b164.text = "false"

    #---#

    b165 = ET.SubElement(b41, "option")
    b165.set('name', 'untimedmax')

    b166 = ET.SubElement(b165, "value")

    b167 = ET.SubElement(b166, "boolean")
    b167.text = "true"

    #---#

    b168 = ET.SubElement(b41, "option")
    b168.set('name', 'untimedmin')

    b169 = ET.SubElement(b168, "value")

    b170 = ET.SubElement(b169, "boolean")
    b170.text = "true"

    #---#

    b171 = ET.SubElement(b41, "option")
    b171.set('name', 'untimedssquare')

    b172 = ET.SubElement(b171, "value")

    b173 = ET.SubElement(b172, "boolean")
    b173.text = "false"

    #---#

    b174 = ET.SubElement(b41, "option")
    b174.set('name', 'untimedssqdev')

    b175 = ET.SubElement(b174, "value")

    b176 = ET.SubElement(b175, "boolean")
    b176.text = "false"

    #---#

    b177 = ET.SubElement(b41, "option")
    b177.set('name', 'untimedstddev')

    b178 = ET.SubElement(b177, "value")

    b179 = ET.SubElement(b178, "boolean")
    b179.text = "false"

    #---#

    b180 = ET.SubElement(b41, "option")
    b180.set('name', 'untimedsum')

    b181 = ET.SubElement(b180, "value")

    b182 = ET.SubElement(b181, "boolean")
    b182.text = "true"

    #---#

    b183 = ET.SubElement(b41, "option")
    b183.set('name', 'untimedvariance')

    b184 = ET.SubElement(b183, "value")

    b185 = ET.SubElement(b184, "boolean")
    b185.text = "false"

    #---#

    b186 = ET.SubElement(m2, "binders")

    b187 = ET.SubElement(b186, "cpnbinder")
    b187.set('id', 'ID2222')
    b187.set('x', '335')
    b187.set('y', '94')
    b187.set('width', '1353')
    b187.set('height', '738')

    b188 = ET.SubElement(b187, "sheets")

    b189 = ET.SubElement(b188, "cpnsheet")
    b189.set('id', 'ID2215')
    b189.set('panx', '0.000000')
    b189.set('pany', '-63.000000')
    b189.set('zoom', '1.000000')
    b189.set('instance', 'ID2149')

    b190 = ET.SubElement(b189, "zorder")

    b191 = ET.SubElement(b190, "position")
    b191.set('value', '0')

    b192 = ET.SubElement(b187, "zorder")

    b193 = ET.SubElement(b192, "position")
    b193.set('value', '0')

    #---#

    b194 = ET.SubElement(m2, "monitorblock")
    b194.set('name', 'Monitors')

    #---# 3

    b195 = ET.SubElement(m2, "IndexNode")
    b195.set('expanded', 'true')

    b196 = ET.SubElement(b195, "IndexNode")
    b196.set('expanded', 'false')

    b197 = ET.SubElement(b195, "IndexNode")
    b197.set('expanded', 'false')

    b198 = ET.SubElement(b195, "IndexNode")
    b198.set('expanded', 'false')

    #---# 5

    b199 = ET.SubElement(b198, "IndexNode")
    b199.set('expanded', 'false')

    b200 = ET.SubElement(b198, "IndexNode")
    b200.set('expanded', 'false')

    b201 = ET.SubElement(b198, "IndexNode")
    b201.set('expanded', 'false')

    b202 = ET.SubElement(b198, "IndexNode")
    b202.set('expanded', 'false')

    b203 = ET.SubElement(b198, "IndexNode")
    b203.set('expanded', 'false')

    #---#

    b204 = ET.SubElement(b203, "IndexNode")
    b204.set('expanded', 'false')

    #---# 15

    b205 = ET.SubElement(b204, "IndexNode")
    b205.set('expanded', 'false')

    b206 = ET.SubElement(b205, "IndexNode")
    b206.set('expanded', 'false')

    b207 = ET.SubElement(b205, "IndexNode")
    b207.set('expanded', 'false')

    b208 = ET.SubElement(b205, "IndexNode")
    b208.set('expanded', 'false')

    b209 = ET.SubElement(b205, "IndexNode")
    b209.set('expanded', 'false')

    b210 = ET.SubElement(b205, "IndexNode")
    b210.set('expanded', 'false')

    b211 = ET.SubElement(b205, "IndexNode")
    b211.set('expanded', 'false')

    b212 = ET.SubElement(b205, "IndexNode")
    b212.set('expanded', 'false')

    b213 = ET.SubElement(b205, "IndexNode")
    b213.set('expanded', 'false')

    b214 = ET.SubElement(b205, "IndexNode")
    b214.set('expanded', 'false')

    b215 = ET.SubElement(b205, "IndexNode")
    b215.set('expanded', 'false')

    b216 = ET.SubElement(b205, "IndexNode")
    b216.set('expanded', 'false')

    b217 = ET.SubElement(b205, "IndexNode")
    b217.set('expanded', 'false')

    b218 = ET.SubElement(b205, "IndexNode")
    b218.set('expanded', 'false')

    b219 = ET.SubElement(b205, "IndexNode")
    b219.set('expanded', 'false')

    b220 = ET.SubElement(b205, "IndexNode")
    b220.set('expanded', 'false')

    #---# 12 

    b221 = ET.SubElement(b204, "IndexNode")
    b221.set('expanded', 'false')

    b222 = ET.SubElement(b221, "IndexNode")
    b222.set('expanded', 'false')

    b223 = ET.SubElement(b221, "IndexNode")
    b223.set('expanded', 'false')

    b224 = ET.SubElement(b221, "IndexNode")
    b224.set('expanded', 'false')

    b225 = ET.SubElement(b221, "IndexNode")
    b225.set('expanded', 'false')

    b226 = ET.SubElement(b221, "IndexNode")
    b226.set('expanded', 'false')

    b227 = ET.SubElement(b221, "IndexNode")
    b227.set('expanded', 'false')

    b228 = ET.SubElement(b221, "IndexNode")
    b228.set('expanded', 'false')

    b229 = ET.SubElement(b221, "IndexNode")
    b229.set('expanded', 'false')

    b230 = ET.SubElement(b221, "IndexNode")
    b230.set('expanded', 'false')

    b231 = ET.SubElement(b221, "IndexNode")
    b231.set('expanded', 'false')

    b232 = ET.SubElement(b221, "IndexNode")
    b232.set('expanded', 'false')

    b233 = ET.SubElement(b221, "IndexNode")
    b233.set('expanded', 'false')

    #---# 12

    b234 = ET.SubElement(b203, "IndexNode")
    b234.set('expanded', 'false')

    b235 = ET.SubElement(b234, "IndexNode")
    b235.set('expanded', 'false')

    b236 = ET.SubElement(b234, "IndexNode")
    b236.set('expanded', 'false')

    b237 = ET.SubElement(b234, "IndexNode")
    b237.set('expanded', 'false')

    b238 = ET.SubElement(b234, "IndexNode")
    b238.set('expanded', 'false')

    b239 = ET.SubElement(b234, "IndexNode")
    b239.set('expanded', 'false')

    b240 = ET.SubElement(b234, "IndexNode")
    b240.set('expanded', 'false')

    b241 = ET.SubElement(b234, "IndexNode")
    b241.set('expanded', 'false')

    b242 = ET.SubElement(b234, "IndexNode")
    b242.set('expanded', 'false')

    b243 = ET.SubElement(b234, "IndexNode")
    b243.set('expanded', 'false')

    b244 = ET.SubElement(b234, "IndexNode")
    b244.set('expanded', 'false')

    b245 = ET.SubElement(b234, "IndexNode")
    b245.set('expanded', 'false')

    b246 = ET.SubElement(b234, "IndexNode")
    b246.set('expanded', 'false')

    #---# 5

    b247 = ET.SubElement(b198, "IndexNode")
    b247.set('expanded', 'false')

    b248 = ET.SubElement(b247, "IndexNode")
    b248.set('expanded', 'false')

    b249 = ET.SubElement(b247, "IndexNode")
    b249.set('expanded', 'false')

    b250 = ET.SubElement(b247, "IndexNode")
    b250.set('expanded', 'false')

    b251 = ET.SubElement(b247, "IndexNode")
    b251.set('expanded', 'false')

    b252 = ET.SubElement(b247, "IndexNode")
    b252.set('expanded', 'false')

    #---# 2

    b253 = ET.SubElement(b195, "IndexNode")
    b253.set('expanded', 'false')

    b254 = ET.SubElement(b195, "IndexNode")
    b254.set('expanded', 'true')

    #---# 3

    b255 = ET.SubElement(b254, "IndexNode")
    b255.set('expanded', 'false')

    b256 = ET.SubElement(b255, "IndexNode")
    b256.set('expanded', 'true')

    b257 = ET.SubElement(b255, "IndexNode")
    b257.set('expanded', 'true')

    b258 = ET.SubElement(b255, "IndexNode")
    b258.set('expanded', 'true')

    #---# 8

    b259 = ET.SubElement(b254, "IndexNode")
    b259.set('expanded', 'true')

    b260 = ET.SubElement(b259, "IndexNode")
    b260.set('expanded', 'false')

    b261 = ET.SubElement(b259, "IndexNode")
    b261.set('expanded', 'false')

    b262 = ET.SubElement(b259, "IndexNode")
    b262.set('expanded', 'false')

    b263 = ET.SubElement(b259, "IndexNode")
    b263.set('expanded', 'false')

    b264 = ET.SubElement(b259, "IndexNode")
    b264.set('expanded', 'false')

    b265 = ET.SubElement(b259, "IndexNode")
    b265.set('expanded', 'false')

    b266 = ET.SubElement(b259, "IndexNode")
    b266.set('expanded', 'true')

    b267 = ET.SubElement(b259, "IndexNode")
    b267.set('expanded', 'true')

    #---# 2

    b268 = ET.SubElement(b195, "IndexNode")
    b268.set('expanded', 'false')

    b269 = ET.SubElement(b195, "IndexNode")
    b269.set('expanded', 'true')

# # Execução das funções
# file = open("structures.xml", "w")
# goals = ['start']
# document = read_xml("wp.xml")
# file = get_groups(document, file)
# file, goals = get_plans(document, file, goals)
# print(goals)
# size = len(goals)
# file.close()
    
#-----------------------------------------------------------------------------------------------#

m1 = ET.Element("generator")
root.append(m1)
m1.set('tool', 'CPN Tools')
m1.set('version', '4.0.1')
m1.set('format', '6')

m2 = ET.Element("cpnet")
root.append(m2)
b1 = ET.SubElement(m2, "globbox")
b2 = ET.SubElement(b1, "block")
b2.set('id', 'ID1412310166')

b3 = ET.SubElement(b2, "id")
b3.text = "Standard priorities"

b4 = ET.SubElement(b2, "ml")
b4.set('id', 'ID1412310255')
b4.text = "val P_HIGH = 100;"
b5 = ET.SubElement(b4, "layout")
b5.text = "val P_HIGH = 100;"

b6 = ET.SubElement(b2, "ml")
b6.set('id', 'ID1412310292')
b6.text = "val P_NORMAL = 1000;"
b7 = ET.SubElement(b6, "layout")
b7.text = "val P_NORMAL = 1000;"

b8 = ET.SubElement(b2, "ml")
b8.set('id', 'ID1412310322')
b8.text = "val P_LOW = 10000;"
b9 = ET.SubElement(b8, "layout")
b9.text = "val P_LOW = 10000;"

b10 = ET.SubElement(b1, "block")
b10.set('id', 'ID1')

b11 = ET.SubElement(b10, "id")
b11.text = "Standard declarations"

b12 = ET.SubElement(b10, "color")
b12.set('id', 'ID85042')
b13 = ET.SubElement(b12, "id")
b13.text = "UNIT"
b14 = ET.SubElement(b12, "unit")
b15 = ET.SubElement(b12, "layout")
b15.text = "colset UNIT = unit;"

b16 = ET.SubElement(b10, "color")
b16.set('id', 'ID4')
b17 = ET.SubElement(b16, "id")
b17.text = "BOOL"
b18 = ET.SubElement(b16, "bool")

b19 = ET.SubElement(b10, "color")
b19.set('id', 'ID3')
b20 = ET.SubElement(b19, "id")
b20.text = "INT"
b21 = ET.SubElement(b19, "int")

b22 = ET.SubElement(b10, "color")
b22.set('id', 'ID1412312409')
b23 = ET.SubElement(b22, "id")
b23.text = "INTINF"
b24 = ET.SubElement(b22, "intinf")
b25 = ET.SubElement(b22, "layout")
b25.text = "colset INTINF = intinf;"

b26 = ET.SubElement(b10, "color")
b26.set('id', 'ID1412312425')
b27 = ET.SubElement(b26, "id")
b27.text = "TIME"
b28 = ET.SubElement(b26, "time")
b29 = ET.SubElement(b26, "layout")
b29.text = "colset TIME = time;"

b30 = ET.SubElement(b10, "color")
b30.set('id', 'ID1412322990')
b31 = ET.SubElement(b30, "id")
b31.text = "REAL"
b32 = ET.SubElement(b30, "real")
b33 = ET.SubElement(b30, "layout")
b33.text = "colset REAL = real;"

b34 = ET.SubElement(b10, "color")
b34.set('id', 'ID5')
b35 = ET.SubElement(b34, "id")
b35.text = "STRING"
b36 = ET.SubElement(b34, "string")

create_variables()

create_functions()

b37 = ET.SubElement(m2, "page") 
b37.set('id', 'ID6')
b38 = ET.SubElement(b37, "pageattr")
b38.set('name', doc_name)

#-----------------------------------------------------------------------------------------------#

node = document.getElementsByTagName("goal")

visited = []

goal = document.getElementsByTagName("goal")[0] # Pega o primeiro nodo goal
root_tree = goal # Armazena o primeiro goal que será o nodo raiz da árvore

goals_missions = []

for i in range(0, len(missions)):
    browser = []
    clear_node(missions[i].childNodes)
    for j in range(0, len(missions[i].childNodes)):
        current = Missions(missions[i].childNodes[j])
        current.mission = missions[i].getAttribute("id")
        browser.append(current)
    goals_missions.append(browser)

i = 0

for i in range(0, len(node)):
    if (node[i].parentNode.nodeName != "plan" and node[i].parentNode.nodeName != "scheme"):
        node[i].parentNode.removeChild(node[i])

node = root_tree

# Leitura da Árvora Funcionando

def elipse_print(node):
    global transitions
    if transitions == 1:
        print(f"\nNodo : start")
    else:
        print(f"\nNodo {node.parentNode.getAttribute("operator")} : {node.getAttribute("id")}")

def trans_print():
    global transitions
    print("* Transição: t{}".format(transitions-1))

def calculate_parallel_positions(node):
    global x
    global parallel_x
    global parallel_y
    global elipse_y
    global has_operator
    
    if has_operator == False:
        parallel_y = elipse_y
    else:
        parallel_y = float(trans_1_y) - 100
        parallel_y = str(parallel_y)
    
    n_childs = len(node.parentNode.childNodes)
    x = -1*((n_childs/2)*80)
    parallel_x = int(float(x))
    parallel_x = str(parallel_x)
    if (n_childs>1):
        x = (abs(float(parallel_x))*2)/(n_childs-1)
    else:
        x = (abs(float(parallel_x))*2)
    if horizontal_x != '0':
        parallel_x = float(parallel_x) + float(horizontal_x) - 150
        parallel_x = str(parallel_x)
    main_operator[op][6] = str(float(parallel_x) + float(x))
    main_operator[op][7] = x
        
def calculate_choice_positions(node):
    global x
    global choice_x
    global choice_y
    global elipse_y
    
    n_childs = len(node.parentNode.childNodes)
    x = -1*((n_childs/2)*80)
    start_choice_x = int(float(x))
    choice_x = int(float(x))
    choice_x = str(choice_x)
    if (n_childs>1):
        x = (abs(float(choice_x))*2)/(n_childs-1)
    else:
        x = (abs(float(choice_x))*2)
    main_operator[op][6] = x
    return start_choice_x

def check_for_operator():
    global main_operator
    global op
    global has_operator
    has_operator = False
    if main_operator[op-1][1] == True:
        has_operator = True
    # print(f"\nHas_operator = {has_operator}")

def create_trans_guard(parent):
    global transitions
    global curr_mission
    global curr_type
    global t14
    
    print(f"transitions = {transitions}")
    
    parent = parent.parentNode
    
    clear_node(parent.childNodes)
    
    stored_mission = curr_mission
    stored_type = curr_type
    
    clear_node(parent.childNodes)
    
    string = ''
    for i in range(0,len(parent.childNodes)):
        find_mission(parent.childNodes[i])
        if curr_mission != 'BOOL':
            # print(f'child[{i}] = {parent.childNodes[i].getAttribute("id")}')
            index = n_missions.index(curr_mission)
            index_role = norm.childNodes[index].getAttribute("role")
            # print(f'normative = {n}')
            for j in range(0, len(struct_spec)):
                if index_role in struct_spec[j]:
                    group = str(struct_spec[j][0])
            #get last 3 digits of funtions
            aux = str(functions[index])[-3:]
            aux = aux.replace(')', '')
            if transitions == 2:
                string = functions[-1]
                string += '\n' + aux + ' = (' + index_role + ',' + group + ')'
                break
            elif parent.getAttribute("operator") == 'sequence' or parent.getAttribute("operator") == 'choice':
                # print(f'operator = {parent.getAttribute("operator")}\n')
                string = aux + ' = (' + index_role + ',' + group + ')'
                break
            elif parent.getAttribute("operator") == 'parallel':
                # print(f'operator = {parent.getAttribute("operator")}\n')
                if i == len(parent.childNodes)-1:
                    string += aux + ' = (' + index_role + ',' + group + ')\n'
                else:
                    string += aux + ' = (' + index_role + ',' + group + ') andalso\n' 
            elif parent.nodeName == 'scheme':
                string = aux + ' = (' + index_role + ',' + group + ')'
                break
    if string != '':
        print(f'{string}')
            
    curr_mission = stored_mission
    curr_type = stored_type
    return string
        
guard = ''
curr_mission = "BOOL"
create_elipse("start", curr_mission, False)
elipse_print(node)

create_trans("t" + str(transitions), False, guard)
trans_print()

create_arc(True, "sequence")

while True:
    
    if (node.nodeName == "plan"):
        if op == -1:
            main_operator[0] = [node, False, 'trans_1_id', 'trans_2_id', 'x', 'y', '', '',[]]
            op += 1
            print (f"\nNew operator added = {node.getAttribute('operator')} - {main_operator[op]}")
        elif main_operator[op][0] != node:
            main_operator.append([node, False, 'trans_1_id', 'trans_2_id', 'x', 'y', '', '',[]])
            op += 1
            print (f"\nNew operator added = {node.getAttribute('operator')} - {main_operator[op]}")
    
    if root_tree.hasChildNodes() == False:
        
        string = find_mission(node)
        
        create_elipse(string, curr_type, False)
        
        print(f"\nCurr_mission = {curr_mission}")
        
        guard = create_trans_guard(node)
        if guard != '':
            if curr_mission != 'BOOL':
                t14.text = guard
                
        print(f"\nGuard: {guard}")
        
        create_arc(False, "sequence")
        create_trans("t" + str(transitions), False, guard)
        create_arc(True, "sequence")
        
        elipse_print(node)
        trans_print()

        curr_mission = "BOOL"
        create_elipse("end", curr_mission, False)
        create_arc(False, "sequence")
        break
    
    if node.hasChildNodes() == True: 
        clear_node(node.childNodes)
        node = node.childNodes[0]
    elif node.hasChildNodes() == False:
        for i in range(0, len(main_operator)):
            if i == 0:
                print(f"\n*\n{main_operator[i][0].getAttribute('operator')}:{main_operator[i]}")
            else:
                print(f"{main_operator[i][0].getAttribute('operator')}:{main_operator[i]}")
        print("*")
            
        if (node.nodeName == "goal"):
            
            plan = node.parentNode
            string = find_mission(node)
            check_for_operator()
            
            # print(f'\n{main_operator[op][0].getAttribute("operator")}: {main_operator[op]}')
            # print(f'\nCreated = {main_operator[op][1]}')
            # print(f"\nCurr_mission = {curr_mission}")
            # print(f"n = {op}")
            # print(f'\nMain_operator[{op}] = {main_operator[op]}\n')
            if (plan.getAttribute("operator") == "sequence"):
                
                print(f"\nCurr_mission = {curr_mission}")
                
                guard = create_trans_guard(node)
                if guard != '':
                    if curr_mission != 'BOOL':
                        print(f"\nt14 sequence = {guard}")
                        t14.text = guard
                        
                if has_operator == True:
                    main_operator[op][1] = True
                    main_operator[op][4] = str(elipse_x)
                    main_operator[op][5] = str(elipse_y)
                    create_elipse(string, curr_type, True)
                    elipse_print(node)
                    # print(f"\nIS FIRST = {is_first_child}")
                    if is_first_child == True and main_operator[op-1][0].getAttribute("operator") == "parallel":
                        create_first_arc('sequence')
                        is_first_child = False
                    elif choice_trans_arc == True:
                        for f in range(0, len(trans_choice)):
                            create_choice_arc()
                            update_start_choice_x()
                        choice_trans_arc = False
                        arc_y = str(int(float(elipse_y)) - 50)   
                    else:
                        create_arc(False, "sequence")      
                elif (main_operator[op][1] == False):
                    main_operator[op][4] = str(elipse_x)
                    main_operator[op][5] = str(elipse_y)
                    create_elipse(string, curr_type, False)
                    elipse_print(node)
                    if choice_trans_arc == False:
                        create_arc(False, "sequence")
                    else:
                        for f in range(0, len(trans_choice)):
                            create_choice_arc()
                            update_start_choice_x()
                        choice_trans_arc = False
                        arc_y = str(int(float(elipse_y)) - 50)                  
                        
            elif (plan.getAttribute("operator") == "parallel"):
                
                if main_operator[op][1] == False:
                    
                    print(f"\nCurr_mission = {curr_mission}")
                    
                    guard = create_trans_guard(node)
                    if guard != '':
                        if curr_mission != 'BOOL':
                            print(f"\nt14 parallel = {guard}")
                            t14.text = guard
                            
                    calculate_parallel_positions(node)
                    main_operator[op][2] = trans_id
                    # print(f"TRANS 1 = {main_operator[op][2]}")
                    main_operator[op][4] = str(parallel_x)
                    main_operator[op][5] = str(parallel_y)
                    trans_1_x = parallel_x
                    create_parallel_elipse(string, curr_type, True)
                    main_operator[op][4] = str(parallel_x)
                    elipse_print(node)
                    create_first_arc('parallel')
                    create_trans("t" + str(transitions), False, guard)
                    trans_print()
                    main_operator[op][3] = trans_id
                    # print(f"TRANS 2 = {main_operator[op][3]}")
                    create_second_arc()
                    main_operator[op][1] = True
                else:
                    create_parallel_elipse(string, curr_type, False)
                    main_operator[op][4] = str(parallel_x)
                    main_operator[op][5] = str(parallel_y)
                    elipse_print(node)
                    if had_operator == False:
                        trans_1_x = str(float(main_operator[op][4]) - float(x))
                    else:
                        trans_1_x = str((float(main_operator[op][4]) + float(horizontal_x))/3)
                    create_first_arc('parallel')
                    main_operator[op][6] = float(main_operator[op][6]) + float(main_operator[op][7])
                    main_operator[op][6] = str(main_operator[op][6])
                    trans_1_x = str(float(main_operator[op][4]) - float(x))
                    create_second_arc()
                    
            elif (plan.getAttribute("operator") == "choice"):
                if main_operator[op][1] == False:
                    start_choice_x = calculate_choice_positions(node)
                    stored_elipse = elipse_id
                    main_operator[op][1] = True
                else:
                    if (op == 0) or (op > 0 and main_operator[op-1][1] == False):
                        elipse_id = stored_elipse
                choice_y = elipse_y
                
                if (op == 0) or (op > 0 and main_operator[op-1][1] == False):
                    create_choice_trans("t"+str(transitions), False)
                    print(f'stored_node = {stored_node.getAttribute("id")}')
                    create_first_choice_arc()
                    trans_print()
                    update_choice_y()
                
                print(f"\nCurr_mission = {curr_mission}")
                    
                guard = create_trans_guard(node)
                if guard != '':
                    if curr_mission != 'BOOL':
                        print(f"\nt14 choice = {guard}")
                        t14.text = guard
                
                create_choice_elipse(string, curr_type, False)
                elipse_print(node)
                # print(f'curr_mission = {curr_mission}')
                create_arc(False, "choice")
                update_choice_y()
                create_choice_trans("t" + str(transitions), True)
                trans_print()
                choice_trans_arc = True
                create_arc(True, "choice")
                last_choice_y = choice_y
                update_choice_x()
                update_choice_y()
                
                if len(node.parentNode.childNodes) == 1:
                    elipse_y = choice_y
        
        if plan.getAttribute('operator') != 'choice':
            stored_node = node
        sibling = node
        
        while True:
            clear_node(sibling.childNodes)
            #Checa se o nodo atual tem um irmão e não tem filhos
            if sibling.nextSibling != None and sibling.hasChildNodes() == False:
                if sibling != node:
                    break
                else:
                    sibling = sibling.nextSibling
            #Checa se o nodo atual tem um irmão e tem filhos
            elif sibling.nextSibling != None and sibling.hasChildNodes() == True:
                sibling = sibling.childNodes[0]
            #Checa se o nodo atual não tem um irmão e tem filhos
            elif sibling.nextSibling == None and sibling.hasChildNodes() == True:
                while sibling.hasChildNodes() == True:
                    clear_node(sibling.childNodes)
                    sibling = sibling.childNodes[0]
            #Checa se o nodo atual não tem um irmão e não tem filhos
            elif sibling.nextSibling == None and sibling.hasChildNodes() == False:
                break
            
        parent = node.parentNode
        
        if node.nodeName == "plan":
            is_first_child = True
            for j in range(0, len(main_operator)):
                if main_operator[j][0] == node:
                    if main_operator[j][0].getAttribute("operator") == "choice":
                        trans_choice = main_operator[j][8]
                    elif (main_operator[j][0].getAttribute("operator") == "parallel" and main_operator[j][1] == True):
                        print(f"\n - Trocou o main_operator[{op-1}][2]:{main_operator[op-1][0].getAttribute("operator")} = {main_operator[op-1][2]} por main_operator[{op}][3]:{main_operator[op][0].getAttribute("operator")} = {main_operator[op][3]}")
                        main_operator[op-1][2] = main_operator[op][3]
                        trans_id = main_operator[op-1][2]
                        # print(f"NEW OPERATOR = {main_operator[op-1][2]}")
                    main_operator.pop()
                    op -= 1
                    had_operator = True
                    if has_operator == False:
                        trans_1_y = '0'
                        horizontal_x = '0'
        
        parent.removeChild(node)
        node = parent
        
        if (node.nodeName == "plan" and node.getAttribute("operator") == "sequence"):
            if sibling != None and sibling.parentNode != None:
                # print(sibling.getAttribute("id"))
                # print(sibling.parentNode)
                if sibling.parentNode.getAttribute("operator") == "choice" and has_operator == False:
                    permit_trans = False
                    print(f'negou a permissão com o sibling = {sibling.getAttribute("id")}')
            if permit_trans == True:
                if has_operator == True:
                    create_trans("t" + str(transitions), True, guard)
                else:
                    trans_1_y = elipse_y
                    create_trans("t" + str(transitions), False, guard)
                trans_print()
                create_arc(True, "sequence")
                main_operator[op][2] = trans_id
            else:
                permit_trans = True
            
            
#-----------------------------------------------------------------------------------------#

# while True:
    
#     if (node.nodeName == "plan"):
#         # print(f"\nPLANO = {node.getAttribute('operator')}\n")
#         if node.getAttribute("operator") != "sequence":
#             op = [node, False, '', '']
#             if op == -1:
#                 main_operator[0] = op
#                 op += 1
#                 print (f"\nADICIONOU UM NOVO MAIN OPERATOR1 {node.getAttribute('operator')} = {main_operator[op]}")
#             elif (main_operator[op-1][0] != node and main_operator[op][0] != node):
#                 print(main_operator[op-1][0])
#                 print(node)
#                 main_operator.append(op)
#                 op += 1
#                 print (f"\nADICIONOU UM NOVO MAIN OPERATOR2 {node.getAttribute('operator')} = {main_operator[op]}")
            
    
#     #Creca se chegou no fim da árvore por meio da checarem de filhos
#     if root_tree.hasChildNodes() == False:
#         string = find_mission(node)
#         print("\n* Leu o Nó: {}".format(node.getAttribute("id")))
#         id = create_id()
#         if find_mission(node) == node.getAttribute("id"):
#             curr_type = "BOOL"
#         else:
#             curr_type = "RG"
#         create_elipse(string, curr_type, id, False)

#         id = create_id()
#         create_arc(id, False, "sequence")

#         id = create_id()
#         print(" * Criou a transição: t{}".format(transitions))
#         create_trans("t" + str(transitions), id, False)
#         transitions += 1

#         id = create_id()
#         create_arc(id, True, "sequence")

#         id = create_id()
#         curr_mission = "BOOL"
#         create_elipse("end", curr_mission, id, False)
#         print("\n* Leu o Nó: end")

#         id = create_id()
#         create_arc(id, False, "sequence")

#         print ("\n* Fim da árvore")
#         break   
#     #Creca se o nodo atual possui filhos

#     if node.hasChildNodes() == True:
#         clear_node(node.childNodes) #Limpa os nodos de texto e novas linhas deixando só os nodos de interesse [goals e plans]
#         node = node.childNodes[0] #Pega o primeiro nodo filho que não possui filhos
#     #Se o nodo atual não possui filhos ele faz a leitura dele
#     elif node.hasChildNodes() == False:

#         if (node.nodeName == "goal"):
#             print(f"n = {op}")
#             print(f'\nMain_operator[{op}] = {main_operator[op]}\n')

#             plan = node.parentNode

#             if (plan.getAttribute("operator") == "sequence"):

#                 print("\n* Leu o Nó em 'sequence': {}".format(node.getAttribute("id")))
#                 string = find_mission(node)

#                 # if created == False:
#                 if (main_operator[op][1] == False or len(main_operator) <= 0):
#                     #Cria a elipse do nodo atual
#                     id = create_id()
#                     if find_mission(node) == node.getAttribute("id"):
#                         curr_type = "BOOL"
#                     else:
#                         curr_type = "RG"
#                     create_elipse(string, curr_type, id, False)

#                     #Cria o arco entre o nodo atual e a transição anterior
#                     if choice_trans_arc == True:
#                         end_choice_x = start_choice_x
#                         for i in range(0, len(trans_choice)):
#                             id = create_id()
#                             create_choice_arc(id)
#                         choice_trans_arc = False
#                         arc_y = int(float(elipse_y)) - 50
#                         arc_y = str(arc_y)
#                     else:
#                         # arc_y = elipse_y
#                         id = create_id()
#                         create_arc(id, False, "sequence")

#                 # if created == True:
#                 if main_operator[op][1] == True:
#                     is_decendant = True
#                     #Cria a elipse do nodo atual
#                     id = create_id()
#                     if find_mission(node) == node.getAttribute("id"):
#                         curr_type = "BOOL"
#                     else:
#                         curr_type = "RG"
#                     create_elipse(string, curr_type, id, True)
                    
#                     # Checa para o caso de não ter um operador principal e esse ser o primeiro filho
#                     if curr_operator != False and is_first_child == True:
#                         id = create_id()
#                         create_first_arc(id)
#                         is_first_child = False
#                     else:
#                         # arc_y = elipse_y
#                         id = create_id()
#                         create_arc(id, False, "sequence")

#             elif (plan.getAttribute("operator") == "parallel"):

#                 print("\n* Leu o Nó em 'parallel': {}".format(node.getAttribute("id")))
#                 string = find_mission(node)

#                 if curr_operator == False:
#                     curr_operator = node.parentNode
#                     print(f'\nCurr_operator: {curr_operator}')

#                 # if created == False:
#                 if main_operator[op][1] == False:
#                     n_childs = len(node.parentNode.childNodes)
#                     x = -1*((n_childs/2)*80)
#                     parallel_x = int(float(x))
#                     parallel_x = str(parallel_x)
#                     if (n_childs>1):
#                         x = (abs(float(parallel_x))*2)/(n_childs-1)
#                     else:
#                         x = (abs(float(parallel_x))*2)
#                 # if created == False:
#                 if main_operator[op][1] == False:
#                     print(f'\nENTROU EM CREATED == FALSE\n')
#                     trans_1 = trans_id
#                     print(f'- Trans_1 = t{transitions-1}\n')
                    
#                     main_operator[op][2] = trans_1

#                     parallel_y = elipse_y

#                     id = create_id()
#                     if find_mission(node) == node.getAttribute("id"):
#                         curr_type = "BOOL"
#                     else:
#                         curr_type = "RG"
#                     create_parallel_elipse(string, curr_type, id, True)

#                     id = create_id()
#                     create_first_arc(id)

#                     id = create_id()
#                     print(" * Criou a transição: t{}".format(transitions))
#                     create_trans("t" + str(transitions), id, False)
#                     transitions += 1
#                     trans_id = trans_2 = id
                
                    
#                     main_operator[op][3] = trans_2

#                     print(f'\n- Trans_2 = t{transitions-1}')
                    
#                     id = create_id()
#                     create_second_arc(id)

#                     main_operator[op][1] = True
#                 else:
#                     print(f'\nENTROU EM CREATED == TRUE\n')
#                     id = create_id()
#                     if find_mission(node) == node.getAttribute("id"):
#                         curr_type = "BOOL"
#                     else:
#                         curr_type = "RG"
#                     create_parallel_elipse(string, curr_type, id, False)
                    
#                     id = create_id()
#                     create_first_arc(id)

#                     id = create_id()
#                     create_second_arc(id)

#             elif (plan.getAttribute("operator") == "choice"):

#                 print("\n* Leu o Nó em 'choice': {}".format(node.getAttribute("id")))
#                 string = find_mission(node)

#                 if curr_operator == False:
#                     curr_operator = node.parentNode
#                     print(f'\nCurr_operator: {curr_operator}')

#                 # if created == False:
#                 if main_operator[op][1] == False:
#                     n_childs = len(node.parentNode.childNodes)
#                     x = -1*((n_childs/2)*80)
#                     choice_x = int(float(x))
#                     choice_x = str(choice_x)
#                     start_choice_x = choice_x
#                     if (n_childs>1):
#                         x = (abs(float(choice_x))*2)/(n_childs-1)
#                     else:
#                         x = (abs(float(choice_x))*2)

#                 # if created == False:
#                 if main_operator[op][1] == False:
#                     stored_elipse = elipse_id
#                     main_operator[op][1] = True
#                 # elif created == True:
#                 elif main_operator[op][1] == True:
#                     if is_decendant == False:
#                         elipse_id = stored_elipse
#                 choice_y = elipse_y
                
#                 if is_decendant == False:
#                     id = create_id()
#                     create_choice_trans("t"+str(transitions), id, False)
#                     transitions += 1

#                     id = create_id()
#                     create_arc(id, True, "choice")
#                     update_choice_y()
                    
#                 id = create_id()
#                 if find_mission(node) == node.getAttribute("id"):
#                     curr_type = "BOOL"
#                 else:
#                     curr_type = "RG"
#                 create_choice_elipse(string, curr_type, id, False)

#                 id = create_id()
#                 create_arc(id, False, "coice")
#                 update_choice_y()

#                 id = create_id()
#                 print(" * Criou a transição: t{}".format(transitions))
#                 create_choice_trans("t" + str(transitions), id, False)
#                 transitions += 1

#                 trans_choice.append(id)
#                 choice_trans_arc = True

#                 id = create_id()
#                 create_arc(id, True, "choice")
                
#                 last_choice_y = choice_y
                
#                 update_choice_y()
#                 update_choice_x()

#                 if len(node.parentNode.childNodes) == 1:
#                     elipse_y = choice_y

#         if (node == curr_operator):
#             curr_operator = False
#             created = False
#             trans_1_y = '0'
#             trans_1_x = '100'
#             is_decendant = False

#         stored_node = node # Armazena o nodo atual

#         # sibling = node.nextSibling # Armazena o nodo irmão
#         sibling = node # Armazena o nodo irmão
#         # print(f'sibling: {sibling}')

#         #find next node with no child that gonna be read
#         while True:
#             clear_node(sibling.childNodes)
#             #Checa se o nodo atual tem um irmão e não tem filhos
#             if sibling.nextSibling != None and sibling.hasChildNodes() == False:
#                 if sibling != node:
#                     break
#                 else:
#                     sibling = sibling.nextSibling
#             #Checa se o nodo atual tem um irmão e tem filhos
#             elif sibling.nextSibling != None and sibling.hasChildNodes() == True:
#                 sibling = sibling.childNodes[0]
#             #Checa se o nodo atual não tem um irmão e tem filhos
#             elif sibling.nextSibling == None and sibling.hasChildNodes() == True:
#                 while sibling.hasChildNodes() == True:
#                     clear_node(sibling.childNodes)
#                     sibling = sibling.childNodes[0]
#             #Checa se o nodo atual não tem um irmão e não tem filhos
#             elif sibling.nextSibling == None and sibling.hasChildNodes() == False:
#                 break

#         parent = node.parentNode # Armazena o nodo pai
#         if (parent.getAttribute("operator") == "sequence"):
#             trans_1 = trans_id
#         if node.nodeName == "plan":
#             is_first_child = True
#         if node.nodeName == "plan":
#             if node.getAttribute("operator") == "choice" or node.getAttribute("operator") == "parallel":
#                 if main_operator[op][1] == node:
#                     main_operator.pop()
#                     op -= 1
#         parent.removeChild(node) # Remove o nodo atual
#         node = parent

#         if (node.nodeName == "plan" and node.getAttribute("operator") == "sequence"):
#             if sibling != None and sibling.parentNode != None:
#                 # print(sibling.getAttribute("id"))
#                 # print(sibling.parentNode)
#                 if sibling.parentNode.getAttribute("operator") == "choice":
#                     permit_trans = False
#                     print(f'negou a permissão com o sibling = {sibling.getAttribute("id")}')
#             if permit_trans == True:
#                 id = create_id()
#                 print(" * Criou a transição: t{}".format(transitions))
#                 if curr_operator != False:
#                     create_trans("t" + str(transitions), id, True)
#                 else:
#                     trans_1_y = elipse_y
#                     create_trans("t" + str(transitions), id, False)
#                 transitions += 1
#                 if curr_operator != False:
#                     trans_1 = trans_id
#                 id = create_id()
#                 create_arc(id, True, "sequence")
#             else:
#                 permit_trans = True

tree = ET.ElementTree(root)
create_body()
doc_name = doc_name.replace('.xml', '.cpn')
ET.indent(tree, space="\t", level=0)
with open(doc_name, "wb") as files:
    tree.write(files, encoding="utf-8")