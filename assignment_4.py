# Assignment 4: Swords and Spears Problem
import sys

def validate_the_parameters():
    flag = True
  
    all_binary_weapons = all(binary in '01' for binary in weapons_stack)
    all_binary_soldiers = all(binary in '01' for binary in soldiers_queue)
    if not all_binary_weapons:
       print "Weapons stack should contain 0 and 1"
       flag=False
    if not all_binary_soldiers:
       print "Soldiers queue stack should contain 0 and 1"
       flag=False
    if total_soldiers <= 0:
        print("Invalid number or soldiers length")
        flag = False
    if total_soldiers != len(weapons_stack):
        print("Invalid input for weapon")
        flag = False
    if total_soldiers != len(soldiers_queue):
        print("Invalid input for soldiers")
        flag = False
    return flag

def count_soldiers_who_gets_weapon(total_soldiers, weapons_stack, soldiers_queue):
    weapons_stack = list(weapons_stack)
    soldiers_queue = list(soldiers_queue)
    
    cnt = 1
    n = len(weapons_stack)
    while n*n >= cnt:
 	if cnt == n*n:
             break	        
        if weapons_stack or soldiers_queue:
            if weapons_stack[0] == soldiers_queue[0]:
	        del weapons_stack[0]
	        del soldiers_queue[0]
	    else:
	        soldiers_queue.append(soldiers_queue[0])
	        del soldiers_queue[0]
        else:
            break
        cnt += 1

    return len(soldiers_queue)


# Driver code
if __name__ == "__main__":
    total_soldiers = int(raw_input("Number of soldiers and weapons: "))
    weapons_stack =  raw_input("Enter weapons stack: ")
    soldiers_queue = raw_input("Enter soldiers queue: ")
    remaining_soldiers = count_soldiers_who_gets_weapon(total_soldiers, weapons_stack, soldiers_queue)
    if not validate_the_parameters():
       sys.exit(1)

    if remaining_soldiers == total_soldiers:
        print "{0} (None of the soldiers get the weapon)".format(remaining_soldiers)
    elif not remaining_soldiers:
        print "{0} (every one should get the weapon)".format(remaining_soldiers) 
    else:
        print "{0} ({0} soldier won't get the weapon)".format(remaining_soldiers)
