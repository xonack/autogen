import autogen

config_list = [
    {   
        'model': 'gpt-3.5-turbo-16k',
        'api_key': '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',
    }
]

llm_config = {
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(
    "assistant", 
    llm_config=llm_config,
    system_message=""
    )

user_proxy = autogen.UserProxyAgent(
    "user_proxy", 
    human_input_mode="TERMINATED",
    max_consecutive_auto_reply=5,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "app_coding"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been soved at full satisfaction. 
    Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
    )

# autogen.ChatCompletion.start_logging()

task = """
Write python code to output numbers 1 to 100, and then store in a file

"""

user_proxy.initiate_chat(
    assistant, 
    message=task
    )

# import json

# json.dump(autogen.ChatCompletion.logged_history, open("conversations.json", "w"), indent=4)