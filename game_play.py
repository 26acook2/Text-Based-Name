def main():
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
post, mats, and a hose/sprinkler. 
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
You may also use them if your horse needs to be isolated.
There are no items in them. 
	"""
	Extra_storage_description = """
Welcome to the extra storage space! This is where all
obstacles are stored such as: barrels, cones, and poles.
	"""
	Paddock_description = """
Welcome to the paddock! This is where your horse roams
when they aren't being used. It includes water troughs,
hay nets, and a hose. 
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
def Paddock(Paddock_description, inventory):
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