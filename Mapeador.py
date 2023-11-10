#Código principal do projeto Mapeamento de Esquemas Moise para Redes de Petri

# Importação de bibliotecas
import xml.dom.minidom

# Função que faz a leitura do arquivo XML
def read_xml(archive):
    document = xml.dom.minidom.parse(archive)
    return document

# Função que faz a separação dos grupos contidos no documento XML
def get_groups(document, file):
    groups = document.getElementsByTagName("group-specification")
    
    for element in groups:
        gp = element.getAttribute("id")
        # print("\nGroup: %s" % (gp))
        file.write("\n{\n")
        file.write("Group: %s" % (gp))
    
        roles = element.getElementsByTagName("role")
        for role in roles:
            role_id = role.getAttribute("id")
            role_min = role.getAttribute("min")
            role_max = role.getAttribute("max")
            # print("role: %s " % (role_id))
            # print("min: %s " % (role_min))
            # print("max: %s " % (role_max))
            file.write("\n role: %s, " % (role_id))
            file.write("min: %s, " % (role_min))
            file.write("max: %s" % (role_max))
        file.write("\n}\n")

    return file
# Função que faz a separação dos planos contidos no documento XML
def get_plans(document, file, list):
    plans = document.getElementsByTagName("plan")
    plans.reverse()

    cont = 0
    
    for element in plans:

        print(cont)
        cont = cont + 1

        op = element.getAttribute("operator")
        # print("\nOperator: %s" % (op))
        file.write("\n{\n")
        file.write("Operator: %s" % (op))
    
        goals = element.getElementsByTagName("goal")
        for goal in goals:
            goal_id = goal.getAttribute("id")
            file.write("\n goal: %s" % (goal_id))
            list.append(goal_id)
            element.removeChild(goal)
        file.write("\n}\n")    
    
    goals = document.getElementsByTagName("goal")[0]
    first = goals.getAttribute("id")
    # print("\nInitial goal: %s" % (first))
    file.write("\nBegin from: %s" % (first))

    return file, list

# Execução das funções
file = open("structures.xml", "w")
goals = ['start']
document = read_xml("wp.xml")
file = get_groups(document, file)
file, goals = get_plans(document, file, goals)
file.close()