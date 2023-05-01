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
-horse shampoo/condioner
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
Horse_name = input("What is your horse's name?")
Horse_gender = input("What gender is your horse? (F-emale or M-ale)")
while Horse_gender != ('F', 'Female', 'M', 'Male'):
    print ("Invalid input, please try again.")
    Horse_gender = input("What gender is your horse? (F-emale or M-ale)")
