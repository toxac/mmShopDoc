# Custom Pages 
-----

## Custom Pages with Accordion
We have already used accordion element in the product description section. We are goin to reuse the same element in the page to add accordion functionality.

**Important note about shopify themes**
Shopify themes are organized into ***templates*** > ***sections*** > ***snippets***. This organization is important to understand when we start to customize pages. Following points are important to remember.
- **templates** are top level component into which **sections** and **snippets** can be included/rendered.
- Sections cannot be rendered in another section
- Custom styles and javascript are available only in section through **liquid**
- When we include section in a template it has access to all the template variables/properties/attributes
- Its is good practice to define a custom section with dedicated schema, styles, and js behavior and include it into a custom template. This gives us bet of both worlds. Else we will have to included all the styles in global assets which can make it difficult to contain bugs and errors, if something were to go wrong.

### Creating duplicate page template
Keeping this in mind we are going to create a duplicate page template ***zdd_page.liquid*** which will show up on finder sidebar under template folder as ***page.zdd_page.liquid***. This template by default is as below

```html
<div class="page-width">
  <div class="grid">
    <div class="grid__item medium-up--five-sixths medium-up--push-one-twelfth">
      <div class="section-header text-center">
        <h1>{{ page.title }}</h1>
      </div>

      <div class="rte">
        {{ page.content }}
      </div>
    </div>
  </div>
</div>
```

We have modified the above template to include a new custom page section which renders the content. This gives us possibility of included custom styling alongwith the section.

### Custom Page Section
In this new custom section we only render the page content which will be filled in using standard page creation interface of Shopify. We will use this section to define custom style using ***{% stylesheet %}.... {% endstylesheet %}*** directive.
```js
// We render the page content through the section now
{{ page.content }}

{% schema %}
  {
    "name": "Section name",
    "settings": []
  }
{% endschema %}

{% stylesheet %}

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
	font-size: 1em;
  	font-weight: 600;
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

{% endstylesheet %}

{% javascript %}
{% endjavascript %}
```

### Including The New Section in Custom Page Template

```html
<div class="page-width">
  <div class="grid">
    <div class="grid__item medium-up--five-sixths medium-up--push-one-twelfth">
      <div class="section-header text-center">
        <h1>{{ page.title }}</h1>
      </div>

      <div class="rte">
        {% section 'zdd-page-template' %}
      </div>
    </div>
  </div>
</div>
```

### Add Content and Use HTML Editor While Creating Page