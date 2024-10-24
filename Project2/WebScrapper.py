import requests
from bs4 import BeautifulSoup
import time

# Function to read URLs from a text file
def read_urls_from_file(file_path):
    with open(file_path, 'r') as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]  # Read each line, stripping whitespace
    return urls

# Function to scrape reviews for a given URL
def get_reviews(url, max_pages=10):
    reviews = []
    page_number = 1
    while page_number <= max_pages:  # Limit the number of pages
        response = requests.get(url, params={"pgn": page_number})
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            review_sections = soup.find_all('div', class_='ebay-review-section')

            if not review_sections:
                # Stop if no more reviews are found
                break

            for review in review_sections:
                # Updated tag selectors based on your provided HTML
                title_tag = review.find('h3', itemprop='name')
                comment_tag = review.find('p', itemprop='reviewBody')
                
                # Only process the review if both the title and comment exist
                if title_tag and comment_tag:
                    title = title_tag.get_text(strip=True)
                    comment = comment_tag.get_text(strip=True)
                    reviews.append(f"Title: {title}\nComment: {comment}\n")
            
            print(f"Fetched page {page_number} for {url}")
            page_number += 1
            time.sleep(2)  # Delay to avoid hitting request limits
        else:
            print(f"Failed to fetch the page: {url}")
            break

    return reviews

# Main function to read URLs and scrape reviews
def main():
    # Read URLs from file
    urls = read_urls_from_file('urls.txt')
    
    # Scrape reviews for all URLs from the file
    for index, url in enumerate(urls, start=1):  # Adding an index for file names
        product_reviews = get_reviews(url, max_pages=10)  # Limit to 10 pages

        # Only save if reviews were found
        if product_reviews:
            filename = f"review_text_Product_{index}.txt"  # Use index for filenames
            
            # Save reviews to text file using utf-8 encoding
            with open(filename, 'w', encoding='utf-8') as f:
                for review in product_reviews:
                    f.write(review + "\n")
            
            print(f"Saved reviews to {filename}")
        else:
            print(f"No reviews found for {url}")

# Run the main function
if __name__ == "__main__":
    main()
