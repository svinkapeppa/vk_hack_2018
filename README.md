# VK Hack 2018

Backend part of mobile app

## API

Here are some tips to get you started with the backend of the app.

### Map

This application provides you with models, views, etc. for working with different objects, related to pets,
e.g. grooming salons, cash boxes, etc.

#### PetPoint

`PetPoint` contains following fields:
* `name` - name of the point
* `type` - one of the point types (see [constants](app/map/constants.py) for better understanding)
* `address` - string, which contains full address of the point
* `location` - contains address as `lon/lat` pair (see [this](app/utils/fields.py) for better understanding)
* `site` - website of the point 
* `extra` - any additional information, that can be useful

API provides one way of communicating:
1. `/api/map/map/` accepts `GET` requests and designed to list and retrieves `PetPoint` objects;
in order to retrieve some particular object specify its `{{id}}`;
also it is possible to filter results by `type`

### Pets

This application provides you with models, views, etc. for working with animal shelter's pets.

#### Pet

`Pet` contains following fields:
* `name` - name of the pet
* `type` - one of the pet types (see [constants](app/map/constants.py) for better understanding)
* `photo` - photo of the pet (see [this](app/utils/fields.py) for better understanding)

API provides one wat of communicating:
1. `/api/map/map/` accepts `GET` requests and designed to list and retrieves `PetPoint` objects;
in order to retrieve some particular object specify its `{{id}}`;
also it is possible to filter results by `type`

### Users

This application provides you with models, views, etc. for working with users' data.

#### UserData

`UserData` contains following fields:
* `vk_id` - id of user at [vk.com](https://vk.com)
* `photo` - link to users' photo (see [this](app/utils/fields.py) for better understanding)
* `first_name` - first name of the user (taken from [vk.com](https://vk.com))
* `second_name` - last name of the user (taken from [vk.com](https://vk.com))
* `level` - level of the user
* `experience` - current experience of the user
* `coins` - users' coins
* `donated` - total values of users' donations

API provides three ways of communicating:
1. `/api/users/users/` accepts `POST` requests and designed to create `UserData` objects
2. `/api/users/users/{{id}}` accepts `GET`, `PATCH`,
`PUT` requests and designed to retrieve and modify `UserData` objects
3. `/api/users/users/leaderboard` accepts `GET` requests and designed to show users in order,
specified by `ordering` keyword, which can either be `level` or `donated`
