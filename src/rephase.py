#!/usr/bin/python3

import os
import sys
import json
from openai import OpenAI


def convert_to_compliant_json(chat_completion_message):
    # Convert the given object to a compliant format for the script filter
    compliant_json = {
        "items": [
            {
                "title": chat_completion_message.content,
                "subtitle": "",
                "arg": chat_completion_message.content,
            }
        ]
    }
    # Convert the dictionary to a JSON string
    return json.dumps(compliant_json, ensure_ascii=False)


if __name__ == "__main__":

    client = OpenAI(api_key=os.environ.get("openai_api_key"))
    target_language = os.environ.get("target_language")
    model = os.environ.get("model")
    prompt = os.environ.get("prompt3")

    text_list = sys.argv[1:]

    # print(text_list)

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": "rephase the following sentences: \n{}".format(text_list[0]),
            },
        ],
    )

    # Convert the completion to a JSON string
    json_string = convert_to_compliant_json(completion.choices[0].message)
    print(json_string)
