from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request ):
    if request.method== 'POST':
        city = request.POST['city']
        api_key = '37502c657242b0a47a4fe6017c74d6bc'  # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        
        try:  
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
               result = response.read()
               json_data = json.loads(result)
            data = {
              "country_code": str(json_data['sys']['country']),
              "coordinate":str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
              "temp":str((json_data['main']['temp']))+ ' k',
              "pressure":str(json_data['main']['pressure']),
              "humidity":str(json_data['main']['humidity']),
              }
        
            return render(request, 'index.html', {'data': data})  # Pass 'data' dictionary to the template context
        except HTTPError as e:
             error_message = f"Error: {e.code} - {e.reason}"
             print(error_message)
             return render(request, 'index.html', {'error_message': error_message})
    else:
        return render(request, 'index.html', {'data': {}})  # Pass an empty dictionary if no data is available

