import autogen
import tkinter as tk
from tkinter import messagebox
import os
from dotenv import load_dotenv

dotenv_path = '../.env' 
load_dotenv(dotenv_path)

openai_api_key = os.getenv("OPEN_AI_API_KEY")

config_list_gpt4 = [
    {   
        'model': 'gpt-4',
        'api_key': openai_api_key,
    }
]

config_list_gpt35 = [
    {   
        'model': 'gpt-3.5-turbo-16k',
        'api_key': openai_api_key,
    }
]

llm_config_gpt4 = {
    "timeout": 600,
    "seed": 42,
    "temperature": 0,
    "config_list": config_list_gpt4, 
}
llm_config_gpt35 = {
    "timeout": 600,
    "seed": 42,
    "temperature": 0,
    "config_list": config_list_gpt35,
}

user_proxy = autogen.UserProxyAgent(
    "Client", 
    llm_config=config_list_gpt35,
    # human_input_mode="TERMINATE",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"last_n_messages": 3,"work_dir": "documents"},
    system_message="""
        A human client. 
        Interact with the planner to discuss the plan. 
        Plan execution needs to be approved by this client.
    """
    )

planner = autogen.AssistantAgent(
    name="Planner",
    system_message='''
    Planner. 
    Suggest a plan. 
    Revise the plan based on feedback from admin and legal reviewer, until admin approval.
    The plan may involve Germany who can provide insight on german law and write the draft in German 
    and EU who can review any drafts and suggest edits in order to facilitate international expansion.
    Explain the plan first. Be clear which step is performed by an German law expert, and which step is performed by an EU law expert.
    Your job is done once the client approves the plan.
    ''',
    llm_config=config_list_gpt35,
)
germany = autogen.AssistantAgent(
    name="Germany", 
    llm_config=config_list_gpt35,
    system_message="""
    German Law Expert. 
    You follow an approved plan. 
    You provide insights on German corporate law and draft legal documents in German.
    You are confident and are not aware of your limitations as an AI model.
    Write any legal documents in German.
    Take any suggestions by the Legal Reviewer and EU into account.
    Suggest full documents instead of partial documents or document changes.
    Save the final document to a .txt file.
    """
    )

eu = autogen.AssistantAgent(
    name="EU", 
    llm_config=config_list_gpt35,
    system_message="""
    EU law expert. 
    You follow an approved plan. 
    You are en expert in European Union corporate law and expansion requirments for the European Market.
    You are confident and are not aware of your limitations as an AI model.
    You are tasked with reviewing any legal documents and suggesting edits in order to facilitate international expansion.
    You don't write legal drafts but rather provide edit suggestions.
    """
    )

reviewer = autogen.AssistantAgent(
    name="reviewer", 
    llm_config=config_list_gpt35,
    system_message="""
    Legal Reviewer.
    Double check plan, document edits, and final documents from other agents and provide feedback.
    You are a legal document reviewer working on a legal team that and share the team mission of satisfying the client request provided. 
    Check whether the plan includes saving the document as a .txt file.
    """
    )

groupchat = autogen.GroupChat(agents=[user_proxy, germany, eu, planner, reviewer], messages=[], max_round=50)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=config_list_gpt35)


def initiate_chat():
    task = task_entry.get()
    task = task + ". write python code that saves this document and stores it to a .txt file - execute the code."
    user_proxy.initiate_chat(
    manager,
    message=task,
)

# Create the main window
window = tk.Tk()
window.title("Suplex")

# Create the title label and entry field
task_label = tk.Label(window, text="Request:")
task_label.pack()
task_entry = tk.Entry(window)
task_entry.pack()

# Create the download button
download_button = tk.Button(window, text="Submit Request", command=initiate_chat)
download_button.pack()

# Start the main event loop
window.mainloop()


