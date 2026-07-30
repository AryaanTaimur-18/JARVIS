import webbrowser
from urllib.parse import quote_plus
from tools.decorators import tool

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "linkedin": "https://www.linkedin.com",
    "chatgpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com",
}

SEARCH_URLS = {
    "google": "https://www.google.com/search?q=",
    "youtube": "https://www.youtube.com/results?search_query=",
    "github": "https://github.com/search?q=",
    "linkedin": "https://www.linkedin.com/search/results/all/?keywords=",
    "stackoverflow": "https://stackoverflow.com/search?q=",
    "chatgpt": "https://chat.openai.com/?q="
}

@tool(
    name="open_website",
    description="Open a website by name."
)
def open_website(website_name):

    website_name = website_name.lower()

    if website_name.startswith(("http://", "https://")):
        url = website_name
    else:
        url = WEBSITES.get(website_name)

    if url is None:
        return f"Sorry, I don't know how to open '{website_name}'."

    try:
        webbrowser.open(url)
        return f"Opening {website_name.title()}."

    except Exception as e:
        return f"Failed to open {website_name}: {e}"

@tool(
    name="search_web",
    description=(
        "Search a supported platform for a query. "
        "Supported platforms include google, youtube, github, linkedin, stackoverflow and chatgpt."
    )
)
def search_web(platform, query):

    platform = platform.lower()

    base_url = SEARCH_URLS.get(platform)

    if base_url is None:
        return f"Sorry, I don't support searching on '{platform}'."

    encoded_query = quote_plus(query)

    url = base_url + encoded_query

    try:
        webbrowser.open(url)
        return f"Searching {platform.title()} for '{query}'."

    except Exception as e:
        return f"Failed to search {platform}: {e}"