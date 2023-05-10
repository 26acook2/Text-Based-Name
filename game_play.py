def Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him):
	print (f"{Paddock_description}")
	Horse_status = False
	while Horse is True:
		release_choice = input(f"Do you want to releaes {Horse_name} in the paddock\n(Y-es or N-o)\n")
		if release_choice in ('Y' 'YES'):
			print(f"{Horse_name} is now in the paddock!")
			Horse_status = False
			return Horse_status
		elif release_choice in ('N', 'NO'):
			print(f"OK, you are still leading {Horse_name}")
		else:
			print("Sorry, that wasn't a valid choice please try again.")
	if Horse == False:
		catch_choice = input(f"Do you want to catch {Horse_name}?\n(Y-es or N-o)\n")
		if catch_choice.upper() in ('Y', 'YES'):
			if 'halter' in inventory:
				if 'lead rope' in inventory:
					print(f"Good job, you had the halter and lead rope to catch {Horse_name}! You are now leading {horse_pronoun_her_him}.")
					Horse_status = True
					return Horse_status
				else:
					print(f"You have a halter to put on {Horse_name}, but nothing to lead {horse_pronoun_her_him} with. Go grab a leadrope!")
			elif 'halter' not in inventory:
				print(f"Sorry, but you don't have a halter to use! Go grab the equipment to lead {Horse_name} with!")
		while catch_choice.upper() in ('N', 'NO'):
			stay_choice = input("OK, would you like to stay or leave the paddock?\n(S-tay or L-eave)\n")
			if stay_choice.upper() in ('S', 'STAY'):
				"Ok, you are staying in the paddock."
				while Horse is True:
					release_choice = input(f"Do you want to release	 {Horse_name} in the paddock\n(Y-es or N-o)\n")
					if release_choice in ('Y' 'YES'):
						print(f"{Horse_name} is now in the paddock!")
						Horse_status = False
						return Horse_status
					elif release_choice in ('N', 'NO'):
						print(f"OK, you are still leading {Horse_name}")
					else:
						print("Sorry, that wasn't a valid choice please try again.")
				if Horse == False:
					catch_choice = input(f"Do you want to catch {Horse_name}?\n(Y-es or N-o)\n")
					if catch_choice.upper() in ('Y', 'YES'):
						if 'halter' in inventory:
							if 'lead rope' in inventory:
								print(f"Good job, you had the halter and lead rope to catch {Horse_name}! You are now leading {horse_pronoun_her_him}.")
								Horse_status = True
								return Horse_status
							else:
								print(f"You have a halter to put on {Horse_name}, but nothing to lead {horse_pronoun_her_him} with. Go grab a leadrope!")
						elif 'halter' not in inventory:
							print(f"Sorry, but you don't have a halter to use! Go grab the equipment to lead {Horse_name} with!")
			elif stay_choice.upper() in ('L', 'LEAVE'):
				print("OK, you are leaving the paddock.")
				catch_choice = 'NA'
			else:
				print("Sorry, that wasn't a valid choice please try again.")
	return Horse_status
