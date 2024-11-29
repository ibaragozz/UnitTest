import pytest
from main import get_dog


def test_get_dog_success(mocker):
   mock_get = mocker.patch('mocingtest.requests.get')

   # Создаем мок-ответ для успешного запроса
   mock_get.return_value.status_code = 200
   mock_get.return_value.json.return_value = {
        "message": "https://images.dog.ceo/breeds/pyrenees/n02111500_1097.jpg",
        "status": "success"
}


   weather_data = get_weather(api_key, city)

   assert weather_data == {
        "message": "https://images.dog.ceo/breeds/pyrenees/n02111500_1097.jpg",
        "status": "success"
}

def test_get_weather_failure(mocker):
   mock_get = mocker.patch('main.requests.get')

   # Создаем мок-ответ для неуспешного запроса
   mock_get.return_value.status_code = 404

   api_key = 'test_api_key'
   city = 'UnknownCity'
   weather_data = get_weather(api_key, city)

   assert weather_data is None
