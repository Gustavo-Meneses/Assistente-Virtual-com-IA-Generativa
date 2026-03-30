class ConversationMemory:
    def __init__(self, max_history=5):
        self.history = []
        self.max_history = max_history

    def add(self, user, assistant):
        self.history.append({
            "user": user,
            "assistant": assistant
        })

        if len(self.history) > self.max_history:
            self.history.pop(0)

    def get_context(self):
        context = ""
        for h in self.history:
            context += f"Usuário: {h['user']}\nAssistente: {h['assistant']}\n"
        return context
