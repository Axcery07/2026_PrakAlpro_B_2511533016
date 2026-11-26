schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

busiest = max(schedule, key=lambda day: len(schedule[day]))
print(f"Busiest day: {busiest} ({len(schedule[busiest])} courses)")

course = input("Course name: ")
count = 0
for day, courses in schedule.items():
    if course in courses:
        count += 1
print(f"{course}: {count} days")