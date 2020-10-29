# We can make the parrot.py program run as long as the user wants by putting
# most of the program inside a while loop. We’ll define a quit value and then
# keep the program running as long as the user has not entered the quit value:

prompt = "\n Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message.lower() != 'quit':
    message = input(prompt)
    if message.lower() != 'quit':
        print(message)