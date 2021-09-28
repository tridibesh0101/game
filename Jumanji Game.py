print("Hello Friend!!\nWelcome to\n Jumanji the game")
name=input("What's your name?? : ")
age=input("What's your age?? : ")
age=int(age)
print("Hey",name)
hey=int(input ("Wanna play this game? (1/0) :"))
if hey==True:
	print("Okay!!\nLet's the journey beign\nYour health = 1\nThat means you've 1 life\nSo, be carefull :)")
	journey=int(input("Choose your charecter\n (1) Spencer\t (2) Martha\t (3) Alan\t (4) Angela\n(1/2/3/4):"))
	if journey==1:
		spe="\twelcome to jumanji"
		print(spe.upper())
	elif journey==2:
		spe="\twelcome to jumanji"
		print(spe.upper())
	elif journey==3:
		spe="\twelcome to jumanji"
		print(spe.upper())
	elif journey==4:
		spe="\twelcome to jumanji"
		print(spe.upper())
	print(" Suddenly you wake up and saw that you are lie in a room which has two door in front of you.\n Now choose one\n Which door you wanna open?")
	martha=int(input("Left [1]\tor\tRight [0] :"))
	if martha==1:
		print("Oops!! You fall down and reach near the bank of a river\n What would you do?")
		spo_ky=int(input("swim [1]\t or\tgo to jungel [0] :"))
		if spo_ky==1:
			print("Shit!!! Suddenly a croc hunt you")
			h_t="\t game over"
			print(h_t.upper())
		else:
			print("Oh no!!! There is a grizly bear rush you\n What would you do now?")
			we_t=int(input("climb a tree [1]\t or\tstay running [0] :"))
			if we_t==1:
				print("Shit!!! Suddenly your leg slept when climbing and fall down then the bear take bite your neck ")
				
				r_y="\t game over"
				print(r_y.upper())
			else:
					print ("Fuck!!! You get hurt by a rock and fall down then the bear rush to you and you've been hunted")
					r_t="\t  game over"
					print(r_t.upper())
			
	else:
		print("Whoa!!! You entered in an another room which has another door and a bomb.\n if you waste your time that bomb will be explode.  \n What would you do now? ")
		e_t=int(input("open the door [1]\t or\tstay[0] :"))
		if e_t==1:
			print("By opening the door, you see that there is a underground tunnel also you have not much time to think about that tunnel.Cuz if you wait, that room where the bomb planted will explode soon.\n So what are you waiting for? ")
			g_t=int(input("GO!!! [1] :"))
			if g_t==1:
				print("wee!!!you saw other side of the tunnel sunlight comes. escape that tunnel. \nWhoa!!! escaping the tunnel you see that you reach in a deep jungel and near you see a knife.\nWhat would you do now?")
				u_i=int(input("take that knife [1]\t or\tunderstimate that thing [0] :"))
				if u_i==1:
					print("Good!!! your decition will help you next step.\n Now you have to make decition which direction you wanna go?")
					y_e=int(input("east [1]\t or \twest [0] :"))
					if y_e==1:
						print("By choosing east you reach the bank of a river and there you see a boat\n\'Yes\' there is no dougt that you ride that boat but that boat has no stick that you could sink it.\nFortunately there are many bamboo bush that you could make your stick if you've knife\nDoes you 've any knife? ")
						b_u=int(input("yep [1]\t or\tnope [0] :"))
						
						if b_u==1:
							print("well done!!! you made it\nNow start journey with your boat to reach other side of the river of the island\nThere you see a JUMANJI milestone\n\tBooooyah!!!")
						
						else:
								print("Very bad!!\nBy forget keeping knife with you now you pay for uderstimate that knife.\n Now you can't make your own stick to overcome this situation\nMeanwhile you hear something wierd\nOops that's a jaguar hunt you\n\t GAMEOVER")
							
					else:
						print("By choosing west you reach swampy  lake where crocs are waiting for dinner and there is no way to avoid that swampy lake\nYou have to cross this lake on foot\nIf you thought that you stay there\nThat foolish choise pay your life by hunted a panther\nSo what would you do now?")
						t_u=int(input("stay [1]\t or\tokeep going [0] :"))
						if t_u==1:
							print("\t  RIP\n\tYou Coward")
						else:
							print("\t  RIP\n\tYou Bravy Soul")
					
				else:
					print("well!!!\nNow you have to make decition which direction you wanna go?")
					t_r=int(input("east [1]\t or \twest [0] :"))
					if t_r==1:
						print("By choosing east you reach the bank of a river and there you see a boat\n\'Yes\' there is no dougt that you ride that boat but that boat has no stick that you could sink it.\nFortunately there are many bamboo bush that you could make your stick if you've knife\nDoes you 've any knife?")
						y_o=int(input("nope [0] :"))
						if y_o==0:
							print("Very bad!!\nBy forget keeping knife with you now you pay for uderstimate that knife.\n Now you can't make your own stick to overcome this situation\nMeanwhile you hear something wierd\nOops that's a jaguar hunt you\n\t GAMEOVER")
						
					else:
						print("By choosing west you reach swampy  lake where crocs are waiting for dinner and there is no way to avoid that swampy lake\nYou have to cross this lake on foot\nIf you thought that you stay there\nThat foolish choise pay your life by hunted a panther\nSo what would you do now?")
						r_u=int(input("stay [1]\t or\tokeep going [0] :"))
						if r_u==1:
							print("\t  RIP\n\tYou Coward")
						else:
							print("\t  RIP\n\tYou Bravy Soul")
		else:
			print("\t Baaaaaam!!!")
			r_u="\t game over"
			print(r_u.upper())
		
else:
	print("0kay friend!!\n Have a nice day :)")