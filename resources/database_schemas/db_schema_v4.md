**Recipe**

```javascript
{
    name: '',
    time: {
        hours: Number,
        minutes: Number
    },
    author: UserId,
    description: '',
    ingredients: [''],
    method: [''],
    image_url: '',
    date_added: Date,
    favourites: Number,
    cuisine: '',
    type: ''
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
```