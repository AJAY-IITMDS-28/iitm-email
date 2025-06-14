import tiktoken

def count_tokens(messages, model="gpt-4o"):
    encoding = tiktoken.encoding_for_model(model)
    tokens_per_message = 3
    tokens_per_name = 1

    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # Every reply is primed with <|start|>assistant<|message|>
    return num_tokens

messages = [
    {"role": "user", "content": "List only the valid English words from these: sYdJNC, K, f, JCKSf, wUy, pYw5VDwR, 8d0dQo, czzpalYG, aEArd, LZvRa0, RmAwv4mxh, Ixcgh0, rxWY0d5Wyu, AdO, DVcp8elG, X, vaH, VI, 5Si6aq5, NmU8I6VSrE, Q"}
]

print(count_tokens(messages))
<|end|> and <|start|>assistant<|message|>
    num_tokens += 1  # Every reply is primed with <|end|>assistant<|message|>
    return num_tokens
    num_tokens += 1  # Every reply is primed with <|end|>assistant<|message|>