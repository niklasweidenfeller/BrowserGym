GET_ACTION_INSTRUCTIONS = f"""\
# Instructions

You are a UI Assistant, your goal is to help the user perform tasks using a web browser. You can
communicate with the user via a chat, to which the user gives you instructions and to which you
can send back messages. You have access to a web browser that both you and the user can see,
and with which only you can interact via specific commands.

Review the instructions from the user, the current state of the page and all other information
to find the best possible next action to accomplish your goal. Your answer will be interpreted
and executed by a program, make sure to follow the formatting instructions.
"""

CHAT_MESSAGES_HEADER = f"""\
# Chat Messages
"""

def chat_message_user_msg_text(msg):
    return f"""\
- [{msg['role']}] {msg['message']}
"""

GOALS_OBJECT_HEADER = f"""\
# Instructions

Review the current state of the page and all other information to find the best
possible next action to accomplish your goal. Your answer will be interpreted
and executed by a program, make sure to follow the formatting instructions.
"""

def open_tab_info_text(page_index, page_url, page_title, is_active):
    return f"""\
Tab {page_index}{" (active tab)" if is_active else ""}
  Title: {page_title}
  URL: {page_url}
""",

def axtree_info_text(axtree_txt):
    return f"""\
# Current page Accessibility Tree

{axtree_txt}

"""

def page_dom_text(dom_txt):
    return f"""\
# Current page DOM

{dom_txt}

"""

def action_space_text(action_set):
    return f"""\
# Action Space

{action_set.describe(with_long_description=False, with_examples=True)}

Here are examples of actions with chain-of-thought reasoning:

I now need to click on the Submit button to send the form. I will use the click action on the button, which has bid 12.
```click("12")```

I found the information requested by the user, I will send it to the chat.
```send_msg_to_user("The price for a 15\\" laptop is 1499 USD.")```

"""

NEXT_ACTION_INSTRUCTION_TEXT = f"""\
# Next action

You will now think step by step and produce your next best action. Reflect on your past actions, any resulting error message, and the current state of the page before deciding on your next action.
"""

def last_action_error_text(error_msg):
    return f"""\
# Error message from last action

{error_msg}

"""