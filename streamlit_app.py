import streamlit as st
import random
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Rüdi Leaks", layout="wide")

# Sidebar - Rüdigers Profil
st.sidebar.title("🕵️‍♂️ Rüdi Leaks")
st.sidebar.image("rüdi.jpg", width=150)  # Bild rüdi.jpg aus demselben Ordner laden
st.sidebar.write("Willkommen bei **Rüdi Leaks**, wo Geheimnisse enthüllt werden 👀!")
st.sidebar.markdown("---")

# Sidebar Filter
st.sidebar.subheader("Wähle den Chat zum Leaken")
chats = ["Chat mit Rille", "Chat mit Sven"]
selected_chat = st.sidebar.selectbox("Wähle einen Chat", chats)


# Mock Chat Daten-Generator mit Abwechslung
def generate_mock_chat(selected_chat):
    mock_chat_data = []
    chat_messages = {
        "Chat mit Rille": [
            ["Rille", "Gerade in Bali gelandet! Das Wetter ist perfekt 🌞"],
            ["Rüdi", "Nice! Wie ist die Villa?"],
            ["Rille", "Hab eine für 50$ pro Nacht gefunden! Remote Life ist genial."],
            ["Rüdi", "Gehst du als nächstes nach Südamerika?"],
            ["Rille", "Vielleicht! Hab diesen Monat 5k gemacht, läuft super!"],
            ["Rüdi", "Das remote Leben scheint dir echt zu liegen!"],
            ["Rille", "Total! Nächster Trip ist schon in Planung."],
            ["Rüdi", "Ich sollte echt mal mit dir mitkommen."],
            [
                "Rille",
                "Mach mal Sven einen Streich und sag ihm, dass ich auch in Athen bin 😆",
            ],
            ["Rüdi", "Haha, der glaubt's sicher! Ich schreib ihm gleich."],
        ],
        "Chat mit Sven": [
            ["Sven", "Hab gestern ein Match mit einer Schwedin - totale 10!"],
            ["Rüdi", "Haha, noch eins? Du bist echt am Start!"],
            ["Sven", "Bin auf dem Weg zu einem Date mit einem italienischen Model 👀"],
            ["Rüdi", "Lass das Sternzeichen-Thema diesmal weg 😂"],
            ["Sven", "Guter Tipp! Die letzte war besessen von Sternzeichen!"],
            ["Rüdi", "Irgendwelche wilden Tinder-Stories?"],
            ["Sven", "Eine Menge! Gestern mit einer Französin gematcht."],
            ["Rüdi", "Muss mir echt Notizen von dir machen!"],
            ["Sven", "Dating-Leben ist ganz nett, sagen wir mal so."],
            ["Rüdi", "Halt uns über die Stories auf dem Laufenden!"],
        ],
    }

    selected_messages = random.sample(
        chat_messages[selected_chat], k=len(chat_messages[selected_chat])
    )  # Zufällige Reihenfolge, um Dopplungen zu vermeiden

    for message_pair in selected_messages:
        friend, message = message_pair
        time = datetime.now() - timedelta(
            hours=random.randint(0, 24), minutes=random.randint(0, 59)
        )
        mock_chat_data.append(
            {
                "time": time.strftime("%Y-%m-%d %H:%M:%S"),
                "friend": friend,
                "message": message,
            }
        )

    return mock_chat_data


# Hauptlayout - Header
st.title("💬 Rüdi Leaks: Das ultimative Geheimnis-Hub")
st.write(
    "Willkommen bei Rüdi Leaks - hier gibt es die saftigsten Chat-Leaks. Viel Spaß beim Durchstöbern! 😄"
)
st.markdown("---")

# Anzeigen der Chat-Daten
chat_data = generate_mock_chat(selected_chat)
for entry in chat_data:
    st.write(f"**[{entry['time']}]** {entry['friend']}: {entry['message']}")
