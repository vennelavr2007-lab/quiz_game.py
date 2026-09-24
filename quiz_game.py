score = 0
q = {
    "Capital of India? ": "delhi",
    "Days in a week? ": "7",
    "Programming language? ": "python",
    "5 + 5 = ? ": "10",
    "Largest planet? ": "jupiter"
}
for question, answer in q.items():
    if input(question).lower() == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print("Your score:", score, "/ 5")

OUTPUT:
Capital of India? amaravathi
Wrong!
Days in a week? 7
Correct!
Programming language? python
Correct!
5 + 5 = ? 10
Correct!
Largest planet? earth
Wrong!
Your score: 3 / 5
