from model.target import Target

def get_opening(context: Target) -> str:
    opening_prompt = f"""
    I want to {context.goal}, and I am {context.situation}. \
    The person I want to approach is a {context.occupation} \
    and our relationship is {context.relationship}. \
    That person is {context.activity}. \

    Here is a list of tactics to start a conversation: \
    ["Ask an easy questions", "Ask them about themselves", \ 
    "Use environmental triggers", "Introduce myself", \
    "Say something surprising or shocking", \
    "Use wit and wisdom"]  \

    Generate a conversation starter for each tactic in html format with bold bullet points \
    and create spaces between parts. \
    """
    return opening_prompt

def get_topic(context: Target) -> str:
    topic_prompt = f"""
    I want to {context.goal}, and I am {context.situation}. \
    The person I want to approach is a {context.occupation} \
    and our relationship is {context.relationship}. \
    That person is {context.activity}. \

    Generate 5 conversatinal topics with overview for each topic in html format with bold bullet points \
    and create spaces between parts. \
    """
    return topic_prompt

def get_sustain(context: Target) -> str:
    sustain_prompt = f"""
    I want to {context.goal}, and I am {context.situation}. \
    The person I want to approach is a {context.occupation} \
    and our relationship is {context.relationship}. \
    That person is {context.activity}. \

    Here is a list of tactics of how to sustain a conversation: \
    ["Ask follow-up questions", "Ask for their opinion", \
    "Expressing Care", "Tell stories"] \

    Generate a conversation sustainer for each tactic in html format with bold bullet points \
    and create spaces between parts. \
    """
    return sustain_prompt

def get_rapport(context: Target) -> str:
    rapport_prompt = f"""
    I want to {context.goal}, and I am {context.situation}. \
    The person I want to approach is a {context.occupation} \
    and our relationship is {context.relationship}. \
    That person is {context.activity}. \

    Here is a list of tactics of how to build rapport: \
    ["Use Empathetic Language", "Active listening", \
    "Mirroring", "Open Honesty"] \

    For each tactic, show me how to use it and return in html format with bold bullet points \
    and create spaces between parts. \
    """
    return rapport_prompt

def get_closing(context: Target) -> str:
    closing_prompt = f"""
    I want to {context.goal}, and I am a {context.situation}. \
    The person I am talking to is a {context.occupation} \
    and our relationship is {context.relationship}. \

    I want to end the conversation. \
    Here is a list of tactics to end a conversation: \
    ["Describe the essence of what has been said" \
    "Say that the conversation is complete", \
    "Put them off to another time", \
    "Give short answers and ask closed questions" \
    "Introduce a friend", \
    "Wave to a friend and go to see them." \
    "Use the phone to interrupt" \
    ]

    Generate a conversation ender \
    for each tactic in html format with bold bullet points. \
    Start a new line for each bullet point. \
    """
    return closing_prompt

def get_joke(context: Target) -> str:
    joke_prompt = f"""
    I want to {context.goal}, and I am a {context.situation}. \
    The person I am talking to is a {context.occupation} \
    and our relationship is {context.relationship}. \
    
    There are 3 types of humors I want to use: \
    ["Self-deprecating", "Misdirection", "Exaggeration", "Puns"] \
    
    For each type of humor, generate three jokes and \
    return in html format with italic bullet points and bold headings, \ 
    and make sure to create 2 spaces between parts. \
    """
    return joke_prompt

def get_excuse(context: Target) -> str:
    excuse_prompt = f"""
    I want to {context.goal}, and I am a {context.situation}. \
    The person I am talking to is a {context.occupation} \
    and our relationship is {context.relationship}. \
    
    When I make a bad mistake in a conversation, there are five tactics to excuse: \
    ["Explaning Good Intention", "Apology", "Forgetting", "Deflection", Distraction] \
    
    Explain each tactic with an example and \
    return in html format with italic bullet points and bold headings, \ 
    and make sure to create 2 spaces between parts. \
    """
    return excuse_prompt













