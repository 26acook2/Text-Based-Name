from playing import Play
from playing import load
quit = ('quit','q')
run = ('run','r')
load_game = ('load', 'l')
choice = ''
my_game = Play()
while choice not in quit:
	print("Run - Run playing.py program")
	print("Quit - exit program")
	print("Load - load game")
	choice = input("Choose an option:\n").lower()
	if choice in run:
		print("<----Starting Program---->")
		my_game.main()
		print("<----Program Complete---->")
	elif choice in quit:
		print("Goodbye.")
	elif choice in load_game:
		load()
	else:
		print("Invalid selection.")