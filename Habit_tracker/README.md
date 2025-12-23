# 📅 Daily Habit Tracker

## Challenge Overview

This challenge focuses on building a habit tracking system using Python's classes, lists, dictionaries, and loops to help users monitor their daily habits and maintain streaks.

**Skills Used:**
- Classes
- Lists
- Dictionaries
- Loops
- Data tracking

---

## Structure

### Class: `Habit`
Represents an individual habit with two attributes:
- `name` - Name of the habit (e.g., "Exercise", "Read")
- `completed_days` - List of days (integers) when the habit was completed

### Class: `HabitTracker`
Manages multiple habits using a list:
- `habits` - List containing all `Habit` objects

---

## Features Implementation

### 1. **Add Habit**
```python
def add_habit(self, habit):
    self.habits.append(habit)
    print(f"Added habit: {habit.name}")
```
**How it works:**
- Accepts a `Habit` object as a parameter
- Appends the habit to the tracker's list
- Provides user feedback confirming the addition
- Each habit starts with an empty `completed_days` list

**Example:**
```python
tracker = HabitTracker()
exercise = Habit("Exercise")
tracker.add_habit(exercise)
# Output: Added habit: Exercise
```

---

### 2. **Mark Habit as Completed for a Day**
```python
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
```
**How it works:**
- Searches for the habit by name (case-insensitive)
- Checks if the day is already marked to prevent duplicates
- Appends the day number to the habit's `completed_days` list
- Provides feedback for success, duplicate, or not found scenarios
- Uses `return` to exit after finding and processing the habit

**Key concepts:**
- **Case-insensitive search**: `.lower()` allows flexible name matching
- **Duplicate prevention**: Checks `if day not in habit.completed_days`
- **Early return pattern**: Exits loop after finding the target habit
- **User feedback**: Clear messages for all outcomes

**Example:**
```python
tracker.mark_completed("Exercise", 1)
# Output: Marked 'Exercise' as completed for day 1

tracker.mark_completed("Exercise", 1)
# Output: 'Exercise' already marked for day 1
```

---

### 3. **Show Streak Count**
```python
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
```
**How it works:**
- Searches for the habit by name
- Handles edge case of no completed days
- **Sorts the completed days** to ensure chronological order
- Iterates through sorted days to find consecutive sequences
- Compares each day with the previous day:
  - If `current_day == previous_day + 1`: consecutive (increment streak)
  - Otherwise: streak broken (reset counter)
- Tracks both current streak and maximum streak
- Displays the longest streak found

**Key concepts:**
- **Sorting**: `sorted(habit.completed_days)` ensures chronological analysis
- **Consecutive detection**: Checks if `sorted_days[i] == sorted_days[i-1] + 1`
- **Streak algorithm**: 
  - Increment `current_streak` for consecutive days
  - Reset to 1 when streak breaks
  - Track `max_streak` to find longest sequence
- **Loop indexing**: Starts at index 1 to compare with previous element

**Streak calculation logic:**
```
Days: [1, 2, 3, 5, 6, 7, 8]
       -------     ---------
       streak=3    streak=4  → max_streak = 4
```

**Example:**
```python
tracker.mark_completed("Exercise", 1)
tracker.mark_completed("Exercise", 2)
tracker.mark_completed("Exercise", 3)
tracker.show_streak("Exercise")
# Output: 'Exercise' - Current streak: 3 days

tracker.mark_completed("Exercise", 5)  # Day 4 skipped
tracker.show_streak("Exercise")
# Output: 'Exercise' - Current streak: 3 days (longest consecutive)
```

---

### 4. **Show All Habits & Progress**
```python
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
```
**How it works:**
- Checks if the tracker has any habits
- Iterates through all habits in the list
- For each habit:
  - Calculates total days completed using `len()`
  - Sorts and displays the list of completed days
  - Handles habits with no completed days
- Formats output with clear sections and indentation

**Key concepts:**
- **Empty check**: Validates list before processing
- **List length**: `len(habit.completed_days)` for count
- **Conditional display**: Different output for habits with/without progress
- **Sorting**: Displays days in chronological order
- **Formatted output**: Uses indentation and sections for readability

