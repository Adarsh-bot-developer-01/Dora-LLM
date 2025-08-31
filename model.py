import random

class FridayAI:
    def __init__(self):
        self.memory = []

    def respond(self, text):
        # Simple AI response (placeholder)
        responses = [
            "I'm here, how can I help? 🤖",
            "Processing your request... ⚡",
            "Interesting! Tell me more 👀",
            "Working on it Master... 👑"
        ]
        return random.choice(responses)
