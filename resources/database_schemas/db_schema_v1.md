**Recipe**

```javascript
{
    name: '',
    time: {
        prep: '',
        cook: ''
},
    author: UserId,
    description: '',
    ingredients: [],
    method: [],
    image_url: '',
    date_added: Date,
    favourites: Number,
    country_of_origin: '',
    cuisine: ''
}
```

**User**

```javascript
{
    name: '',
    username: '',
    my_recipes: [RecipeId],
    favourite_recipes: [RecipeId]
}