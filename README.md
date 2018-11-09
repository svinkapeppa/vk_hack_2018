# VK Hack 2018

Backend part of mobile app


## API

### Users

#### UserData

API provides two ways of communicating:
1. `/api/users/users/` accepts `POST` requests and designed to create `UserData` objects
2. `/api/users/users/{{id}}` accepts `GET`, `PATCH`, `PUT` requests and designed to retrieve and modify `UserData` objects
