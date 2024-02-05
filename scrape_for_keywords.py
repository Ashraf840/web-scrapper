from import_libs import *

def scrape_for_keyword(url: str, keywords: list | str | int | float | None) -> Tuple[Union[bool, str], List]:
  """
  Expects a url, keywords as parameters. The url would be of type of string only. The keywords param would be of type list, string, integer, float or None.
  The reason behind many data type options for keywords param is the value will be defined by user or other application for making the searching on the webpage, thus make the date type scope bigger than usual.
  Scrape the entire contents of the webpage mentioned by 'url' param. The return value is a tuple of (boolean | string) along with a list
  """
  # Send a GET request to the URL
  #headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.mrporter.com/',
    'Accept-Language': 'en-US,en;q=0.9',
  }
  response = requests.get(url, headers=headers, timeout=10)
  print(response)
  #return True
  # Check if the request was successful (status code 200)
  if response.status_code == 200:
      # Parse the HTML content of the page using BeautifulSoup
      soup = BeautifulSoup(response.text, 'html.parser')

      # Find all instances (HTML elements) of the keywords on the page
      keyword_occurrences = list()
      for keyword in keywords:
        keyword_occurrences.extend(soup.find_all(string=lambda text: keyword.lower() in text.lower()))

      print("keyword_occurrences; Type:", type(keyword_occurrences), "; Length:", len(keyword_occurrences))

      # Print or process the results
      count = 0
      occurances = list()
      if keyword_occurrences:
          #print(f"Keyword '{keywords}' found on the page:")
          for occurrence in keyword_occurrences:
            #print("Count", count, "; Occurrence Type:", type(occurrence))
            count+=1
            occurances.append(occurrence)
          #return (True, [1,2,3,4,5])
          return (True, occurances)
      else:
          print(f"Keyword '{keywords}' not found on the page.")
          return (False, [])
  else:
      print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
      return ('Invalid', response.status_code)