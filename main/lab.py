import os
import requests

"""
All requests to the LLM require some form of a key.
Other sensitive data has also been hidden through environment variables.
"""
api_key = os.environ['OPENAI_API_KEY']
base_url = os.environ['OPENAI_API_BASE']
deployment = os.environ['OPENAI_API_DEPLOYMENT']
version = os.environ['OPENAI_API_VERSION']
"""
This function will use the string defined below to form a system prompt. 
Then, user input will be passed into the LLM to be
interpreted. In this case, it is expected for resources/prompt.txt to provide the LLM
with instructions for classifying by sentiment (positive or negative.) This is usually
in the context of categorizing human text such as online posts & product reviews
between positive (eg, happy, excited, 5-star) and negative (eg, angry, disappointed,
1-star) text. This is an elementary problem within AI, and the AI will understand
sentiment classification so long as you provide it the instructions for classifying
"positive" and "negative" inputs in the prompt. Because the AI understands the task
without the need for any shown examples, this is considered a zero-shot problem.
"""

"""
TODO: Change the prompt below to allow for classification as described above.
"""
prompt = ""

"""
There is no need to change the below function. It will properly use the prompt &
user input as needed.
"""


def classify(user_input):
    res = requests.post(f"{base_url}/deployments/{deployment}/chat/completions?api-version={version}",
                        headers={
                            "Content-Type": "application/json",
                            "api-key": f"{api_key}"
                        },
                        json={
                            "messages": [
                                {"role": "system",
                                 "content": f"{prompt}"},
                                {"role": "user",
                                 "content": f"{user_input}"}],
                        })
    message = str(res.json().get("choices")[0].get("message").get("content"))
    print(message)
    if "positive" in message.lower():
        return "positive"
    elif "negative" in message.lower():
        return "negative"
    else:
        return "user input was not properly classified"
