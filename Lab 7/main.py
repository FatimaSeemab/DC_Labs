n=input("Enter the number of nodes: ")
Nodes={}
for i in range(int(n)):
    Nodes[i]={}
    priority = input("Enter the priority for the node with ID :" +str(i+1) +" ")
    active=input("Enter the 1 for active status for the node with ID :"+ str(i+1)+" ")
    Nodes[i]["node_id"] = i+1
    Nodes[i]["priority"] = priority
    Nodes[i]["active"] = active

max_pri=-1

for key,value in Nodes.items():
   if max_pri < int(Nodes[key]["priority"]) and Nodes[key]["active"]=="1":
       id=Nodes[key]["node_id"]
       max_pri = int(Nodes[key]["priority"])

if max_pri == -1:
    print("No node is active")
else:
    print("The coordinator chosen by the bully algorithm has ID:", max_pri)

while True:
    id = input("Enter the id of node going to run the election algorithm: ")
    max_pri = -1
    for key,value in Nodes.items():
       if int(Nodes[key]["node_id"])>=int(id) :
           print("message sent to id"+str(Nodes[key]["node_id"]))
           if max_pri < int(Nodes[key]["priority"]) and Nodes[key]["active"] == "1":
               max_pri = int(Nodes[key]["priority"])

    if max_pri==-1:
        print("No node is active")
    else:
        print("The coordinator chosen has ID:", max_pri)

    active_update=input("Do you want to update the active status.Enter Y/N for Yes/No  ")
    if(active_update=="Y"):
        i=0
        for key, value in Nodes.items():
            active = input("Enter the 1 for active status for the node with ID  " + str(i+1) + ":")
            Nodes[i]["active"] = active
            i += 1
    else:
        exit()

