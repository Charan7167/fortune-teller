def get_fortune(mood):
    if mood == "happy":
    	return "✨ Your fortune: Joy radiates from within you, spreading light wherever you go. Bask in it, Charan, and keep shining bright! ✨"
    elif mood == "sad":
    	return "🌧️ Your fortune: Even the stormiest skies clear with time. Hold on tight, Charan-the rainbow is closer than you think. 🌈"
    elif mood == "neutral":
    	return "😐 Your fortune: Life flows steadily, Charan. Embrace the calm—it’s the perfect moment to plant seeds for future triumphs. 🌿"
    elif mood == "excited":
        return "🎉 Your enthusiasm is contagious! Dive headfirst, Charan—the universe is ready for your energy. 🌟"
    elif mood == "stressed":
        return "🧘‍♂️Take a deep breath, alaji. You’re stronger than you realize, and this pressure will shape you into brilliance. 🛠!"
    elif mood == "angry":
        return "🔥 The fire within you is powerful, Charan. Channel it wisely, and you’ll forge a brighter tomorrow. 🔆"
    else:
    	return "🤔 Hmm... I don't have a fortune for that mood."


def main():
    print("🔮 Welcome to Charan's Fortune Teller (20JE0383) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/excited/stressed/angry): ").lower()
    fortune = get_fortune(mood)
    print(fortune)

if __name__ == "__main__":
    main()