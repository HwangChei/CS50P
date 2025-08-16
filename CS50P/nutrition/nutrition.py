def main():
    calories=input("Item:")
    if calories.lower() in ['apple']:
        print("Calories: 130")
    elif calories.lower() in ['avocado','cantaloupe','honeydew melon','pineapple','strawberries','tangirine']:
        print("Calories: 50")
    elif calories.lower() in ['banana']:
        print("Calories: 110")
    elif calories.lower() in ['grapefruit','nectarine','peach']:
        print("Calories: 60")
    elif calories.lower() in ['lemon']:
        print("Calories: 15")
    elif calories.lower() in ['grapes','kiwifruit']:
        print("Calories: 90")
    elif calories.lower() in ['lime']:
        print("Calories: 20")
    elif calories.lower() in ['plums']:
        print("Calories: 70")
    elif calories.lower() in ['pear','sweet cherries']:
        print("Calories: 100")
    elif calories.lower() in ['watermelon']:
        print("Calories: 80")
    
main()

