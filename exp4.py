def get_user_inputs():
    # take input for heuristic values
    heuristic={}
    num_nodes=int(input("Enter total no.of nodes:"))
    print("\n Enter heuristic value h(n) for each node:")
    for _ in range(num_nodes):
        node=input("Node name:").strip().upper()
        h_val=float(input(f"Heuristic h({node}):"))
        heuristic[node]=h_val
        