import webbrowser
from urllib.parse import quote_plus
from tools.decorators import tool
import subprocess

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "yt": "https://www.youtube.com",

    "github": "https://github.com",
    "gh": "https://github.com",

    "linkedin": "https://www.linkedin.com",
    "linkedin profile": "https://www.linkedin.com",

    "chatgpt": "https://chat.openai.com",
    "openai": "https://chat.openai.com",

    "gmail": "https://mail.google.com",
    "mail": "https://mail.google.com",
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
    description="Open a website by name.",
    direct_response=True
)
def open_website(website_name):

    # Normalize the input
    website_name = website_name.lower().strip()

    website_name = website_name.replace("https://", "")
    website_name = website_name.replace("http://", "")
    website_name = website_name.replace("www.", "")

    if website_name.endswith(".com"):
        website_name = website_name[:-4]

    url = WEBSITES.get(website_name)

    if url is None:
        return f"Sorry, I don't know how to open '{website_name}'."

    try:
        webbrowser.open_new_tab(url)
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
        subprocess.Popen(
        ["cmd", "/c", "start", "", url],
        shell=True
        )
        return f"Searching {platform.title()} for '{query}'."

    except Exception as e:
        return f"Failed to search {platform}: {e}"