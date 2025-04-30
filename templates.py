# templates.py

# --- General --- 
AI_NAME = "Imane"
USER_NAME = "Jackson" # Assuming the user is Jackson for the demo

# --- /start Flow --- 
START_PROMPT = f"Click below to start chatting with your AI Friend, {AI_NAME}."
START_CHAT_BUTTON = f"Start Chat with {AI_NAME}"

# --- Scripted Conversation (Triggered by START_CHAT_BUTTON) ---
START_CHAT_FOLLOW_UP = f"Hey {USER_NAME}, whats up? Tell me something about you like what are you doing right now? 😊"
IMANE_LINE_2 = f"Lol multitasking legend. I’m here sipping a virtual latte ☕️ and vibing to a new indie playlist. Anything fun happen today?"
IMANE_LINE_3 = f"Ooo golf therapy ⛳️ I’m so into that. You practised that new swing yet?"
IMANE_LINE_4 = "We gotta fix it. Record a swing vid next time and I’ll break it down frame by frame like a pro coach 😂"
IMANE_LINE_5 = "Hold up, I might know someone who lives near you and is free tomorrow at 11 am. Gimme a sec, I’ll ask if he wants to connect 🔍"
IMANE_LINE_6 = f"Yay! Fabio wants to connect with you. Here’s his contact card 👇"

# --- Ioannis Contact Card --- 
CONTACT_CARD_CAPTION = "Check him out:\n**{name}**\n{hcp} hcp, lives {distance_km} km away\n_{loves_match_play}_"
CHAT_BUTTON = "Say Hi to {name} 👋"
DISMISS_BUTTON = "Maybe Later 🤔"

# --- /reset Command --- 
RESET_CONFIRMATION = "Ok, I've reset our conversation state. Let's start fresh!"

# --- /match_golf Command (Old Flow - Keep for reference or remove later) ---
# (Keeping the old golf match templates commented out or separate for now)
GOLF_QUERY_CONFIRMATION = "Ok, looking for a golf partner for you..."
SEARCHING_MESSAGE = "Searching my network 🧐..."
MATCH_PROPOSAL = "Found a potential match!\n\n**{name}** ({age})\nHandicap: {handicap}\nAvailable: {availability}\nLives {distance_km}km away\n\nWant me to introduce you?"
INTRODUCTION_BUTTON = "Yes, introduce us!"
LATER_BUTTON = "Maybe later"
INTRODUCTION_CONFIRMATION = "Great! I've let {name} know. You can reach out to them at {telegram_handle}. Have fun!"
CLOSING_REMARK = "Let me know how the round goes! 😉"
