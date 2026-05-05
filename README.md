from src.agent import run_agent

if __name__ == "__main__":
    print("Tactical Field Assistant AI")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Enter scenario: ")

        if user_input.lower() == "exit":
            break

        response = run_agent(user_input)
        print("\nResponse:", response, "\n")
