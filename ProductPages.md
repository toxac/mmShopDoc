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

To the new section we have added a piece of code to first fetch all the tags for a given product and them display them as *pills*. In the code below, the custom ***div*** for tags is placed right below the ***product.title*** which is an ***h1*** element.

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
- Anchor tag <a>..</a>: We are using anchor tags to display each of the tags which is linked to collection page by tag.
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
## Adding Product Brief Summary below Title

This has been implemented by manually hardcoding the summary to the product-section file. Which means we have created a template for each product at the present. This will be be standardized once we settle on sections for each product. This is what most of the page-builders also end up doing under the hood.
```html
<div class="product-single__meta">
    <h1 class="product-single__title">{{ product.title }}</h1>
    <!-- Custom Block for Tags (Amit)   -->
    <div class="zdd-tag-block">
        {% for tag in product.tags %}
          	<a class="zdd-tag-pill" href="/collections/all/{{ tag | handleize }}">{{ tag }}</a>
        {% endfor %}
        
    </div>
    <p>
        Product summary text would be added here along with some styling depending on the overall font and color schemes
    </p>
    <!-- End Custom Block for Tags (Amit)   -->
    ...
```
## Accordion for Product Details
Ideas is to remove the information density from the product pages by hiding them using accordion. So users can click of the information they need. Below is an example of one such accordion.

![Acordion Example](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fbd%2F1f%2F5f%2Fbd1f5f8644226704558c3513c720601b.gif&f=1&nofb=1)


### Implementing Pure CSS Accordion 
Accordion instead of using the popular option of jquery based behaviour we are going with Pure CSS. This minimizes the dependencies and additional file downloads.

### HTML CODE
We are using ***hidden radio input*** to give us access to the event of someone clicking on the tab. 

```html
<!--Main Container element for Accordion-->
<div class="zdd-product-accordion">
    <!-- Accordion Element -->
    <div> 
        <input type="radio" name="zdd_accordion" id="section1" class="zdd_accordion__input">
        <label for="section1" class="zdd_accordion__label">Description</label>
        <div class="zdd_accordion__content">
            <ul>
                <li>Premium 100% Natural Latex</li>
                <li>Naturally Breathable and Naturally Cooling</li>
                <li>Eco-friendly, Free From Harmful Chemicals</li>
                <li>High Bounceback and Resilience</li>
                <li>Highly Durable</li>
                <li>Naturally Hypoallergenic</li>
                <li>Anti-bacterial and Anti-fungal</li>
                <li>Dust Mite Resistant</li>
                <li>Innercore Technology</li>
                <li>7 Years warranty</li>
            </ul>
        </div>
    </div>

    <div>
        <input type="radio" name="zdd_accordion" id="section2" class="zdd_accordion__input">
        <label for="section2" class="zdd_accordion__label">Section #2</label>
        <div class="zdd_accordion__content">
            <ul>
                <li>product Dimensions:&nbsp;65 x 42.5 x 16 cm</li>
                <li>Primary Material: Natural Latex Foam Rubber</li>
                <li>Number of Pieces: 1</li>
                <li>Shipping Weight: 2.5 Kilograms</li>
            </ul>
        </div>
    </div>

    <div>
        <input type="radio" name="zdd_accordion" id="section3" class="zdd_accordion__input">
        <label for="section3" class="zdd_accordion__label">Section #3</label>
        <div class="zdd_accordion__content">
            <ul>
                <li>product Dimensions:&nbsp;65 x 42.5 x 16 cm</li>
                <li>Primary Material: Natural Latex Foam Rubber</li>
                <li>Number of Pieces: 1</li>
                <li>Shipping Weight: 2.5 Kilograms</li>
            </ul>
        </div>
    </div>

</div>
```
This product html is not actually manually inserted in to the template but we use the existing ***product page > description*** to add the code and then style it through the templates.

### CSS styles take care of the dropdowns.

```css
.zdd-product-accordion {
  	width: 100%;
	margin: 0;
  	overflow: hidden;
}

.zdd_accordion__label,
.zdd_accordion__content {
	width: 100%;  
	padding: 14px 20px;
}

.zdd_accordion__label {
  	display: block;
  	color: #474747;
	font-size: 1.5em;
  	font-weight: 500;
  	cursor: pointer;
  	position: relative;
  	transition: background 0.1s;
}

.zdd_accordion__label:hover {
  background: rgba(0, 0, 0, 0.1);
}

.zdd_accordion__label::after {
  content: "";
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  right: 20px;
  width: 12px;
  height: 6px;
  background-image: url('data:image/svg+xml;utf8,<svg width="100" height="50" xmlns="http://www.w3.org/2000/svg"><polygon points="0,0 100,0 50,50" style="fill:%2300000099;" /></svg>');
  background-size: contain;
  transition: transform 0.4s;
}

.zdd_accordion__content {
  background: #ffffff;
  line-height: 1.6;
  font-size: 1em;
  display: none;
}

.zdd_accordion__input {
  display: none;
}

.zdd_accordion__input:checked ~ .zdd_accordion__content {
  display: block;
}

.zdd_accordion__input:checked ~ .zdd_accordion__label::after {
  transform: translateY(-50%) rotate(0.5turn);
}
```

This custom css is added to the custom product section using the shopify liquid based functionality for adding template level css. 

```js
// add to the bottom of the custom section file 
{% stylesheet %}
    // All the custom styles can be copied in here
{% endstylesheet %}

```

## Image Grid

By default shopify/debut theme has a simple product page layout.