**Example:**
```python
tracker.show_all_habits()
# Output:
# === All Habits & Progress ===
# 
# Exercise:
#   Days completed: 4
#   Completed on days: [1, 2, 3, 5]
# 
# Read:
#   Days completed: 2
#   Completed on days: [1, 3]
# ============================
```

---

## Key Concepts Demonstrated

### 1. **Object-Oriented Design**
- **Encapsulation**: Habit data bundled in `Habit` class
- **Composition**: `HabitTracker` manages a collection of `Habit` objects
- **Single Responsibility**: Each class has a clear purpose

### 2. **List Operations**
```python
# Append
habit.completed_days.append(day)

# Check membership
if day not in habit.completed_days:

# Length
days_completed = len(habit.completed_days)

# Sorting
sorted_days = sorted(habit.completed_days)
```

### 3. **Streak Algorithm**
- Sorting for chronological order
- Comparing consecutive elements
- Tracking current and maximum values
- Resetting counters when patterns break

### 4. **Search and Validation**
- Case-insensitive searching
- Duplicate prevention
- Edge case handling (empty lists)
- User-friendly error messages

### 5. **Loop Patterns**
```python
# Search pattern
for habit in self.habits:
    if condition:
        # Process
        return

# Comparison pattern
for i in range(1, len(list)):
    if list[i] relates_to list[i-1]:
        # Process relationship
```

---

## Complete Usage Example

```python
# Create tracker
tracker = HabitTracker()

# Add habits
tracker.add_habit(Habit("Exercise"))
tracker.add_habit(Habit("Read"))
tracker.add_habit(Habit("Meditate"))

# Mark completed days for Exercise
tracker.mark_completed("Exercise", 1)
tracker.mark_completed("Exercise", 2)
tracker.mark_completed("Exercise", 3)
tracker.mark_completed("Exercise", 5)
tracker.mark_completed("Exercise", 6)

# Mark completed days for Read
tracker.mark_completed("Read", 1)
tracker.mark_completed("Read", 3)
tracker.mark_completed("Read", 4)

# Show streak for Exercise
tracker.show_streak("Exercise")
# Output: 'Exercise' - Current streak: 3 days (days 1-3)

# Show streak for Read
tracker.show_streak("Read")
# Output: 'Read' - Current streak: 2 days (days 3-4)

# Display all habits and progress
tracker.show_all_habits()
# Shows comprehensive view of all habits
```

---

## Data Structure Visualization

```python
# HabitTracker structure:
habits = [
    Habit("Exercise", completed_days=[1, 2, 3, 5, 6]),
    Habit("Read", completed_days=[1, 3, 4]),
    Habit("Meditate", completed_days=[])
]

# Each Habit object contains:
# - name: string
# - completed_days: list of integers representing day numbers
```

---

## Algorithm Breakdown: Streak Calculation

```python
# Example: completed_days = [3, 1, 5, 2, 6]

# Step 1: Sort
sorted_days = [1, 2, 3, 5, 6]

# Step 2: Iterate and compare
# i=1: days[1]=2, days[0]=1 → 2==1+1? Yes → current=2, max=2
# i=2: days[2]=3, days[1]=2 → 3==2+1? Yes → current=3, max=3
# i=3: days[3]=5, days[2]=3 → 5==3+1? No  → current=1, max=3
# i=4: days[4]=6, days[3]=5 → 6==5+1? Yes → current=2, max=3

# Result: max_streak = 3 (days 1, 2, 3)
```

---

## Potential Enhancements

- Add date/timestamp support (instead of just day numbers)
- Calculate current ongoing streak vs. best streak
- Add habit deletion functionality
- Implement habit categories/tags
- Add weekly/monthly summaries
- Track habit completion percentage
- Set and track habit goals (e.g., "30 days straight")
- Add reminders or notifications
- Visualize streaks with charts
- Export progress to file (JSON/CSV)
- Add habit descriptions or notes
- Calculate total habits completed per day
- Add motivational messages for milestones
- Implement habit prioritization
- Track time of completion for each day
