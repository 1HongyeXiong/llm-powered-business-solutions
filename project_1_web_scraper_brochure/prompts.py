link_system_prompt = "You are provided with a list of links found on a webpage. You are able to decide which of the links would be most relevant to include in a brochure about the company, such as links to an About page, or a Company page, or Careers/Jobs pages. Respond in JSON as in this example: { 'links': [ { 'type': 'about page', 'url': 'https://full.url/goes/here/about' }, { 'type': 'careers page', 'url': 'https://another.full.url/careers' } ] }"

def get_links_user_prompt(website):
    user_prompt = f"Here is the list of links on the website of {website.url}:\n"
    user_prompt += "Please decide which of these are relevant web links for a brochure about the company.\n"
    user_prompt += "\n".join(website.links)
    return user_prompt

