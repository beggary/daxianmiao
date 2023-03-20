import openai

import json

# 目前需要设置代理才可以访问 api


openai.api_key = "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"

q = "你好"

rsp = openai.ChatCompletion.create(

    model="gpt-3.5-turbo",

    messages=[

        {"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"},

        {"role": "user", "content": q}

    ]

)
print(rsp.get("choices")[0]["message"]["content"])
