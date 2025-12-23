with open("workout_log.txt", "w") as file:
    file.write("""Sarah,Yoga,60,0
 Mike,Crossfit,40,55
 Emily,Running,90,10
 David,Yoga,45,15
 Invalid,Entry,No,Numbers
 Chris,Crossfit,50,50
 Anna,Running,30,0""")
def process_fitness_data(filename):
    my_dict = {}
    iron_athletes = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            name = parts[0]
            activity = parts[1]
            cardio_str = parts[2]
            strength_str = parts[3]
            try:
                    cardio_str = int(cardio_str)
                    strength_str = int(strength_str) 
                    total_minutes = cardio_str + strength_str
                    if activity not in my_dict:
                        my_dict[activity] = 0
                    my_dict[activity] += total_minutes
                    if total_minutes > 90:
                        iron_athletes.append((name,total_minutes))
            except ValueError:
                    continue 
        return my_dict, iron_athletes
def fitness_report(my_dict, iron_athletes):
     with open("fitness_report.txt", "w") as file:
          file.write("ACTIVITY TYPE TOTALS (Minutes)\n")
          file.write("------------------------------\n")
          for activity, time in my_dict.items():
               file.write(f"{activity}: {time}\n")
          file.write("IRON ATHLETES (> 90 mins)\n")
          file.write("-------------------------\n")
          for name, minutes in iron_athletes:
               file.write(f"{name} ({minutes} mins)\n")
activity_totals, iron_athletes = process_fitness_data("workout_log.txt")
fitness_report(activity_totals, iron_athletes)