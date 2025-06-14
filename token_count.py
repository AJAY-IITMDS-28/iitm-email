import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4")

user_message = "List only the valid English words from these: sYdJNC, K, f, JCKSf, wUy, pYw5VDwR, 8d0dQo, czzpalYG, aEArd, LZvRa0, RmAwv4mxh, Ixcgh0, rxWY0d5Wyu, AdO, DVcp8elG, X, vaH, VI, 5Si6aq5, NmU8I6VSrE, Q"

chat_message = [{"role": "user", "content": user_message}]

def count_tokens(messages, encoding):
    num_tokens = 0
    for message in messages:
        num_tokens += 4
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
    num_tokens += 2
    return num_tokens

print("Token count:", count_tokens(chat_message, encoding))

