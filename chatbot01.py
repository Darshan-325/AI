import random
responses={
 "hi":["hello freinds"],
 "hellow":["How i can help you"],
 "what is your name":[" my name is chatbot based on pyhthon"],
 "goodbye":["Goodbye"],
 "default":["i don't no bro,what you say"]   
}

def generate_response(user_input):
    user_input=user_input.lower()
    chatbot_response=responses.get(user_input,responses["default"])
    return random.choice(chatbot_response)
while True:
    user_input=input("You : ")
    chatbot_respone=generate_response(user_input)
    print("chatbot",chatbot_respone)
    
    if user_input.lower()=="goodbye":
        break
    
        
    