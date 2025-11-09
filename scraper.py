from playwright.sync_api import sync_playwright
import re

def extract_numbers_from_page(page):
    """Extract all numbers from tables on a page"""
    numbers = []
    
    # Wait for page to load
    page.wait_for_load_state('networkidle')
    
    # Find all tables
    tables = page.locator('table').all()
    
    for table in tables:
        # Get all text content from the table
        text_content = table.inner_text()
        
        # Extract all numbers (including decimals and negatives)
        found_numbers = re.findall(r'-?\d+\.?\d*', text_content)
        
        for num_str in found_numbers:
            try:
                num = float(num_str)
                numbers.append(num)
            except ValueError:
                continue
    
    return numbers

def main():
    urls = [
        "https://rack-tds.vercel.app/table?seed=14",
        "https://rack-tds.vercel.app/table?seed=15",
        "https://rack-tds.vercel.app/table?seed=16",
        "https://rack-tds.vercel.app/table?seed=17",
        "https://rack-tds.vercel.app/table?seed=18",
        "https://rack-tds.vercel.app/table?seed=19",
        "https://rack-tds.vercel.app/table?seed=20",
        "https://rack-tds.vercel.app/table?seed=21",
        "https://rack-tds.vercel.app/table?seed=22",
        "https://rack-tds.vercel.app/table?seed=23",
    ]
    
    all_numbers = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        for url in urls:
            print(f"Scraping {url}...")
            page.goto(url)
            numbers = extract_numbers_from_page(page)
            print(f"Found {len(numbers)} numbers")
            all_numbers.extend(numbers)
        
        browser.close()
    
    total = sum(all_numbers)
    print(f"\n{'='*50}")
    print(f"TOTAL SUM OF ALL NUMBERS: {total}")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    main()
