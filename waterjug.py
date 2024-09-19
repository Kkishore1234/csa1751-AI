def waterjug(jug1cap,jug2cap,target,jug1=0,jug2=0,visited=None):
    if visited is None:
        visited=set()
    if jug1==target or jug2==target:
        print(f"solved jug1:{jug1} ,jug2:{jug2}")
        return True
    if (jug1,jug2) in visited:
        return False
    visited.add((jug1,jug2))
    return(
            waterjug(jug1cap,jug2cap,target,jug1cap,jug2,visited) or
            waterjug(jug1cap,jug2cap,target,jug1,jug2cap,visited) or
            waterjug(jug1cap,jug2cap,target,0,jug2,visited) or
            waterjug(jug1cap,jug2cap,target,jug1,0,visited) or
            waterjug(jug1cap,jug2cap,target,max(0,jug1-(jug2cap-jug2)),min(jug2cap,jug1+jug2),visited) or
            waterjug(jug1cap,jug2cap,target,max(0,jug2-(jug1cap-jug1)),min(jug1cap,jug1+jug2),visited)
           )
waterjug(4,3,2)