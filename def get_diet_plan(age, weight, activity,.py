def get_diet_plan(age, weight, activity, goal, preference):
    # Estimate calorie needs
    if goal == "weight loss":
        calories = 1500 if activity == "low" else 1800
    elif goal == "muscle gain":
        calories = 2500 if activity == "high" else 2200
    else:
        calories = 2000

    # Sample food choices
    if preference == "vegetarian":
        breakfast = "Oats with banana and almond milk"
        lunch = "Vegetable curry with brown rice"
        snack = "Fruit salad and almonds"
        dinner = "Lentil soup with whole grain bread"
    elif preference == "non-vegetarian":
        breakfast = "Eggs and toast"
        lunch = "Grilled chicken with quinoa"
        snack = "Greek yogurt with honey"
        dinner = "Fish curry with vegetables"
    else:  # vegan
        breakfast = "Smoothie with oats and plant-based milk"
        lunch = "Chickpeas with quinoa and salad"
        snack = "Hummus and carrot sticks"
        dinner = "Tofu stir fry with brown rice"

    # Build plan
    plan = {
        "Estimated Calories": calories,
        "Breakfast": breakfast,
        "Lunch": lunch,
        "Snack": snack,
        "Dinner": dinner
    }
    return plan


# User Input
print("Personalized Diet Recommendation System\n")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
activity = input("Activity level (low / moderate / high): ").strip().lower()
goal = input("Health goal (weight loss / maintain / muscle gain): ").strip().lower()
preference = input("Diet preference (vegetarian / non-vegetarian / vegan): ").strip().lower()

# Get diet plan
diet_plan = get_diet_plan(age, weight, activity, goal, preference)

# Show output
print("\nYour Personalized Diet Plan:")
for key, value in diet_plan.items():
    print(f"{key}: {value}")
