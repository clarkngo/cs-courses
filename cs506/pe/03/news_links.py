"""
# 🤖 AI Assistant Prompting Techniques

## 1. Goal Setting and Constraints
- **Primary Goal:** Extract the main story links and titles from the Hacker News front page.
- **Constraint:** Use the 'requests' library to fetch content and 'BeautifulSoup' to parse the HTML.
- **New Feature:** After extraction, save all titles and links to a CSV file named 'hacker_news_links.csv'.
- **Output Format:** The file should have two columns: 'Title' and 'Link URL'.
- **Best Practice Reminder:** Acknowledge that using the official Hacker News API is the recommended method for production or heavy use.

## 2. Contextual Information
- The target URL is 'https://news.ycombinator.com/news'.
- The external links/titles are contained within <a> tags that have the CSS class 'titlelink'.

## 3. Desired Output Format
- A dictionary where keys are the story titles (strings) and values are the corresponding URLs (strings).
- A formatted printout of the results, clearly showing the Title and Link for each entry.
- A saved file named 'hacker_news_links.csv'.
"""

import requests
from bs4 import BeautifulSoup
import csv
from typing import Dict, Optional

def extract_hn_links(url: str) -> Optional[Dict[str, str]]:
    """
    Fetches the Hacker News front page and extracts the titles and external URLs
    of the main stories using BeautifulSoup.

    This function specifically targets <a> tags with the class 'titlelink',
    which contain the submission's title and the link to the external article.

    Args:
        url: The URL of the Hacker News page to scrape (e.g., "https://news.ycombinator.com/news").

    Returns:
        An optional dictionary mapping story titles to their URLs.
        Returns None if the HTTP request fails.
    """
    print(f"📡 Attempting to fetch content from: {url}")
    try:
        # Fetch the page content
        # Setting a User-Agent is good practice to mimic a real browser
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx or 5xx)

        # Parse the HTML content using the built-in 'html.parser'
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> tags with the specific class for the main story title links
        story_link_tags = soup.find_all('a', class_='titlelink')

        extracted_links = {}

        # Iterate over the found tags and extract the text (title) and href (URL)
        for link_tag in story_link_tags:
            title = link_tag.get_text()
            href = link_tag.get('href')

            # Store the title and the external link
            extracted_links[title] = href

        return extracted_links

    except requests.exceptions.RequestException as e:
        print(f"🚨 An error occurred while fetching the page: {e}")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return None

def save_links_to_csv(data: Dict[str, str], filename: str = 'hacker_news_links.csv') -> None:
    """
    Saves a dictionary of titles and links to a CSV file.

    Args:
        data: A dictionary where keys are titles and values are URLs.
        filename: The name of the file to save the data to.
    """
    fieldnames = ['Title', 'Link URL']
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for title, url in data.items():
                writer.writerow({'Title': title, 'Link URL': url})

        print(f"\n✅ Successfully saved {len(data)} links to **{filename}**.")
    except Exception as e:
        print(f"\n❌ Failed to save data to file {filename}: {e}")

# --- Execution Block ---
# This block runs when the script is executed directly
if __name__ == "__main__":
    hn_url = "https://news.ycombinator.com/news"
    
    # 1. Extract the data
    links = extract_hn_links(hn_url)

    if links:
        # 2. Save the data to file
        output_filename = 'hacker_news_links.csv'
        save_links_to_csv(links, output_filename)
        
        # 3. Print the data to the console (for verification)
        print("\n--- Console Output (Verification) ---")
        for title, href in list(links.items())[:5]: # Print only the first 5 for brevity
            print(f"📰 **Title:** {title[:70]}...")
            print(f"🔗 **Link:** {href}")
            print("-" * 30)
        
        print(f"\n...and {len(links) - 5} more links were saved to the file.")

    else:
        print("\nCould not proceed with saving as no links were extracted.")