def Barn(Barn_description, inventory):
	print (f"{Barn_description}")
	grab_yn = input("Do you want to grab something from the barn?\n(Y-es or N-o)\n")
	if grab_yn.upper() in ('Y', 'YES'):
		what_grab = input("""
What do you want to grab?
H-halter
LR-lead rope
LL-lunge line
B-bridle
S-saddle
SP-saddle pad
SN-sinch
BC-breast collar
BR-brushes
HP-hoof picks
SC-shampoo/conditioner
HY-hay
G-grain
T-treats
""")
		if what_grab.upper() in ('H', 'HALTER'):
			inventory.append('halter')
			print ("A halter has been added to your inventory!")
		elif what_grab.upper() in ('LR', 'LEAD ROPE'):
			inventory.append('lead rope')
			print ("A lead rope has been added to your inventory!")
		elif what_grab.upper() in ('LL', 'LUNGE LINE'):
			inventory.append('lunge line')
			print ("A lunge line has been added to your inventory!")
		elif what_grab.upper() in ('B', 'BRIDLE'):
			inventory.append('bridle')
			print ("A bridle has been added to your inventory!")
		elif what_grab.upper() in ('S', 'SADDLE'):
			inventory.append('saddle')
			print ("A saddle has been added to your inventory!")
		elif what_grab.upper() in ('SP', 'SADDLE PAD'):
			inventory.append('saddle pad')
			print ("A saddle pad has been added to your inventory!")
		elif what_grab.upper() in ('SN', 'SINCH'):
			inventory.append('sinch')
			print ("A sinch has been added to your inventory!")
		elif what_grab.upper() in ('BC', 'BREAST COLLAR'):
			inventory.append('breast collar')
			print ("A breast collar has been added to your inventory!")
		elif what_grab.upper() in ('BR', 'BRUSHES'):
			inventory.append('brushes')
			print ("Brushes have been added to your inventory!")
		elif what_grab.upper() in ('HP', 'HOOF PICKS'):
			inventory.append('hoof picks')
			print ("A hoof pick has been added to your inventory!")
		elif what_grab.upper() in ('SC', 'SHAMPOO/CONDITIONER'):
			inventory.append('shampoo/conditioner')
			print ("Shampoo and conditioner have been added to your inventory!")
		elif what_grab.upper() in ('HY', 'HAY'):
			inventory.append('hay')
			print ("Hay has been added to your inventory!")
		elif what_grab.upper() in ('G', 'GRAIN'):
			inventory.append('grain')
			print ("Grain has been added to your inventory!")
		elif what_grab.upper() in ('T', 'TREATS'):
			inventory.append('treats')
			print ("Treats have been added to your inventory!")
		else:
			print("Sorry, that wasn't a valid choice. Please try again!")
			what_grab = input("""
What do you want to grab?
H-halter
LR-lead rope
LL-lunge line
B-bridle
S-saddle
SP-saddle pad
SN-sinch
BC-breast collar
BR-brushes
HP-hoof picks
SC-shampoo/conditioner
HY-hay
G-grain
T-treats
""")
	elif grab_yn.upper() in ('N', 'NO'):
		print("OK, nothing was added to your inventory.")
	else:
		print("Sorry, that wasn't a valid choice. Please try again!")
		grab_yn = input("Do you want to grab something from the barn?\n(Y-es or N-o)\n")
		if grab_yn.upper() in ('Y', 'YES'):
			what_grab = input("""
	What do you want to grab?
	H-halter
	LR-lead rope
	LL-lunge line
	B-bridle
	S-saddle
	SP-saddle pad
	SN-sinch
	BC-breast collar
	BR-brushes
	HP-hoof picks
	SC-shampoo/conditioner
	HY-hay
	G-grain
	T-treats
	""")
			if what_grab.upper() in ('H', 'HALTER'):
				inventory.append('halter')
				print ("A halter has been added to your inventory!")
			elif what_grab.upper() in ('LR', 'LEAD ROPE'):
				inventory.append('lead rope')
				print ("A lead rope has been added to your inventory!")
			elif what_grab.upper() in ('LL', 'LUNGE LINE'):
				inventory.append('lunge line')
				print ("A lunge line has been added to your inventory!")
			elif what_grab.upper() in ('B', 'BRIDLE'):
				inventory.append('bridle')
				print ("A bridle has been added to your inventory!")
			elif what_grab.upper() in ('S', 'SADDLE'):
				inventory.append('saddle')
				print ("A saddle has been added to your inventory!")
			elif what_grab.upper() in ('SP', 'SADDLE PAD'):
				inventory.append('saddle pad')
				print ("A saddle pad has been added to your inventory!")
			elif what_grab.upper() in ('SN', 'SINCH'):
				inventory.append('sinch')
				print ("A sinch has been added to your inventory!")
			elif what_grab.upper() in ('BC', 'BREAST COLLAR'):
				inventory.append('breast collar')
				print ("A breast collar has been added to your inventory!")
			elif what_grab.upper() in ('BR', 'BRUSHES'):
				inventory.append('brushes')
				print ("Brushes have been added to your inventory!")
			elif what_grab.upper() in ('HP', 'HOOF PICKS'):
				inventory.append('hoof picks')
				print ("A hoof pick has been added to your inventory!")
			elif what_grab.upper() in ('SC', 'SHAMPOO/CONDITIONER'):
				inventory.append('shampoo/conditioner')
				print ("Shampoo and conditioner have been added to your inventory!")
			elif what_grab.upper() in ('HY', 'HAY'):
				inventory.append('hay')
				print ("Hay has been added to your inventory!")
			elif what_grab.upper() in ('G', 'GRAIN'):
				inventory.append('grain')
				print ("Grain has been added to your inventory!")
			elif what_grab.upper() in ('T', 'TREATS'):
				inventory.append('treats')
				print ("Treats have been added to your inventory!")
			else:
				print("Sorry, that wasn't a valid choice. Please try again!")
				what_grab = input("""
	What do you want to grab?
	H-halter
	LR-lead rope
	LL-lunge line
	B-bridle
	S-saddle
	SP-saddle pad
	SN-sinch
	BC-breast collar
	BR-brushes
	HP-hoof picks
	SC-shampoo/conditioner
	HY-hay
	G-grain
	T-treats
	""")
				
	stay_ask = input("""
Do you want to stay in the barn, or leave?
S-tay
L-eave
""")

	while stay_ask.upper() in ('S', 'STAY'):
		print("OK, you are staying in the barn.")
		grab_yn = input("Do you want to grab something from the barn?\n(Y-es or N-o)\n")
		if grab_yn.upper() in ('Y', 'YES'):
			what_grab = input("""
What do you want to grab?
H-halter
LR-lead rope
LL-lunge line
B-bridle
S-saddle
SP-saddle pad
SN-sinch
BC-breast collar
BR-brushes
HP-hoof picks
SC-shampoo/conditioner
HY-hay
G-grain
T-treats
""")
			if what_grab.upper() in ('H', 'HALTER'):
				inventory.append('halter')
				print ("A halter has been added to your inventory!")
			elif what_grab.upper() in ('LR', 'LEAD ROPE'):
				inventory.append('lead rope')
				print ("A lead rope has been added to your inventory!")
			elif what_grab.upper() in ('LL', 'LUNGE LINE'):
				inventory.append('lunge line')
				print ("A lunge line has been added to your inventory!")
			elif what_grab.upper() in ('B', 'BRIDLE'):
				inventory.append('bridle')
				print ("A bridle has been added to your inventory!")
			elif what_grab.upper() in ('S', 'SADDLE'):
				inventory.append('saddle')
				print ("A saddle has been added to your inventory!")
			elif what_grab.upper() in ('SP', 'SADDLE PAD'):
				inventory.append('saddle pad')
				print ("A saddle pad has been added to your inventory!")
			elif what_grab.upper() in ('SN', 'SINCH'):
				inventory.append('sinch')
				print ("A sinch has been added to your inventory!")
			elif what_grab.upper() in ('BC', 'BREAST COLLAR'):
				inventory.append('breast collar')
				print ("A breast collar has been added to your inventory!")
			elif what_grab.upper() in ('BR', 'BRUSHES'):
				inventory.append('brushes')
				print ("Brushes have been added to your inventory!")
			elif what_grab.upper() in ('HP', 'HOOF PICKS'):
				inventory.append('hoof picks')
				print ("A hoof pick has been added to your inventory!")
			elif what_grab.upper() in ('SC', 'SHAMPOO/CONDITIONER'):
				inventory.append('shampoo/conditioner')
				print ("Shampoo and conditioner have been added to your inventory!")
			elif what_grab.upper() in ('HY', 'HAY'):
				inventory.append('hay')
				print ("Hay has been added to your inventory!")
			elif what_grab.upper() in ('G', 'GRAIN'):
				inventory.append('grain')
				print ("Grain has been added to your inventory!")
			elif what_grab.upper() in ('T', 'TREATS'):
				inventory.append('treats')
				print ("Treats have been added to your inventory!")
			else:
				print("Sorry, that wasn't a valid choice. Please try again!")
				what_grab = input("""
What do you want to grab?
H-halter
LR-lead rope
LL-lunge line
B-bridle
S-saddle
SP-saddle pad
SN-sinch
BC-breast collar
BR-brushes
HP-hoof picks
SC-shampoo/conditioner
H-hay
G-grain
T-treats
""")
		elif grab_yn.upper() in ('N', 'NO'):
			print("OK, nothing was added to your inventory.")
		else:
			print("Sorry, that wasn't a valid choice. Please try again!")
			grab_yn = input("Do you want to grab something from the barn?\n(Y-es or N-o)\n")
		stay_ask = input("""
Do you want to stay in the barn, or leave?
S-tay
L-eave
""")
		if stay_ask.upper() in ('L', 'LEAVE'):
			print("OK, you are leaving the barn.")
