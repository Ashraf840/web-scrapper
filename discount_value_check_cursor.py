from import_libs import *

def discount_value_check_cursor(val: str) -> tuple:
  """
  Find the value of "x% off" from each "bs4.element.NavigableString". Lastly, returns 
  """
  #print("discount_value_check_cursor (type):", type(val))
  #single_string = "UP TO 90% OFF"
  #pattern = re.compile(r'(\d?\d{2})(\W+\w+)')
  #pattern = re.compile(r'(\d?\d{2})(\W+(off))')
  pattern = re.compile(r'(\d?\d{2})(.*?off)', re.IGNORECASE)  # Polished regex pattern
  result = re.search(pattern, val)
  if result is not None:
    # print("discount_value_check_cursor - result.group(0):", result.group(0))
    # print("discount_value_check_cursor - result.group(1):", result.group(1))
    # print("discount_value_check_cursor - result.group(2):", result.group(2))
    return (result.group(0).lower(), result.group(1))
  else:
    return ()