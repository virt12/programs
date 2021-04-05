first_name=input("dsada")
second_name=input("dsadsa")

n1_v=0
n2_v=0

vo_id=[1,2,3,4,5,6,7,8,9,10]

nv=len(vo_id)

while True:
    if vo_id==[]:
        print("Voter session over")
        if n1_v>n2_v:
            percent=(n1_v/n2_v)*100
            print(n1_v,"First winner",percent)
        elif n2_v>n1_v:
            percent=(n2_v/n1_v)*100
            print(n2_v,"Second winner",percent)
    else:
        voter=int(input("Enter vote id"))
        if voter in vo_id:
            print("Voter")
            vo_id.remove(voter)
            v=int(input("dsadsad"))
            if v==1:
                n1_v+=1
                print("Voted")
            if v==2:
                n2_v+=1
                print("Voted")
        
        else:
            print("Not a voter here")