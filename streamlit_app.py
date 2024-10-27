import streamlit as st
import random
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Rüdi Leaks", layout="wide")

# Sidebar - Rüdiger's Profile
st.sidebar.title("🕵️‍♂️ Rüdi Leaks")
st.sidebar.image("rüdi.jpg", width=150)  # Load rüdi.jpg from the same folder
st.sidebar.write("Welcome to **Rüdi Leaks**, where secrets are revealed 👀!")
st.sidebar.markdown("---")

# Sidebar Filters
st.sidebar.subheader("Choose Chat to Leak")
chats = ["Chat with Rille", "Chat with Sven"]
selected_chat = st.sidebar.selectbox("Choose a chat to view", chats)


# Mock Chat Data Generator
def generate_mock_chat(selected_chat):
    mock_chat_data = []
    messages = {
        "Chat with Rille": [
            "Rille: Just landed in Bali! The weather's perfect 🌞",
            "Rüdi: Nice! How’s the villa?",
            "Rille: Got it for $50 a night! Remote life is awesome.",
            "Rüdi: Any plans for South America next?",
            "Rille: Maybe! Made $5k this month, feeling great!",
        ],
        "Chat with Sven": [
            "Sven: Matched with a Swedish girl yesterday - total 10!",
            "Rüdi: Dude, you’re on fire with these matches 😂",
            "Sven: Off to a date with an Italian model now 👀",
            "Rüdi: Just don’t bring up astrology this time!",
            "Sven: Haha, I’ll try! Got another wild Tinder story.",
        ],
    }

    for _ in range(10):  # Generate 10 mock messages
        time = datetime.now() - timedelta(
            hours=random.randint(0, 24), minutes=random.randint(0, 59)
        )
        message = random.choice(messages[selected_chat])
        mock_chat_data.append(
            {"time": time.strftime("%Y-%m-%d %H:%M:%S"), "message": message}
        )
    return mock_chat_data


# Main Layout - Header
st.title("💬 Rüdi Leaks: The Ultimate Chat Secrets Hub")
st.write(
    "Welcome to Rüdi Leaks - where the juiciest chats are just a click away. Enjoy responsibly! 😄"
)
st.markdown("---")

# Display Chat Data
chat_data = generate_mock_chat(selected_chat)
for entry in chat_data:
    st.write(f"**[{entry['time']}]** {entry['message']}")
