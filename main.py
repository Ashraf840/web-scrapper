from scrapper import scrapper
from offer_check_cursor import offer_check_cursor
from find_max_offer import find_max_offer
from website_list import website_list   # Not required now, getting the list from POST method of the api externally
from import_libs import *

app = Flask(__name__) 

@app.route('/', methods = ['GET', 'POST']) 
def website_with_offer():
  if request.method == 'POST':
    print("This is a post method!")
    json_data = request.get_json()
    for req in request.__dir__():
      print(req)
    offer_result = {}
    website_list = json_data.get('website_list')
    if len(website_list) < 15:
      for wl in website_list:
        print(wl)
        result = scrapper(url=wl)
        check_offer = offer_check_cursor(result)
        if check_offer[0]:
          offer_result[wl] = find_max_offer(check_offer[1])
      return offer_result
    else:
      return jsonify("Maxed out! Please decrease the number of URL to 30")
      # break
  if request.method == 'GET':
    data = {'message': []}
    return jsonify(data)

# print(website_with_offer(website_list))

if __name__ == '__main__': 
    app.run(debug = False, host="0.0.0.0", port=8080)