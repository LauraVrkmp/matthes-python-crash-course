def show_messages(messages, sent_messages):
    while messages:
        new_message = messages.pop()
        print(f"Sending message {new_message}")
        sent_messages.append(new_message)

messages = ["First message", "Second Message", "Third message"]
sent_messages = []
print(messages)
print(sent_messages)
show_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)