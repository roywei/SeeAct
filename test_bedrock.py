
import os
import boto3

#MODEL_ID = "us.meta.llama3-2-11b-instruct-v1:0"
MODEL_ID = "arn:aws:bedrock:us-west-2:897880167187:imported-model/skiml9az32mw"
IMAGE_NAME = "fridge.png"

bedrock_runtime = boto3.client("bedrock-runtime", 
                               aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"], 
                               aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"], 
                               aws_session_token=os.environ["AWS_SESSION_TOKEN"])

with open(IMAGE_NAME, "rb") as f:
    image = f.read()

user_message = "What's in the fridge?"

messages = [
    {
        "role": "user",
        "content": [
            {"image": {"format": "png", "source": {"bytes": image}}},
            {"text": user_message},
        ],
    }
]

response = bedrock_runtime.converse(
    modelId=MODEL_ID,
    messages=messages,
)
response_text = response["output"]["message"]["content"][0]["text"]
print(response_text)