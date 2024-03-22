import requests
import tkinter as tk
import json

def fetch_data():
    url = "https://vision.foodvisor.io/api/1.0/en/analysis/"
    headers = {"Authorization": "Api-Key TAHsFDAB.WJAqMmGPggyhMdgTTWlSLHANKYcncd3Q"}
    with open("01.jpg", "rb") as image:
        response = requests.post(url, headers=headers, files={"image": image})
        response.raise_for_status()
    data = response.json()

    text_box.insert('1.0', "The prediction will be from least probable to most probable\n")
    
    foods = data['items'][0]['food']

    for food in foods:
        food_info = food['food_info']
        display_name = food_info['display_name']
        quantity = food['quantity']
        nutrition = food_info['nutrition']
        ingredients = food['ingredients']
        g_per_serving = food_info['g_per_serving']

        text_box.insert('1.0', f"Display Name: {display_name}\n")
        text_box.insert('1.0', f"Quantity: {quantity} servings\n")
        text_box.insert('1.0', f"Nutrition: {nutrition}\n")
        text_box.insert('1.0', f"Ingredients: {ingredients}\n")
        text_box.insert('1.0', f"Grams per Serving: {g_per_serving}\n")
        text_box.insert('1.0', "-----------------------------------------------------\n")

       
root = tk.Tk()

text_box = tk.Text(root, font=("Helvetica", 16, "bold"))
text_box.pack()

button = tk.Button(root, text='fetch data', command=fetch_data)
button.pack()

root.mainloop()