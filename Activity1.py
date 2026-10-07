total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores in today's list")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1:
        next_chore = "Make your bed."
    elif chore_num == 2:
        next_chore = "Pack your bag."
    elif chore_num == 3:
        next_chore = "Clean your studytable."
    else:
        next_chore = "Wash your cycle."

    chore_completed = input(f"Have you finished your {next_chore} (yes/no)")
    if chore_completed == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job chores completed")
    else:
        print("Ok finish it and check it again.")
    print(f"Chores remaining are {original_count - completed_count}")
print("=====ALL CHORES COMPLETE! =====")
print("Great work finishing your entire checklist today!\n")

print("Now let's safely peek at an infinite loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 10:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break

print("\n===== CHORES CHECKLIST SUMMARY =====")
print("Chores Assigned Today: ", original_count)
print("Chored Completed: ", completed_count)
print("Chores Remining: ", total_chores - completed_count)
print("======================================")