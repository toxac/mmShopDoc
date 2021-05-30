# Product Pages
----

## Displaying Product Tags
Displaying product tags below the product title to give customer a quick overview of most important features of the product. These Tags also have links to all products with similat tags when clicked. 

### Step 1: Custominzing Template Code
A duplicate of ***"Product template"*** is created in Template folder which renders a section for ***product*** and ***product-recommendation*** right on the top of the file. 

```js
{% section 'product-template' %}
{% section 'product-recommendations' %}
```

We have replaced the original section with a new one called ***zdd-product-template***. We don't really want to mess with the original theme files. All the custom additions in the form of files, styles, assets etc will have prefix of ***zdd** to it. This makes it easy to identify them.

```js
{% section 'zdd-product-template' %}
{% section 'product-recommendations' %}
```

To the new section we have added a piece of code to first fetch all the tags for a given product and them display them as *pills*. In the code below, the custom ***div*** for tags is placed right below the ***product.title*** which is an <h1> element.

```html
<div class="product-single__meta">
    <h1 class="product-single__title">{{ product.title }}</h1>
    <!-- Custom Block for Tags (Amit)   -->
    <div class="zdd-tag-block">
        {% for tag in product.tags %}
            <a class="zdd-tag-pill" href="/collections/all/{{ tag | handleize }}">{{ tag }}</a>
        {% endfor %}
    </div>
```
#### Explanation
- Liquid code ***{% for tag in product.tags %}*** : Gets all the tags for the product and iterates over it (for loop)
- Anchor tag <a>..</a>: We are using achor tags to display each of the tags which is linked to collection page by tag.
- Styles (***zdd-tag-block*** and ***zdd-tag-pill***): Tag block is to ensure spacing and layout positioning of the block while tag-pill styles the anchor tags to display as pills. The css codes for both are below. 

```css
.zdd-tag-block {
	margin-bottom: 20px;
}

.zdd-tag-pill {
  background-color: #ddd;
  border: none;
  color: black;
  padding: 5px 8px;
  text-align: center;
  font-size: .9em;
  text-decoration: none;
  display: inline-block;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 16px;
}
```





