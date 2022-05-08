n=input("Enter the number of nodes: ")
Nodes={}

for i in range(1,int(n)+1):
    Nodes[i] = {}
    Nodes[i]["node_id"] = i
    Nodes[i]["next"] = (i+1)%(int(n)+1)
    if Nodes[i]["next"]==0:
       Nodes[i]["next"]=1

for i in range(int(n)):
    active = input("please enter the 1 for active status of node id # " + str(i+1)+" ")
    Nodes[i+1]["active"] = active


while True:
    id = input("Enter the id of node going to run the election algorithm: ")
    list=[]
    for key,value in Nodes.items():
       if int(Nodes[key]["node_id"])==int(id) and Nodes[key]["active"]=="1":
           list.append(Nodes[key]["node_id"])
           node=int(Nodes[key]["next"])
           while node != int(id):
               if Nodes[node]["active"] == "1":
                 list.append(node)
               node = int(Nodes[node]["next"])
           coordinator=max(list)
           print(list)
           print("The cordinator chosen from election algorithm is:",coordinator)
    active_update = input("Do you want to update the active status.Enter Y/N for Yes/No")
    if (active_update == "Y"):
        i = 1
        for key, value in Nodes.items():
            active = input("Enter the 1 for active status for the node with ID  " + str(i) + ":")
            Nodes[i]["active"] = active
            i += 1
    else:
        exit()