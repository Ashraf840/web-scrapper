def find_max_offer(offer_list: list) -> tuple:
  """
  Find the max tuple element from a list of tuples containing [('10% off', '10'), ('20% off', '20')] in this form.
  """
  print("Find the max valued offer!")
  max_offer = max(offer_list, key=lambda x: int(x[1]))
  return max_offer