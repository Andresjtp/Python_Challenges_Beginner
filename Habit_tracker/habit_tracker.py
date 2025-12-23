class Habit:
    def __init__(self, name):
        self.name = name
        self.completed_days = []


class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)
        print(f"Added habit: {habit.name}")

    def mark_completed(self, habit_name, day):
        for habit in self.habits:
            if habit_name.lower() == habit.name.lower():
                if day not in habit.completed_days:
                    habit.completed_days.append(day)
                    print(f"Marked '{habit.name}' as completed for day {day}")
                else:
                    print(f"'{habit.name}' already marked for day {day}")
                return
        print(f"Habit '{habit_name}' not found")

    def show_streak(self, habit_name):
        for habit in self.habits:
            if habit_name.lower() == habit.name.lower():
                if not habit.completed_days:
                    print(f"'{habit.name}' - No days completed yet. Streak: 0")
                    return

                # Sort days to calculate streak
                sorted_days = sorted(habit.completed_days)
                current_streak = 1
                max_streak = 1

                for i in range(1, len(sorted_days)):
                    if sorted_days[i] == sorted_days[i - 1] + 1:
                        current_streak += 1
                        max_streak = max(max_streak, current_streak)
                    else:
                        current_streak = 1

                print(f"'{habit.name}' - Current streak: {max_streak} days")
                return
        print(f"Habit '{habit_name}' not found")

    def show_all_habits(self):
        if not self.habits:
            print("No habits tracked yet.")
            return

        print("\n=== All Habits & Progress ===")
        for habit in self.habits:
            days_completed = len(habit.completed_days)
            if habit.completed_days:
                days_list = sorted(habit.completed_days)
                print(f"\n{habit.name}:")
                print(f"  Days completed: {days_completed}")
                print(f"  Completed on days: {days_list}")
            else:
                print(f"\n{habit.name}:")
                print("  Days completed: 0")
                print("  No days completed yet")
        print("============================\n")
