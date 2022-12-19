market = {"strawberry":[0, 300], "carrot":[0, 500], "watermelon":[0, 2000],"melon":[0, 1000]}

while True:
	initial_input = int(input("0 : calculate, 1 : add\n"))
	straw=market["strawberry"]
	carrot=market["carrot"]
	watermelon=market["watermelon"]
	melon=market["melon"]
	
	if initial_input == 1:
		fruit = input()
		if fruit in market.keys():
			num_fruit = int(input())
			market[fruit][0] = market[fruit][0] + num_fruit
			print("strawberry : {}, carrot : {}, watermelon : {}, melon : {}".format(straw[0],carrot[0],watermelon[0],melon[0]))
			continue
		
		else:
			print("no product in market")
			print("strawberry : {}, carrot : {}, watermelon : {}, melon : {}".format(straw[0],carrot[0],watermelon[0],melon[0]))
		continue	
		
	elif initial_input == 0:
		total_straw=int(straw[0]*300)
		if straw[0]<10:
			straw_value=int(straw[0]*300)
		if 20>straw[0]>=10:
			straw_value=int(straw[0]*270)
		if straw[0]>=20:
			straw_value=int(straw[0]*220)
		
		total_carrot=int(carrot[0]*500)
		if carrot[0]<10:
			carrot_value=int(carrot[0]*500)
		if 20>straw[0]>=10:
			carrot_value=int(carrot[0]*450)
		if carrot[0]>=20:
			carrot_value=int(carrot[0]*370)
			
		total_watermelon=int(watermelon[0]*2000)	
		if 0<=watermelon[0]<3:
			watermelon_value=int(watermelon[0]*2000)
		if watermelon[0]>=3:
			watermelon_value=int(watermelon[0]*1600)
		
		total_mel=int(melon[0]*1000)
		if 0<=melon[0]<5:
			mel_value=int(melon[0]*1000)
		if melon[0]>=5:
			mel_value=int(melon[0]*800)
	

		total = total_straw + total_carrot + total_watermelon + total_mel
		discount = straw_value + carrot_value + watermelon_value + mel_value
		print("Here is recipt. Total price is {}. Discount price is {}.".format(total,discount))
		break


