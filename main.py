import game_play
quit = ('quit','q')
run = ('run','r')
choice = ''

while choice not in quit:
	print("Run - Run game_play.py program")
	print("Quit - exit program")
	choice = input("Choose an option:\n").lower()
	if choice in run:
		print("<----Starting Program---->")
		game_play.main()
		print("<----Program Complete---->")
	elif choice in quit:
		print("Goodbye.")
	else:
		print("Invalid selection.")