def Extra_Storage(Extra_storage_description, inventory):
	print (f"{Extra_storage_description}")
	grab_yn = input("Do you want to grab something from storage?\n(Y-es or N-o)\n")
	if grab_yn.upper() in ('Y', 'YES'):
		what_grab = input("""
What do you want to grab?
B-barrels
C-cones
P-poles
""")
		if what_grab.upper() in ('B', 'BARRELS'):
			inventory.append('barrels')
			print ("Barrels have been added to your inventory!")
		elif what_grab.upper() in ('C', 'CONES'):
			inventory.append('cones')
			print ("Cones have been added to your inventory!")
		elif what_grab.upper() in ('P', 'POLES'):
			inventory.append('poles')
			print ("Poles have been added to your inventory!")
		else:
			print("Sorry, that wasn't a valid choice. Please try again!")
			what_grab = input("""
What do you want to grab?
B-barrels
C-cones
P-poles
""")
	elif grab_yn.upper() in ('N', 'NO'):
		print("OK, nothing was added to your inventory.")
	else:
		print("Sorry, that wasn't a valid choice. Please try again!")
		grab_yn = input("Do you want to grab something from storage?\n(Y-es or N-o)\n")
		if grab_yn.upper() in ('Y', 'YES'):
			what_grab = input("""
	What do you want to grab?
B-barrels
C-cones
P-poles
""")
		if what_grab.upper() in ('B', 'BARRELS'):
			inventory.append('barrels')
			print ("Barrels have been added to your inventory!")
		elif what_grab.upper() in ('C', 'CONES'):
			inventory.append('cones')
			print ("Cones have been added to your inventory!")
		elif what_grab.upper() in ('P', 'POLES'):
			inventory.append('poles')
			print ("Poles have been added to your inventory!")
		else:
			print("Sorry, that wasn't a valid choice. Please try again!")
			what_grab = input("""
What do you want to grab?
B-barrels
C-cones
P-poles
""")
				
	stay_ask = input("""
Do you want to stay in storage, or leave?
S-tay
L-eave
""")

	while stay_ask.upper() in ('S', 'STAY'):
		print("OK, you are staying in storage.")
		grab_yn = input("Do you want to grab something from storage?\n(Y-es or N-o)\n")
		if grab_yn.upper() in ('Y', 'YES'):
			what_grab = input("""
What do you want to grab?
B-barrels
C-cones
P-poles
""")
			if what_grab.upper() in ('B', 'BARRELS'):
				inventory.append('barrels')
				print ("Barrels have been added to your inventory!")
			elif what_grab.upper() in ('C', 'CONES'):
				inventory.append('cones')
				print ("Cones have been added to your inventory!")
			elif what_grab.upper() in ('P', 'POLES'):
				inventory.append('poles')
				print ("Poles have been added to your inventory!")
			else:
				print("Sorry, that wasn't a valid choice. Please try again!")
				what_grab = input("""
What do you want to grab?
B-barrels
C-cones
P-poles
""")
		elif grab_yn.upper() in ('N', 'NO'):
			print("OK, nothing was added to your inventory.")
		else:
			print("Sorry, that wasn't a valid choice. Please try again!")
			grab_yn = input("Do you want to grab something from storage?\n(Y-es or N-o)\n")
		stay_ask = input("""
Do you want to stay in the barn, or leave?
S-tay
L-eave
""")
		if stay_ask.upper() in ('L', 'LEAVE'):
			print("OK, you are leaving storage.")
def Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him):
	print (f"{Round_Pen_description}")
	if Horse == True:
		lunge_choice = input(f"Do you want to free lunge {Horse_name}?\n(Y-es, or N-o)\n")
		if lunge_choice.upper() in ('Y', 'YES'):
			print(f"""
You are free lunging {Horse_name}
lunging...
lunging...
lunging...
""")
			print(f"You are now done lunging {horse_pronoun_her_him}.")
		elif lunge_choice.upper() in ('N', 'NO'):
			print(f"OK, you are not lunging {Horse_name}.")
		else:
			print("Sorry, that wasn't a valid input. Please try again.")
			lunge_choice = input(f"Do you want to free lunge {Horse_name}?\n(Y-es, or N-o)\n")
			if lunge_choice.upper() in ('Y', 'YES'):
				print(f"""
You are free lunging {Horse_name}
lunging...
lunging...
lunging...
""")
				print(f"You are now done lunging {horse_pronoun_her_him}.")
			elif lunge_choice.upper() in ('N', 'NO'):
				print(f"OK, you are not lunging {Horse_name}.")
	elif Horse == False:
		print(f"Sorry, but you don't have a horse to lunge. Go grab {Horse_name} and try again!")
	stay_ask = input("""
Do you want to stay in the round pens, or leave?
S-tay
L-eave
""")
	while stay_ask.upper() in ('S', 'STAY'):
		print("OK, you are staying in the round pens.")
		if Horse == True:
			lunge_choice = input(f"Do you want to free lunge {Horse_name}?\n(Y-es, or N-o)\n")
			if lunge_choice.upper() in ('Y', 'YES'):
				print(f"""
You are free lunging {Horse_name}
lunging...
lunging...
lunging...
""")
				print(f"You are now done lunging {horse_pronoun_her_him}.")
			elif lunge_choice.upper() in ('N', 'NO'):
				print(f"OK, you are not lunging {Horse_name}.")
			else:
				print("Sorry, that wasn't a valid input. Please try again.")
				lunge_choice = input(f"Do you want to free lunge {Horse_name}?\n(Y-es, or N-o)\n")
				if lunge_choice.upper() in ('Y', 'YES'):
					print(f"""
You are free lunging {Horse_name}
lunging...
lunging...
lunging...
""")
					print(f"You are now done lunging {horse_pronoun_her_him}.")
				elif lunge_choice.upper() in ('N', 'NO'):
					print(f"OK, you are not lunging {Horse_name}.")
		elif Horse == False:
			print(f"Sorry, but you don't have a horse to lunge. Go grab {Horse_name} and try again!")
		stay_ask = input("""
Do you want to stay in the round pens, or leave?
S-tay
L-eave
""")
		if stay_ask.upper() in ('L', 'LEAVE'):
			print("OK, you are leaving the round pens.")
