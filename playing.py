import pickle
class Play:
    def save(self, Horse, Tacked_Up, Brushed, inventory, Horse_name, Horse_gender):
        with open ('Horse.pickle', 'wb') as f:
            pickle.dump(Horse, f)
        with open ('Tacked_Up.pickle', 'wb') as f:
            pickle.dump(Tacked_Up, f)
        with open ('Brushed.pickle', 'wb') as f:
            pickle.dump(Brushed, f)
        with open ('inventory.pickle', 'wb') as f:
            pickle.dump(inventory, f)
        with open ('Horse_name', 'wb') as f:
            pickle.dump(Horse_name, f)
        with open ('Horse_gender', 'wb') as f:
            pickle.dump(Horse_gender, f)
    def Paddock(self, Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him):
        print (f"{Paddock_description}")
        Horse_status = False
        if Horse is True:
            release_choice = input(f"Do you want to releaes {Horse_name} in the paddock\n(Y-es or N-o)\n")
            if release_choice.upper() in ('Y' 'YES'):
                print(f"{Horse_name} is now in the paddock!")
                Horse_status = False
                return Horse_status
            elif release_choice.upper() in ('N', 'NO'):
                print(f"OK, you are still leading {Horse_name}")
                Horse_status = True
                return Horse_status
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
    def Barn(self, Barn_description, inventory):
        print (f"{Barn_description}")
        grab_yn = input("Do you want to grab something from the barn?\n(Y-es or N-o)\n")
        if grab_yn.upper() in ('Y', 'YES'):
            what_grab = input("""
What do you want to grab?
H-halter
LR-lead rope
B-bridle
S-saddle
SP-saddle pad
SN-sinch
BC-breast collar
BR-brushes
HP-hoof picks
SC-shampoo/conditioner
T-treats
""")
            if what_grab.upper() in ('H', 'HALTER'):
                inventory.append('halter')
                print ("A halter has been added to your inventory!")
            elif what_grab.upper() in ('LR', 'LEAD ROPE'):
                inventory.append('lead rope')
                print ("A lead rope has been added to your inventory!")
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
B-bridle
S-saddle
SP-saddle pad
SN-sinch
BC-breast collar
BR-brushes
HP-hoof picks
SC-shampoo/conditioner
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
B-bridle
S-saddle
SP-saddle pad
SN-sinch
BC-breast collar
BR-brushes
HP-hoof picks
SC-shampoo/conditioner
T-treats
""")
                if what_grab.upper() in ('H', 'HALTER'):
                    inventory.append('halter')
                    print ("A halter has been added to your inventory!")
                elif what_grab.upper() in ('LR', 'LEAD ROPE'):
                    inventory.append('lead rope')
                    print ("A lead rope has been added to your inventory!")
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
B-bridle
S-saddle
SP-saddle pad
SN-sinch
BC-breast collar
BR-brushes
HP-hoof picks
SC-shampoo/conditioner
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
B-bridle
S-saddle
SP-saddle pad
SN-sinch
BC-breast collar
BR-brushes
HP-hoof picks
SC-shampoo/conditioner
T-treats
""")
                if what_grab.upper() in ('H', 'HALTER'):
                    inventory.append('halter')
                    print ("A halter has been added to your inventory!")
                elif what_grab.upper() in ('LR', 'LEAD ROPE'):
                    inventory.append('lead rope')
                    print ("A lead rope has been added to your inventory!")
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
B-bridle
S-saddle
SP-saddle pad
SN-sinch
BC-breast collar
BR-brushes
HP-hoof picks
SC-shampoo/conditioner
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
    def Extra_Storage(self, Extra_storage_description, inventory):
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
                inventory.append('obstacle')
                print ("Barrels have been added to your inventory!")
            elif what_grab.upper() in ('C', 'CONES'):
                inventory.append('obstacle')
                print ("Cones have been added to your inventory!")
            elif what_grab.upper() in ('P', 'POLES'):
                inventory.append('obstacle')
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
                inventory.append('obstacle')
                print ("Barrels have been added to your inventory!")
            elif what_grab.upper() in ('C', 'CONES'):
                inventory.append('obstacle')
                print ("Cones have been added to your inventory!")
            elif what_grab.upper() in ('P', 'POLES'):
                inventory.append('obstacle')
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
                    inventory.append('obstacle')
                    print ("Barrels have been added to your inventory!")
                elif what_grab.upper() in ('C', 'CONES'):
                    inventory.append('obstacle')
                    print ("Cones have been added to your inventory!")
                elif what_grab.upper() in ('P', 'POLES'):
                    inventory.append('obstacle')
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
    def Round_Pens(self, Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him, inventory):
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
                inventory.append('Lunged')
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
                    inventory.append('Lunged')
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
    def Arena(self, Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him, Tacked_Up):
        print (f"{Arena_description}")
        Tack_temp = False
        if Horse == False:
            print(f"Sorry, you don't have a horse to work with!\nGo catch {Horse_name} and come back!")
        elif Horse == True:
            act_choice = input(f"""
What would you like to do?
B-brush
R-ride
T-tack up
BA-bathe {Horse_name}
U-untack
""")
            if act_choice.upper() in ('B', 'BRUSH'):
                if 'brushes' in inventory:
                    if 'hoof picks' in inventory:
                        print(f"Great work! You successfully brushed and picked {Horse_name}'s feet.")
                        inventory.append('Brushed')
                    else:
                        print(f"You brushed off {Horse_name}, but you didn't have a hoof pick to clean out her hooves.\n Grab a hoof pick and try again.")
                else:
                    if 'hoof picks' in inventory:
                        print(f"You cleaned out {Horse_name}'s hooves, but didn't have brushes to brush her down.\n Go grab brushes and try again.")
                    else:
                        print(f"Sorry, you didn't have hoof picks or brushes for {Horse_name}.\nGo grab the supplies and try again.")
            elif act_choice.upper() in ('BA', 'BATHE'):
                if 'shampoo/conditioner' in inventory:
                    print(f"""
Good job, you had the shampoo and conditioner to clean {Horse_name}!
Bathing...
Bathing...
Bathing...
{Horse_name} is now freshly clean!
""")
                    inventory.append('Bathed')
                else:
                    print("Sorry, you didn't have shampoo/conditioner to use.\nGrab some, and try again.")
            elif act_choice.upper() in ('U', 'UNTACK'):
                if 'Tacked' in inventory:
                    print(f"Good work, you untacked {Horse_name}.")
                    inventory.remove('Tacked')
                    inventory.append('Untacked')
                else:
                    print(f"Sorry, {Horse_name} wasn't tacked up, so you can't untack {horse_pronoun_her_him}.")
            elif act_choice.upper() in ('T', 'TACK UP'):
                print("""
To tack up your horse to ride follow these steps:
1) Put on the saddle pad
2) Put on the saddle
3) Put on the sinch
4) Put on the breast collar
5) Put on the bridle
""")
                if 'saddle pad' in inventory:
                    print(f"You have the saddle pad, and put it on {Horse_name}.")
                    Tack_temp = False
                    if 'saddle' in inventory:
                        print(f"You have the saddle, and put it on {Horse_name}.")
                        Tack_temp = False
                        if 'sinch' in inventory:
                            print(f"You have the sinch, and put it on {Horse_name}.")
                            Tack_temp = False
                            if 'breast collar' in inventory:
                                print(f"You have the breast collar, and put in on {Horse_name}.")
                                Tack_temp = False
                                if 'bridle' in inventory:
                                    print(f"You have the bridle, and putit on {Horse_name}.")
                                    print(f"Good work! You successfully tacked up {Horse_name}, and are ready to ride!")
                                    Tack_temp = True
                                    inventory.append('Tacked')
                                else:
                                    print(f"Sorry, you didn't have a bridle. Go grab one and try again!")
                            else:
                                print(f"Sorry, you didn't have a breast collar. Go grab one and try again!")
                        else:
                            print(f"Sorry, you didn't have a sinch. Go grab one and try again!")
                    else:
                        print(f"Sorry, you didn't have a saddle. Go grab one and try again!")
                else:
                    print(f"Sorry, you didn't have a saddle pad. Go grab one and try again!")
            elif act_choice.upper() in ('R', 'RIDE'):
                if Tack_temp is True or Tacked_Up is True:
                    print(f"""
You are ready to ride!
Riding...
Riding...
Riding...
Great work!
""")
                    inventory.append('Rode')
                else:
                    print(f"Sorry, {Horse_name} wasn't tacked up, so you could ride.\nTack {horse_pronoun_her_him} and try again!")
            else:
                print(f"Sorry, that wasn't a valid choice. Please try again.")
        stay_ask = input("""
Do you want to stay in the arena, or leave?
S-tay
L-eave
""")
        while stay_ask.upper() in ('S', 'STAY'):
            print("OK, you are staying in the arena.")
            if Horse == False:
                print(f"Sorry, you don't have a horse to work with!\nGo catch {Horse_name} and come back!")
            elif Horse == True:
                act_choice = input(f"""
What would you like to do?
B-brush
R-ride
T-tack up
BA-bathe {Horse_name}
U-untack
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
                elif act_choice.upper() in ('BA', 'BATHE'):
                    if 'shampoo/conditioner' in inventory:
                        print(f"""
Good job, you had the shampoo and conditioner to clean {Horse_name}!
Bathing...
Bathing...
Bathing...
{Horse_name} is now freshly clean!
""")
                        inventory.append('Bathed')
                    else:
                        print("Sorry, you didn't have shampoo/conditioner to use.\nGrab some, and try again.")
                elif act_choice.upper() in ('U', 'UNTACK'):
                    if 'Tacked' in inventory:
                        print(f"Good work, you untacked {Horse_name}.")
                        inventory.remove('Tacked')
                        inventory.append('Untacked')
                    else:
                        print(f"Sorry, {Horse_name} wasn't tacked up, so you can't untack {horse_pronoun_her_him}.")
                elif act_choice.upper() in ('T', 'TACK UP'):
                    print("""
To tack up your horse to ride follow these steps:
1) Put on the saddle pad
2) Put on the saddle
3) Put on the sinch
4) Put on the breast collar
5) Put on the bridle
""")
                    if 'saddle pad' in inventory:
                        print(f"You have the saddle pad, and put it on {Horse_name}.")
                        Tack_temp = False
                        if 'saddle' in inventory:
                            print(f"You have the saddle, and put it on {Horse_name}.")
                            Tack_temp = False
                            if 'sinch' in inventory:
                                print(f"You have the sinch, and put it on {Horse_name}.")
                                Tack_temp = False
                                if 'breast collar' in inventory:
                                    print(f"You have the breast collar, and put in on {Horse_name}.")
                                    Tack_temp = False
                                    if 'bridle' in inventory:
                                        print(f"You have the bridle, and putit on {Horse_name}.")
                                        print(f"Good work! You successfully tacked up {Horse_name}, and are ready to ride!")
                                        Tack_temp = True
                                        inventory.append('Tacked')
                                    else:
                                        print(f"Sorry, you didn't have a bridle. Go grab one and try again!")
                                else:
                                    print(f"Sorry, you didn't have a breast collar. Go grab one and try again!")
                            else:
                                print(f"Sorry, you didn't have a sinch. Go grab one and try again!")
                        else:
                            print(f"Sorry, you didn't have a saddle. Go grab one and try again!")
                    else:
                        print(f"Sorry, you didn't have a saddle pad. Go grab one and try again!")
                elif act_choice.upper() in ('R', 'RIDE'):
                    if Tack_temp is True or Tacked_Up is True:
                        print(f"""
