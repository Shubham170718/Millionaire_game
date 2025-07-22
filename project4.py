# millionaire game
questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 'c'],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 'b'],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 'c'],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 'b'],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", "b"],
    ["What is the square root of 64?", "8", "10", "6", "12", 'a'],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 'c'],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 'c'],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 'c'],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 'b'],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 'b']
]

prizes = [100000, 320000, 400000, 450000,  500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]

i = 0 
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # Check whether the answer is correct or not
    a = input("Enter your answer.  a,  b,  c,  d\n")
    if(question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break 
    print(f"You won {prizes[i]}")
    i +=1    