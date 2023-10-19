# from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
# # import openai
# # openai.api_key = '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'
# # config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# config_list = [
#     {
#         'model': 'gpt-3.5-turbo-16k',
#         'api_key': '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',
#     },
# ]
# assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
# user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

# user_proxy.initiate_chat(assistant, message="")
