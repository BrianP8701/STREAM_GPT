import tiktoken

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = 0
    for message in messages:
        num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":  # if there's a name, the role is omitted
                num_tokens += -1  # role is always required and always 1 token
    num_tokens += 2  # every reply is primed with <im_start>assistant
    return num_tokens

def concatenate_with_indices(string_list):
    '''
    Concatenates a list of strings, separating them with four new lines and 
    prefixing each with its index in the format '<Category n>'.

    Args:
    - string_list (list of str): The list of strings to concatenate.

    Returns:
    - str: The concatenated string with indices and newline separations.
    '''
    result = ""
    for index, string in enumerate(string_list):
        result += f'<Category {index}>\n{string}\n\n\n\n'
    return result