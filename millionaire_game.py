import streamlit as st

# Questions and answers
questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 'c'],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 'b'],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 'c'],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 'b'],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 'a'],
    ["What is the square root of 64?", "8", "10", "6", "12", 'a'],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 'c'],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 'c'],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 'c'],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 'b'],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 'b']
]

prizes = [100000, 320000, 400000, 450000, 500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]

# Initialize session state
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.end = False

st.set_page_config(page_title="Millionaire Game", layout="centered")
st.title(" Who Wants to Be a Millionaire?")

# End screen
if st.session_state.end or st.session_state.index >= len(questions):
    st.subheader(" Game Over!")
    st.write(f" You won: ₹ {st.session_state.score:,}")
    if st.button(" Play Again"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.end = False
    st.stop()

# Current question
q = questions[st.session_state.index]
st.subheader(f"Question {st.session_state.index + 1}: {q[0]}")

# Option selector
selected = st.radio("Choose your answer:", ['a', 'b', 'c', 'd'], format_func=lambda x: {
    'a': f"a. {q[1]}",
    'b': f"b. {q[2]}",
    'c': f"c. {q[3]}",
    'd': f"d. {q[4]}"
}[x], key=f"question_{st.session_state.index}")

# Submit button
if st.button("Submit"):
    correct = q[5]
    if selected == correct:
        st.success(" Correct Answer!")
        st.session_state.score = prizes[st.session_state.index]
        st.session_state.index += 1
        st.rerun()  # Rerun to show next question immediately
    else:
        st.error(f"Incorrect! The correct answer was '{correct}'")
        st.session_state.end = True
        st.rerun()
