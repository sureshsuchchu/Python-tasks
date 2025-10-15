No_of_items=int(input("Enter tot no of items:"))
cost_of_per_item=100
tot_cost=No_of_items*cost_of_per_item

if tot_cost>2000:
    discount=tot_cost*0.10
    tot_cost=tot_cost-discount
print("tot cost of consumer:",tot_cost)
