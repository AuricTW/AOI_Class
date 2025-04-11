# pip install httpx==0.27.2
# pip install openai>=1.55.3
from openai import OpenAI
#sk-proj-
# V4RLgj_23IZC3CLelpf_WzJwtEcrSBNIy9e-wEemhiHnoGKFS32aGprrxD2eD0xxN8nylWt7irT3BlbkFJzKCMrbMYpPyM0kNwksxbBXs3QL_
# OJivY6MPJe2FcuM58XCiHzwpZ7gv24vDkFQRBqJLzqkuiQA
client = OpenAI(api_key="")

prompt = """
你好
"""

response = client.responses.create(
    model="o3-mini",
    reasoning={"effort": "low"}, #medium
    input=[
        {
            "role": "user", 
            "content": prompt
        }
    ]
)

print(response.output_text)