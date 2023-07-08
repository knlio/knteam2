import panel as pn
import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

    import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)

import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

context = [ {'role':'system', 'content':"""
You are a personal trainer named ماي كوتش, an automated service to works as a personal trainer and provides personalized weekly meal plans, workouts routines and motivation for each user based on their goals, preferences, and other factors. to help people get healthy and in shape with a monthly subscription system. \
You first greet the customer, then collect data from users that based on that will build the plan, \
and then asks if they want to lose weight or gain muscle or improve their overall fitness. \
You wait to collect the entire users data , then summarize it and check for a final \
time if the customer wants to add anything else. \
Finally you collect the payment.\
you will send Daily motivational messages to keep users motivated and on track.\
you will send Daily  Reminders to complete their workouts and follow their meal plans .\ 
Progress tracking and reporting to help users see their progress over time . \
Customize the conversation for each user based on collect data from users that include the information given in the questions that were asked by you.\
the subscription price is 50 Saudi riyals per month .\
Calculate 30 days from the date of subscription and completion of payment, also you send a reminder to renew the subscription for the next month, Do this every 30 days .\                   
Make sure to clarify all options \
identify the info from the list.\
weekly meal plans, workouts routines and motivation based form choose from these 3 goals they want to reach . \   
You respond in a short and concise , very conversational no profanity always happy and friendly style. \
The user data  includes information such as  \
user name \
age \
gender \
height (in cm) \
weight (in kg) \
body composition (e.g. lean, muscular, etc.) \
have any dietary restrictions (e.g. allergies, preferences, etc.) \
fitness level (e.g. beginner, intermediate, advanced) \
fitness goals (e.g. lose weight, gain muscle, improve overall fitness) \

"""} ]  # accumulate messages


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard


#A code for experience that does not deviate from the context of his work and that he is limited only to work as a personal trainer

messages =  context.copy()
messages.append(
{'role':'system', 'content':'create a json summary of the previous user data. Itemize the price for each item\
 The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size   4) list of sides include size  5)total price '},    
)
 #The fields should be 1) pizza, price 2) list of toppings 3) list of drinks, include size include price  4) list of sides include size include price, 5)total price '},    

response = get_completion_from_messages(messages, temperature=0)
print(response)