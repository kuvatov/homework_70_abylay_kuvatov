# homework_70_abylay_kuvatov

## superuser:

login: admin
password: root

## DB users:

login: Manager
password: Manager210323

login: Captain
password: Captain210323

login: Developer
password: Developer210323

## API:

Для проверки API можно воспользоваться программой **Postman**
##### Примечание: 
_Для проверки метода PUT, необходимо сначала получить данные определенной задачи/проекта, скопировать данные в окно BODY -> raw (JSON), затем внести изменения в необходимые поля и нажать на кнопку **Send**_

Ниже указаны методы и пути к API:

### Projects
#### detail
GET _hostname_/api/project/id
#### update
PUT _hostname_/api/project/id/update
#### delete
DELETE _hostname_/api/project/id/delete

### Issues
#### detail
GET _hostname_/api/issue/id
#### update
PUT _hostname_/api/issue/id/update
#### delete
DELETE _hostname_/api/issue/id/delete
