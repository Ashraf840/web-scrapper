from scrape_for_keywords import scrape_for_keyword

def scrapper(url: str) -> tuple:
  """
  Expects a url of type string in the parameter.
  Set the webpage-url along with the keywords to search for in the webpage's text contents to invoke the actual scrapping function. This function will return a combination of data types.
  """
  url_to_scrape = url
  #keyword_to_search = 'off'  # Variant-1: pass string
  #keyword_to_search = 'sale'
  keyword_to_search = ['off', 'sale', 'discount'] # Variant-1: pass string; Can pass the list using params
  #keyword_to_search = []

  result = scrape_for_keyword(url_to_scrape, keyword_to_search)
  print("Type of result:", type(result))
  #print("Length:", len(result[1]))
  #print(result)
  return result