from groq import Groq
import os
os.environ["GROQ_API_KEY"] = "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"
client = Groq()
response = client.chat.completions.create(
    model="meta-llama/llama-guard-4-12b",
    messages=[
        {"role": "system", "content": "You are a python programming expert."
         },
        {
            "role": "user", "content": "How python language saves a variable in memory."
        }
    ]
) 