You are ready to ride!
Riding...
Riding...
Riding...
Great work!
""")
                        inventory.append('Rode')
                    else:
                        print(f"Sorry, {Horse_name} wasn't tacked up, so you could ride.\nTack {horse_pronoun_her_him} and try again!")
                else:
                    print(f"Sorry, that wasn't a valid choice. Please try again.")
            stay_ask = input("""
Do you want to stay in the arena, or leave?
S-tay
L-eave
""")
            if stay_ask.upper() in ('L', 'LEAVE'):
                print('OK, you are leaving the arena.')
        return Tack_temp
    def main(self, Horse=False, Tacked_Up=False, Brushed=False, inventory=[], Horse_name='', Horse_gender=''):
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
        if Horse_name == '':
            Horse_name = input("What is your horse's name?\n")
        if Horse_gender == '':
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

S-save game
""")
            if choice.upper() in ('B', 'BARN'):
                self.Barn(Barn_description, inventory)
            elif choice.upper() in ('P', 'PADDOCK'):
                Horse = self.Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
            elif choice.upper() in ('E', 'EXTRA STORAGE'):
                self.Extra_Storage(Extra_storage_description, inventory)
            elif choice.upper() in ('R', 'ROUND PENS'):
                self.Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him, inventory)
            elif choice.upper() in ('A', 'ARENA'):
                Tacked_Up = self.Arena(Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him, Tacked_Up)
            elif choice.upper() in ('S', 'SAVE GAME'):
                self.save(Horse, Tacked_Up, Brushed, inventory, Horse_name, Horse_gender)
        print(f"""
Now that you've caught your horse, brush {horse_pronoun_her_him} down.
""")
        while 'Brushed' not in inventory:
            choice = input("""
Where do you want to go?
A-rena
B-arn
E-xtra Storage
P-addock
R-ound Pens

S-save game
""")
            if choice.upper() in ('B', 'BARN'):
                self.Barn(Barn_description, inventory)
            elif choice.upper() in ('P', 'PADDOCK'):
                Horse = self.Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
            elif choice.upper() in ('E', 'EXTRA STORAGE'):
               self. Extra_Storage(Extra_storage_description, inventory)
            elif choice.upper() in ('R', 'ROUND PENS'):
               self.Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him, inventory)
            elif choice.upper() in ('A', 'ARENA'):
                Tacked_Up = self.Arena(Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him, Tacked_Up)
            elif choice.upper() in ('S', 'SAVE GAME'):
                self.save(Horse, Tacked_Up, Brushed, inventory, Horse_name, Horse_gender)
        print(f"""
Now that you have brushed off {Horse_name}, warm {horse_pronoun_her_him} up!
Hint - Free lunge {horse_pronoun_her_him}
""")
        while 'Lunged' not in inventory:
            choice = input("""
Where do you want to go?
A-rena
B-arn
E-xtra Storage
P-addock
R-ound Pens

S-save game
""")
            if choice.upper() in ('B', 'BARN'):
                self.Barn(Barn_description, inventory)
            elif choice.upper() in ('P', 'PADDOCK'):
                Horse = self.Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
            elif choice.upper() in ('E', 'EXTRA STORAGE'):
                self.Extra_Storage(Extra_storage_description, inventory)
            elif choice.upper() in ('R', 'ROUND PENS'):
                self.Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him, inventory)
            elif choice.upper() in ('A', 'ARENA'):
                Tacked_Up = self.Arena(Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him, Tacked_Up)
            elif choice.upper() in ('S', 'SAVE GAME'):
                self.save(Horse, Tacked_Up, Brushed, inventory, Horse_name, Horse_gender)
        print(f"""
Now that you have warmed up {Horse_name}, 
get {horse_pronoun_her_him} tacked up and ready to ride!
""")
        while 'Tacked' not in inventory:
            choice = input("""
Where do you want to go?
A-rena
B-arn
E-xtra Storage
P-addock
R-ound Pens

S-save game
""")
            if choice.upper() in ('B', 'BARN'):
                self.Barn(Barn_description, inventory)
            elif choice.upper() in ('P', 'PADDOCK'):
                Horse = self.Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
            elif choice.upper() in ('E', 'EXTRA STORAGE'):
                self.Extra_Storage(Extra_storage_description, inventory)
            elif choice.upper() in ('R', 'ROUND PENS'):
                self.Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him, inventory)
            elif choice.upper() in ('A', 'ARENA'):
                Tacked_Up = self.Arena(Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him, Tacked_Up)
            elif choice.upper() in ('S', 'SAVE GAME'):
                self.save(Horse, Tacked_Up, Brushed, inventory, Horse_name, Horse_gender)
        print(f"""
Now that you tacked up {Horse_name} and she's ready to ride,
grab an obstacle to practice an event with!
""")
        while 'obstacle' not in inventory:
            choice = input("""
Where do you want to go?
A-rena
B-arn
E-xtra Storage
P-addock
R-ound Pens

S-save game
""")
            if choice.upper() in ('B', 'BARN'):
                self.Barn(Barn_description, inventory)
            elif choice.upper() in ('P', 'PADDOCK'):
                Horse = self.Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
            elif choice.upper() in ('E', 'EXTRA STORAGE'):
                self.Extra_Storage(Extra_storage_description, inventory)
            elif choice.upper() in ('R', 'ROUND PENS'):
                self.Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him, inventory)
            elif choice.upper() in ('A', 'ARENA'):
                Tacked_Up = self.Arena(Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him, Tacked_Up)
            elif choice.upper() in ('S', 'SAVE GAME'):
                self.save(Horse, Tacked_Up, Brushed, inventory, Horse_name, Horse_gender)
        print(f"""
Now that you've chosen your event to work on, go ride!
""")
        while 'Rode' not in inventory:
            choice = input("""
Where do you want to go?
A-rena
B-arn
E-xtra Storage
P-addock
R-ound Pens

S-save game
""")
            if choice.upper() in ('B', 'BARN'):
                self.Barn(Barn_description, inventory)
            elif choice.upper() in ('P', 'PADDOCK'):
                Horse = self.Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
            elif choice.upper() in ('E', 'EXTRA STORAGE'):
                self.Extra_Storage(Extra_storage_description, inventory)
            elif choice.upper() in ('R', 'ROUND PENS'):
                self.Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him, inventory)
            elif choice.upper() in ('A', 'ARENA'):
                Tacked_Up = self.Arena(Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him, Tacked_Up)
            elif choice.upper() in ('S', 'SAVE GAME'):
                self.save(Horse, Tacked_Up, Brushed, inventory, Horse_name, Horse_gender)
        print(f"""
Now that you are done riding {Horse_name}, untack {horse_pronoun_her_him}.
""")
        while 'Untacked' not in inventory:
            choice = input("""
Where do you want to go?
A-rena
B-arn
E-xtra Storage
P-addock
R-ound Pens

S-save game
""")
            if choice.upper() in ('B', 'BARN'):
                self.Barn(Barn_description, inventory)
            elif choice.upper() in ('P', 'PADDOCK'):
                Horse = self.Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
            elif choice.upper() in ('E', 'EXTRA STORAGE'):
                self.Extra_Storage(Extra_storage_description, inventory)
            elif choice.upper() in ('R', 'ROUND PENS'):
                self.Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him, inventory)
            elif choice.upper() in ('A', 'ARENA'):
                Tacked_Up = self.Arena(Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him, Tacked_Up)
            elif choice.upper() in ('S', 'SAVE GAME'):
                self.save(Horse, Tacked_Up, Brushed, inventory, Horse_name, Horse_gender)
        print(f"""
Now that you've untacked {Horse_name}, get {horse_pronoun_her_him} a treat.
""")
        while 'treats' not in inventory:
            choice = input("""
Where do you want to go?
A-rena
B-arn
E-xtra Storage
P-addock
R-ound Pens

S-save game
""")
            if choice.upper() in ('B', 'BARN'):
                self.Barn(Barn_description, inventory)
            elif choice.upper() in ('P', 'PADDOCK'):
                Horse = self.Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
            elif choice.upper() in ('E', 'EXTRA STORAGE'):
                self.Extra_Storage(Extra_storage_description, inventory)
            elif choice.upper() in ('R', 'ROUND PENS'):
                self.Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him, inventory)
            elif choice.upper() in ('A', 'ARENA'):
                Tacked_Up = self.Arena(Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him, Tacked_Up)
            elif choice.upper() in ('S', 'SAVE GAME'):
                self.save(Horse, Tacked_Up, Brushed, inventory, Horse_name, Horse_gender)
        print(f"""
Now that you've rewarded {Horse_name} and given {horse_pronoun_her_him} a treat,
give {horse_pronoun_her_him} a bath!
""")
        while 'Bathed' not in inventory:
            choice = input("""
Where do you want to go?
A-rena
B-arn
E-xtra Storage
P-addock
R-ound Pens

S-save game
""")
            if choice.upper() in ('B', 'BARN'):
                self.Barn(Barn_description, inventory)
            elif choice.upper() in ('P', 'PADDOCK'):
                Horse = self.Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
            elif choice.upper() in ('E', 'EXTRA STORAGE'):
                self.Extra_Storage(Extra_storage_description, inventory)
            elif choice.upper() in ('R', 'ROUND PENS'):
                self.Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him, inventory)
            elif choice.upper() in ('A', 'ARENA'):
                Tacked_Up = self.Arena(Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him, Tacked_Up)
            elif choice.upper() in ('S', 'SAVE GAME'):
                self.save(Horse, Tacked_Up, Brushed, inventory, Horse_name, Horse_gender)
        print(f"""
Now that {Horse_name} is clean, release {horse_pronoun_her_him} into the paddock for the night.
""")
        while Horse is True:
            choice = input("""
Where do you want to go?
A-rena
B-arn
E-xtra Storage
P-addock
R-ound Pens

S-save game
""")
            if choice.upper() in ('B', 'BARN'):
                self.Barn(Barn_description, inventory)
            elif choice.upper() in ('P', 'PADDOCK'):
                Horse = self.Paddock(Paddock_description, inventory, Horse, Horse_name, horse_pronoun_her_him)
            elif choice.upper() in ('E', 'EXTRA STORAGE'):
                self.Extra_Storage(Extra_storage_description, inventory)
            elif choice.upper() in ('R', 'ROUND PENS'):
                self.Round_Pens(Round_Pen_description, Horse, Horse_name, horse_pronoun_her_him, inventory)
            elif choice.upper() in ('A', 'ARENA'):
                Tacked_Up = self.Arena(Arena_description, inventory, Horse, Horse_name, horse_pronoun_her_him, Tacked_Up)
            elif choice.upper() in ('S', 'SAVE GAME'):
                self.save(Horse, Tacked_Up, Brushed, inventory, Horse_name, Horse_gender)
        print("Congratulations! You finished the game!")
def load():
        try:
            with open('Horse.pickle', 'rb') as f:
                Horse = pickle.load(f)
            with open('Tacked_Up.pickle', 'rb') as f:
                Tacked_Up = pickle.load(f)
            with open('Brushed.pickle', 'rb') as f:
                Brushed = pickle.load(f)
            with open('inventory.pickle', 'rb') as f:
                inventory = pickle.load(f)
            with open('Horse_name', 'rb') as f:
                Horse_name = pickle.load(f)
            with open('Horse_gender', 'rb') as f:
                Horse_gender = pickle.load(f)
            state_dictionary = {
                'Horse': Horse,
                'Tacked_Up': Tacked_Up,
                'Brushed': Brushed,
                'inventory': list(inventory),
                'Horse_name': Horse_name,
                'Horse_gender': Horse_gender
            }
            return state_dictionary

        except FileNotFoundError:
            print ("Game file not found")
# play = Play()