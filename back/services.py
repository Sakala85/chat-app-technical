async def process_message(user_message: str) -> str:
    user_message = user_message.lower()
    
    if "bonjour" in user_message or "salut" in user_message:
        return "Bonjour! Comment puis-je vous aider aujourd'hui?"
    
    elif "comment ça va" in user_message or "comment vas-tu" in user_message:
        return "Je vais très bien, merci! Et vous?"
    
    elif "merci" in user_message:
        return "Je vous en prie! N'hésitez pas si vous avez d'autres questions."
    
    elif "au revoir" in user_message or "bye" in user_message:
        return "Au revoir! Passez une excellente journée!"
    
    else:
        return "Je ne suis pas sûr de comprendre. Pouvez-vous reformuler votre message?"