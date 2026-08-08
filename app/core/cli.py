from app.services.ollama_service import generate_response


class AICommandCenter:
    def __init__(self):
        self.conversation_history = []

    def start(self):
        self._show_welcome()

        while True:
            try:
                user_input = input("You: ").strip()

                if not user_input:
                    continue

                if user_input.startswith("/"):
                    should_exit = self._handle_command(user_input)

                    if should_exit:
                        break

                    continue

                self._chat(user_input)

            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break

            except Exception as error:
                print(f"\nError: {error}\n")

    def _show_welcome(self):
        print("=" * 55)
        print("              AI COMMAND CENTER")
        print("=" * 55)
        print("Local AI Assistant")
        print("Model: llama3.2:3b")
        print()
        print("Type /help to see available commands.")
        print("Type /exit to quit.")
        print("=" * 55)
        print()

    def _chat(self, user_input):
        self.conversation_history.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        print("\nAI: ", end="", flush=True)

        response = generate_response_with_history(
            self.conversation_history
        )

        self.conversation_history.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        print(response)
        print()

    def _handle_command(self, command):
        command = command.lower().strip()

        if command == "/help":
            self._show_help()

        elif command == "/clear":
            self.conversation_history.clear()
            print("\nConversation memory cleared.\n")

        elif command == "/model":
            print("\nCurrent model: llama3.2:3b")
            print("Runtime: Ollama")
            print("Mode: Local AI\n")

        elif command == "/history":
            self._show_history()

        elif command == "/exit":
            print("\nGoodbye! 👋")
            return True

        else:
            print(
                f"\nUnknown command: {command}"
                "\nType /help to see available commands.\n"
            )

        return False

    def _show_help(self):
        print(
            """
Available Commands
------------------
/help       Show available commands
/clear      Clear conversation memory
/model      Show active AI model
/history    Show conversation history
/exit       Exit the application
"""
        )

    def _show_history(self):
        if not self.conversation_history:
            print("\nNo conversation history.\n")
            return

        print("\nConversation History")
        print("--------------------")

        for message in self.conversation_history:
            role = message["role"].upper()
            content = message["content"]

            print(f"{role}: {content}")

        print()


def generate_response_with_history(history):
    import ollama

    from app.config.settings import AI_MODEL, OLLAMA_HOST

    client = ollama.Client(host=OLLAMA_HOST)

    response = client.chat(
        model=AI_MODEL,
        messages=history,
    )

    return response["message"]["content"]


def start_cli():
    assistant = AICommandCenter()
    assistant.start()