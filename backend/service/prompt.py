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

    Generate a conversation starter for each tactic. \
    """
    return opening_prompt

def get_topic(context: Target) -> str:
    topic_prompt = f"""
    I want to {context.goal}, and I am {context.situation}. \
    The person I want to approach is a {context.occupation} \
    and our relationship is {context.relationship}. \
    That person is {context.activity}. \

    Generate 5 conversatinal topics with overview for each topic. \
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

    Generate a conversation sustainer for each tactic. \
    """
    return sustain_prompt

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

    Generate a conversation ender, \
    which is relevant in this situation, for each tactic. \
    """
    return closing_prompt

def get_joke(context: Target) -> str:
    joke_prompt = f"""
    I want to {context.goal}, and I am a {context.situation}. \
    The person I am talking to is a {context.occupation} \
    and our relationship is {context.relationship}. \
    
    Generate five self-deprecating jokes. \
    """
    return joke_prompt













