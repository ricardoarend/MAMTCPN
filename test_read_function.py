import xml.dom.minidom

# Função que limpa os nós de texto e novas linhas deixando só os nodos de interesse [goals e plans]
def clear_node(branch):
    n = 0
    while n < len(branch):
        if branch[n].nodeName == "#text":
            branch[n].parentNode.removeChild(branch[n])
        n+=1
    return branch

class Missions():
    def __init__(self, data):
        self.data = data
        self.mission = None


document = xml.dom.minidom.parse("wp.xml") # Faz a leitura do arquivo XML

node = document.getElementsByTagName("goal")

visited = []

goal = document.getElementsByTagName("goal")[0] # Pega o primeiro nodo goal
root = goal # Armazena o primeiro goal que será o nodo raiz da árvore

missions = document.getElementsByTagName("mission") # Pega todos os nodos mission
goals_missions = []

for i in range(0, len(missions)):
    browser = []
    clear_node(missions[i].childNodes)
    for j in range(0, len(missions[i].childNodes)):
        current = Missions(missions[i].childNodes[j])
        current.mission = missions[i].getAttribute("id")
        browser.append(current)
    goals_missions.append(browser)

# Print all the goals and mission atached to them
# for i in range(0, len(goals_missions)):
#     print("Mission: " + goals_missions[i][0].mission)
#     for j in range(0, len(goals_missions[i])):
#         print(" ", goals_missions[i][j].data.getAttribute("id"))
            
#Check which mission the current node has
# for i in range(0, len(goals_missions)):
#     for j in range(0, len(goals_missions[i])):
#         if goals_missions[i][j].data.getAttribute("id") == goal.getAttribute("id"):
#             print("Mission: ", goals_missions[i][j].mission)

n = 0

while n < len(node):
    if (node[n].parentNode.nodeName != "plan" and node[n].parentNode.nodeName != "scheme"):
        node[n].parentNode.removeChild(node[n])
    n+=1

node = root

# Leitura da Árvora Funcionando

while True:
    # if (node.nodeName == "goal"):
    #     print("Node: {}, Id: {}, hasChild: {}".format(node.nodeName, node.getAttribute("id"), node.hasChildNodes()))
    if node.hasChildNodes() == True:
        clear_node(node.childNodes)
        node = node.childNodes[0]
    elif node.hasChildNodes() == False:
        if (node.nodeName == "goal"):
            print("* Leu o Nó: {}".format(node.getAttribute("id")))
        elif (node.nodeName == "plan"):
            print("* Leu o Plano: {}".format(node.getAttribute("operator")))
        parent = node.parentNode # Armazena o nodo pai
        node.parentNode.removeChild(node) # Remove o nodo atual
        node = parent
    if root.hasChildNodes() == False:
        print ("* Fim da árvore")
        break