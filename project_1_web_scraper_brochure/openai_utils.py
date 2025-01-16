import json
from openai import OpenAI
from website import Website
from prompts import link_system_prompt, get_links_user_prompt

openai = OpenAI()
MODEL = 'gpt-4o-mini'

def get_links(url):
    website = Website(url)
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(website)}
        ],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)

def get_all_details(url):
    website = Website(url)
    result = f"Landing page:\n{website.get_contents()}"
    links = get_links(url)
    for link in links["links"]:
        result += f"\n\n{link['type']}\n"
        result += Website(link["url"]).get_contents()
    return result
