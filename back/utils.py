def validate_chat_history(chat_history: list) -> bool:
    """
    Validates that the chat history alternates between 'user' and 'agent'.
    """
    if not chat_history:
        return True
    
    for i in range(len(chat_history) - 1):
        current_role = chat_history[i].get("role")
        next_role = chat_history[i + 1].get("role")
        
        if current_role == next_role or current_role not in ["user", "agent"]:
            return False
    return True
