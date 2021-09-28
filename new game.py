print("Hello Friend!! \n welcome to my first game")
input("What's your name? : ")
player=int(input("What's your age? : "))



if player <= 4 :
	print ("Sorry friend :(  \n You can't play this game")
elif player >=4 :
	print ("You're able to play this game :) \n wanna play!? ")
	play=int(input("yes or no(1/0) :"))	
	
	if play==1 :
		print ("Oneday you and all of  your friends arrange a picnic by the side of the river bank. Suddenly you saw a aligator near in your picnic spot.  \n what would you do? ")
		cave=int(input("Shout and inform them or catch the aligator (1/0) :"))
		
		if cave==1:
			print ("good!! you have common sense\n But some one ran away. Unfotunately that friend killed by that aligator\n your leader wanted to escape that place but all of you forgot where you come from\ what would you do then?")
			bank=int(input("call your parents and say that its your last call to them or make smoke to inform near the villegers (1/0) : "))
			
			if bank==1:
				print("hah you prove that you're a coward. so what would you expect now.")
			else :
					print ("bravo!!! you're insane ")
		else :
			print("game over")
		
	else  :
		print ("okay !! \n have a nice day :)")
'''		
		if cave==1:
			print ("good!! you have common sense\n But some one ran away. Unfotunately that friend killed by that aligator\n your leader wanted to escape that place but all of you forgot where you come from\ what would you do then?")
			bank=int(input("call your parents and say that its your last call to them or make smoke to inform near the villegers"))
		else :
			print("game over!!")'''
	