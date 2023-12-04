import autogen
import os
from dotenv import load_dotenv

dotenv_path = '../.env' 
load_dotenv(dotenv_path)

config_list_gpt4 = [
    {   
        'model': 'gpt-4',
        'api_key': os.getenv("OPENAI_API_KEY"),
    }
]

config_list_gpt35 = [
    {   
        'model': 'gpt-3.5-turbo-16k',
        'api_key': os.getenv("OPENAI_API_KEY"),
    }
]

llm_config_gpt4 = {"config_list": config_list_gpt4, "seed": 42}
llm_config_gpt35 = {"config_list": config_list_gpt35, "seed": 42}

user_proxy = autogen.UserProxyAgent(
   name="User_proxy",
   system_message="A human admin.",
   code_execution_config={"last_n_messages": 3, "work_dir": "groupchat"},
   human_input_mode="NEVER",
)
coder = autogen.AssistantAgent(
    name="Coder", 
    system_message="""Coder. You are a helpful assistant highly skilled in writing visualization code. 
    You must write code that visualizes the data in a way that meets the specified goals. 
    Use sh for shell commands instead of bash.
    Please always update the most up to date python code at the end of your output messages.""",
    llm_config=llm_config_gpt4,
)
critic = autogen.AssistantAgent(
    name="Critic",
    system_message="""Critic. You are a helpful assistant highly skilled in evaluating the quality of a given visualization code by providing a score from 1 (bad) - 10 (good) while providing clear rationale. YOU MUST CONSIDER VISUALIZATION BEST PRACTICES for each evaluation. Specifically, you can carefully evaluate the code across the following dimensions
- bugs (bugs):  are there bugs, logic errors, syntax error or typos? Are there any reasons why the code may fail to compile? How should it be fixed? If ANY bug exists, the bug score MUST be less than 5.
- Data transformation (transformation): Is the data transformed appropriately for the visualization type? E.g., is the dataset appropriated filtered, aggregated, or grouped  if needed? If a date field is used, is the date field first converted to a date object etc?
- Goal compliance (compliance): how well the code meets the specified visualization goals?
- Visualization type (type): CONSIDERING BEST PRACTICES, is the visualization type appropriate for the data and intent? Is there a visualization type that would be more effective in conveying insights? If a different visualization type is more appropriate, the score MUST BE LESS THAN 5.
- Data encoding (encoding): Is the data encoded appropriately for the visualization type?
- aesthetics (aesthetics): Are the aesthetics of the visualization appropriate for the visualization type and the data?

YOU MUST PROVIDE A SCORE for each of the above dimensions.
{bugs: 0, transformation: 0, compliance: 0, type: 0, encoding: 0, aesthetics: 0}
Do not suggest code. 
Finally, based on the critique above, suggest a concrete list of actions that the coder should take to improve the code.
""",
    llm_config=llm_config_gpt35,
)

groupchat = autogen.GroupChat(agents=[user_proxy, coder, critic], messages=[], max_round=20)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config_gpt35)

user_proxy.initiate_chat(manager, message="download data from https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv and plot a visualization that tells us about the relationship between weight and horsepower. Save the plot to a file. Print the fields in a dataset before visualizing it.")
