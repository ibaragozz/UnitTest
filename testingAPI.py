import pytest
from mocingtest import get_dog


def test_get_dog_success(mocker):
   mock_get = mocker.patch('mocingtest.requests.get')

   # Создаем мок-ответ для успешного запроса
   mock_get.return_value.status_code = 200
   mock_get.return_value.json.return_value = {
        "message": "https://images.dog.ceo/breeds/pyrenees/n02111500_1097.jpg",
        "status": "success"
}


   dog_picture = get_dog()

   assert dog_picture == {
        "message": "https://images.dog.ceo/breeds/pyrenees/n02111500_1097.jpg",
        "status": "success"
}

def test_get_weather_failure(mocker):
   mock_get = mocker.patch('mocingtest.requests.get')

   # Создаем мок-ответ для неуспешного запроса
   mock_get.return_value.status_code = 404

   dog_picture = get_dog()

   assert dog_picture is None
