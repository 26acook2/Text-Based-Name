from playing import Play
quit = ('quit','q')
run = ('run','r')
choice = ''
my_game = Play()
while choice not in quit:
	print("Run - Run playing.py program")
	print("Quit - exit program")
	choice = input("Choose an option:\n").lower()
	if choice in run:
		print("<----Starting Program---->")
		my_game.main()
		print("<----Program Complete---->")
	elif choice in quit:
		print("Goodbye.")
	else:
		print("Invalid selection.")