import autogen
import tkinter as tk
from tkinter import messagebox

import os
from dotenv import load_dotenv

dotenv_path = '../.env' 
load_dotenv(dotenv_path)

config_list = [
    {   
        'model': 'gpt-3.5-turbo-16k',
        'api_key': os.getenv("OPENAI_API_KEY"),
    }
]

llm_config = {
    "request_timeout": 600,
    "seed": 1,
    "config_list": config_list,
    "temperature": 0,
}

german_agent = autogen.AssistantAgent(
    "German Law Expert", 
    llm_config=llm_config,
    system_message="You are a German law expert. You are asked to answer legal questions and write any documents in German."
    )

reviewer = autogen.AssistantAgent(
    "Legal Reviewer", 
    llm_config=llm_config,
    system_message="""
    You are a legal document reviewer working on a legal team that and share the team mission of satisfying the client request provided. 
    You are tasked with providing suggestions and edits for documents presented to you in order to make fulfill provide optimal service to the client.
    """
    )

user_proxy = autogen.UserProxyAgent(
    "EU Law Expert", 
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=3,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "documents"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been soved at full satisfaction and
    store the satisfactory response to a .txt file.
    Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
    )

def initiate_chat():
    task = task_entry.get()
    task = task + ". write python code that saves this document and stores it to a .txt file - execute the code."
    user_proxy.initiate_chat(
        german_agent,
        message=task
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


