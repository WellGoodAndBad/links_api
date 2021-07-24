###### rest_api with redis db

запуск сервиса
- docker-compose build
- docker-compose up

####### get 
получение данных
 - GET /visited_domains?from=sometimestamp&to=sometimestamp
   
параметры "from", "to" обязательны, сервис проверят их наличие.

####### post 
отправка данных
 - POST /visited_links

тело запроса

{
"links": [
"https://ya.ru",
"https://ya.ru?q=123",
"funbox.ru",
"https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
]
}
   json должен передавать в таком виде, сервис проверяет наличие ключа "links", и наличие списка в значении этого ключа