prompt= "\nEnter the name of a city you visited"
prompt+= "\n(Enter quit to quit)"



while True:
    city= input(prompt)
    if city == 'quit':
        break
    else:
        
        print("id like to go to " + city.title() + "!")