# VK Hack 2018

Backend part of mobile app


## API

### Users

This applications provides you with models, views, etc. for working with users' data.

#### UserData

`UserData` contains following fields:
* `vk_id` - id of user at [vk.com](https://vk.com)
* `first_name` - first name of the user (taken from [vk.com](https://vk.com))
* `second_name` - last name of the user (taken from [vk.com](https://vk.com))
* `level` - level of the user
* `experience` - current experience of the user
* `coins` - users' coins
* `donated` - total values of users' donations

API provides three ways of communicating:
1. `/api/users/users/` accepts `POST` requests and designed to create `UserData` objects
2. `/api/users/users/{{id}}` accepts `GET`, `PATCH`, `PUT` requests and designed to retrieve and modify `UserData` objects
3. `/api/users/users/leaderboard` accepts `GET` requests and designed to show users in order, specified by `ordering` keyword,
which can either be `level` or `donated`
