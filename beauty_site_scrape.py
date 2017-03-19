#!usr/bin/env python3

# import the library used to query a website
import urllib.request
# import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup


def get_html(url):
    # Query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(url)
    return page


def page_parse(url):
    # Parse the html in the 'page' variable, and store it in Beautiful Soup format
    soup = BeautifulSoup(get_html(url))
    return soup


def ulta_scrape():
    # Build a list comprised of ulta category base urls and the number of pages in that category, and a blank dictionary for page contents
    ulta_page_list = [("http://www.ulta.com/tools-brushes-makeup-brushes-tools?N=27hn", 11),
                      ("http://www.ulta.com/tools-brushes-hair-styling-tools?N=27gc", 7),
                      ("http://www.ulta.com/tools-brushes-skincare-tools?N=27g5", 2),
                      ("http://www.ulta.com/tools-brushes-hair-brushes-combs?N=27gj", 4)
                      ]
    page_contents = {}
    for entry in ulta_page_list:
        # Split the base URL and number of pages into separate variables
        base_url, num_pages = entry
        # For each page in the base_url category, construct and return a full url
        for page_num in range(0, num_pages):
            # ulta site structure for page 2 and beyond is base_url+'&No='+(48*page_num)+'&Nrpp='+(48*page_num)
            if page_num == 0:
                address = base_url
            else:
                step = 48*page_num
                address = base_url+'&No='+str(step)+'&Nrpp='+str(step)
            # add page url and contents to the page_contents dictionary
            page_contents[address] = page_parse(address)
    return page_contents

if __name__ == '__main__':
    print(ulta_scrape())
    
# Future Plans
# - parse out product title and image from BeautifulSoup content in page_contents
# - consider adjusting to obtain just one page via randomly selecting options rather than indexing all possible items
# - add sephora scrape
# - cloudability image manilpuation via api
# - deep dream image manipulation via api