def Arena(Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him):
	print (f"{Arena_description}")
	if Horse == False:
		print(f"Sorry, you don't have a horse to work with!\nGo catch {Horse_name} and come back!")
	elif Horse == True:
		act_choice = input(f"""
What would you like to do?
B-brush
R-ride
T-tack up
BA-Bathe {Horse_name}
""")
		if act_choice.upper() in ('B', 'BRUSH'):
			if 'brushes' in inventory:
				if 'hoof picks' in inventory:
					print(f"Great work! You successfully brushed and picked {Horse_name}'s feet.")
				else:
					print(f"You brushed off {Horse_name}, but you didn't have a hoof pick to clean out her hooves.\n Grab a hoof pick and try again.")
			else:
				if 'hoof picks' in inventory:
					print(f"You cleaned out {Horse_name}'s hooves, but didn't have brushes to brush her down.\n Go grab brushes and try again.")
				else:
					print(f"Sorry, you didn't have hoof picks or brushes for {Horse_name}.\nGo grab the supplies and try again.")
		elif act_choice.upper() in ('BA')

def main():
	Horse = False
	inventory = []
	Map = """
     	    _____________
     	   |             |
	   |    Arena    |_______
 __________|_____________|       | 
|          |      |      | Extra | 
|   Barn   | Round Pens  |Storage|
|__________|______|______|_______|
|                                |
|                                |
|             Paddock            |
|________________________________|
"""
	Intro = """
Welcome to the equestrian game simulator!
In this game you will become an equestrian,
and take part in their daily lives. The 
objective is to take care of your horse, 
and deal with the problems that may arise. 
You also want to take care of yourself, and
allow time for riding! This game ends at the
end of the day. Good luck!
	"""
	Arena_description = """
Welcome to the arena! This is where you will ride,
tack up, brush, and more! The arena includes a tying 
post, and mats.
	"""
	Barn_description = """
Welcome to the barn! This is where all necessary 
equipment is stored such as: tack, food, treats, etc.
It includes:
-halters
-lead ropes
-lunge lines
-bridles
-saddles
-saddle pads
-sinches
-breast collars
-brushes
-hoof picks
-horse shampoo/conditioner
-hay
-grain
-treats
	"""
	Round_Pen_description = """
Welcome to the round pens! This is where you can round
pen your horses, either to warm up, or to excersise them.
There are no items in them. 
	"""
	Extra_storage_description = """
Welcome to the extra storage space! This is where all
obstacles are stored such as: barrels, cones, and poles.
	"""
	Paddock_description = """
Welcome to the paddock! This is where your horse roams
when they aren't being used. It includes a hay net.
	"""

	print (f"{Intro}")
	print (f"{Map}")
	Horse_name = input("What is your horse's name?\n")
	Horse_gender = input("What gender is your horse? (F-emale or M-ale)\n")
	while Horse_gender.upper() not in ('F', 'FEMALE', 'M', 'MALE'):
		print ("Invalid input, please try again.")
		Horse_gender = input("What gender is your horse? (F-emale or M-ale)\n")
	if Horse_gender.upper() in ('F', 'FEMALE'):
		horse_pronoun_her_him = 'her'
		horse_pronoun_she_he = 'she'
	else:
		horse_pronoun_her_him = 'him'
		horse_pronoun_she_he = 'he'
	print (f"""
It's 6 am in the morning. You hear the roosters crowing
and you know it's time to wake up and get a start on the day. 
Let's get to work with {Horse_name}! Go catch {horse_pronoun_her_him}!
(Remember, you need a halter and leadrope to catch {horse_pronoun_her_him})
""")
	
	while Horse is False:
		choice = input("""
Where do you want to go?
A-rena
B-arn
E-xtra Storage
P-addock
R-ound Pens
""")
		if choice.upper() in ('B', 'BARN'):
			Barn(Barn_description, inventory)
		elif choice.upper() in ('P', 'PADDOCK'):
			Horse = Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
		elif choice.upper() in ('E', 'EXTRA STORAGE'):
			Extra_Storage(Extra_storage_description, inventory)
		elif choice.upper() in ('R', 'ROUND PENS'):
			Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him)

	while Horse is True:
		choice = input("""
Where do you want to go?
A-rena
B-arn
E-xtra Storage
P-addock
R-ound Pens
""")
		if choice.upper() in ('B', 'BARN'):
			Barn(Barn_description, inventory)
		elif choice.upper() in ('P', 'PADDOCK'):
			Horse = Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
		elif choice.upper() in ('E', 'EXTRA STORAGE'):
			Extra_Storage(Extra_storage_description, inventory)
		elif choice.upper() in ('R', 'ROUND PENS'):
			Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him)