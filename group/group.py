import autogen

config_list = [
    {   
        'model': 'gpt-4',
        'api_key': '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',
    }
]

llm_config = {"config_list": config_list, "seed": 44}
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
    human_input_mode="TERMINATE",
)
coder = autogen.AssistantAgent(
    name="Coder",
    # system_message="Codes python.",
    llm_config=llm_config,
)
pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Creative in software product ideas.",
    llm_config=llm_config,
)

groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

user_proxy.initiate_chat(manager, message="Find one latest paper about gpt-4 on arxiv and find its potential applications in software.")