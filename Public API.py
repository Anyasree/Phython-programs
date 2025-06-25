import requests

url = "https://uselessfacts.jsph.pl/random.json?language=en"
while True:
    response = requests.get(url)
    answer = input("Press enter to get a random fact, or type 'q' to quit...")
    if answer.lower() == "q":
        break
    if response.status_code == 200:
        fact_data = response.json()
        print(fact_data['text'])

    else:
        print("Failed to retrieve fact")
    
