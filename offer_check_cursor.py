from import_libs import *
from discount_value_check_cursor import discount_value_check_cursor

def offer_check_cursor(result: list) -> tuple[bool, list]:
  """
  Expects a result of type list which consists of bs4.element, basically the scrapped text data.
  A sample example of result parameter containing value:
  Only invoke the regex pattern checker function if the each iterable's (bs4.element) from the result list length is smaller than 200 & the type of bs4.element is a 'NavigableString'.
  Only returns true if the regex pattern checker function is not 0 while maintaing the aforementioed conditional iteration.
  Returns a boolean value with the list of offers (empty or non-empty).
  """
  try:
    count=0
    has_offer = False
    offer_list = []
    for r in result[1]:
      if len(r) < 200 and type(r)==bs4.element.NavigableString:
        count+=1
        # Check for certain string pattern to determine if the website is providing any offer
        #print(r.strip())
        #print(type(r))
        #print(type(r.get_text()))
        #discount_value_check_cursor(r.get_text())
        if len(discount_value_check_cursor(r.get_text())) != 0:
          # print(discount_value_check_cursor(r.get_text()))
          offer_list.append(discount_value_check_cursor(r.get_text()))
          has_offer = True
        #print(r.get_text().strip().lower())
        #print(type(r))
        #print(type(r.string))
        #print(len(r.__dir__()))
        #for d in r.__dir__():
         # print(d)
        #break
        #print(type(r.string), isinstance(r, NS))  # Not satisfied
        #print(type(r.string), ('isNavigableString:', type(r)==bs4.element.NavigableString))  # Not satisfied
        #print(isinstance(r.string, NavigableString))
    print("Count Collections:", count)
    offer_set = set(offer_list)
    offer_list = list(offer_set)
    print("offer list:", len(offer_list))
    # If there is any offer available, only then send the boolean value with the offer list, else return a false boolean value with empty list
    if len(offer_list):
      # print("Store offers list using the method!")
      return has_offer, offer_list
    return has_offer, []
  except TypeError as te:
    print("TypeError:", te)
    return False, []