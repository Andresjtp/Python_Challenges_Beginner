data = ["10", "5", "abc", None, "20"]
cleaned_data = []

for item in data:
    try:
        cleaned_data.append(int(item))
    except ValueError:
        print(f"ValueError: Cannot convert '{item}' to integer - not a valid number")
    except TypeError:
        print(f"TypeError: Cannot convert {item} to integer - not a string")

print(f"\nCleaned data: {cleaned_data}")

    
   