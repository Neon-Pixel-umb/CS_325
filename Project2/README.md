# eBay Product Review Scraper

This project is a web scraper designed to automatically fetch and save user reviews for specific product versions from eBay. The scraper reads URLs from a file, and it will fetch up to 10 pages of reviews per product automatically.

## Features
- Scrapes user reviews for multiple product versions.
- Extracts both the title and the comment from each review.
- Saves the reviews for each product in a separate `.txt` file.
- Limits the number of pages to 10 per product, ensuring efficient scraping.
  
## Tested Products
This scraper has been successfully tested on the following products:
1. **Meta Quest 3**
2. **Meta Quest 2**
3. **Oculus Go**
4. **Oculus Rift S**

## Setup Instructions

### Prerequisites
1. **Conda**: You need to have [Anaconda](https://www.anaconda.com/products/distribution) installed to create and manage the required Python environment.
2. **Python 3.9**: The project runs on Python 3.9.

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Step 2: Create and Activate the Conda Environment
The requirements.yml file includes all necessary dependencies for the project.
```bash
conda env create -f requirements.yml
conda activate webscraping_env
```

### Step 3: Prepare the URLs File
Go to the Product ratings and reviews section of the desired product on eBay.
Click "See all x Reviews" to open the full review page.
Copy the URL from the browser's address bar and paste it into a file named urls.txt. Ensure that each URL is on its own line.
Example urls.txt content:
```bash
https://www.ebay.com/urw/Meta-Quest-3-128GB-VR-Headset-White/product-reviews/27063012682?_itm=256687906775
https://www.ebay.com/urw/Meta-Oculus-Quest-2-128GB-Standalone-VR-Headset-White/product-reviews/20049175729?_itm=387531912888
```
Note: There is no need to gather URLs for each page. The script will automatically go through the first 10 pages of reviews for each product.
### Step 4: Run the Script
```bash
python WebScrapper.py
```
### Step 5: Review the Output
The scraper will save each product's reviews in separate text files named review_text_Product_1.txt, review_text_Product_2.txt, etc. You can find these files in the same directory where the script is run.

