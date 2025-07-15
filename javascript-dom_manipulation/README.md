# JavaScript DOM Manipulation

This project demonstrates various JavaScript DOM manipulation techniques through practical examples.

## Learning Objectives

- How to select HTML elements in JavaScript
- What are differences between ID, class and tag name selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a request with XmlHTTPRequest
- How to make a request with Fetch API
- How to listen/bind to DOM events
- How to listen/bind to user events

## Files and Examples

### 0-script.js - Basic Element Selection and Style Modification
```javascript
document.querySelector('header').style.color = '#FF0000';
```
- **Concept**: Selecting elements by tag name and modifying CSS properties
- **Method**: `document.querySelector()` with tag selector
- **Action**: Direct style modification using `.style` property

### 1-script.js - Event Listeners and Click Events
```javascript
document.querySelector('#red_header').addEventListener('click', function() {
    document.querySelector('header').style.color = '#FF0000';
});
```
- **Concept**: ID selectors and event binding
- **Method**: `document.querySelector('#id')` for ID selection
- **Action**: Adding click event listeners with `addEventListener()`

### 2-script.js - CSS Class Manipulation
```javascript
document.querySelector('#red_header').addEventListener('click', function() {
    document.querySelector('header').classList.add('red');
});
```
- **Concept**: Adding CSS classes instead of direct style modification
- **Method**: `classList.add()` for class manipulation
- **Advantage**: Better separation of concerns (CSS vs JavaScript)

### 3-script.js - Advanced Class Toggling
```javascript
document.querySelector('#toggle_header').addEventListener('click', function() {
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
});
```
- **Concept**: Conditional class switching and state management
- **Methods**: `classList.contains()`, `classList.remove()`, `classList.add()`
- **Logic**: Toggle between two mutually exclusive states

### 4-script.js - DOM Element Creation and Insertion
```javascript
document.querySelector('#add_item').addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newItem);
});
```
- **Concept**: Creating new DOM elements and adding them to existing elements
- **Methods**: `document.createElement()`, `appendChild()`
- **Selector**: Class selector using `.className`

### 5-script.js - Text Content Modification
```javascript
document.querySelector('#update_header').addEventListener('click', function() {
    document.querySelector('header').textContent = 'New Header!!!';
});
```
- **Concept**: Updating element text content
- **Method**: `textContent` property for safe text insertion
- **Note**: `textContent` vs `innerHTML` - safer for plain text

### 6-script.js - Fetch API for HTTP Requests
```javascript
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
        document.querySelector('#character').textContent = data.name;
    });
```
- **Concept**: Making HTTP requests with modern Fetch API
- **Methods**: `fetch()`, Promise chaining with `.then()`
- **Action**: Displaying API data in DOM elements

### 7-script.js - Dynamic List Generation from API
```javascript
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        const moviesList = document.querySelector('#list_movies');
        data.results.forEach(movie => {
            const listItem = document.createElement('li');
            listItem.textContent = movie.title;
            moviesList.appendChild(listItem);
        });
    });
```
- **Concept**: Processing API arrays and creating multiple DOM elements
- **Methods**: `forEach()` iteration, dynamic element creation
- **Pattern**: Common pattern for displaying lists from API data

### 8-script.js - DOM Ready Events and Script Loading
```javascript
document.addEventListener('DOMContentLoaded', function() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json())
        .then(data => {
            document.querySelector('#hello').textContent = data.hello;
        });
});
```
- **Concept**: Ensuring DOM is ready before script execution
- **Event**: `DOMContentLoaded` for scripts in `<head>`
- **Use Case**: When scripts load before HTML elements are rendered

## Key Concepts Summary

### Element Selectors
- **Tag selector**: `document.querySelector('header')`
- **ID selector**: `document.querySelector('#red_header')`
- **Class selector**: `document.querySelector('.my_list')`

### DOM Manipulation Methods
- **Style**: `element.style.property = 'value'`
- **Classes**: `element.classList.add/remove/contains()`
- **Content**: `element.textContent = 'text'`
- **Creation**: `document.createElement('tagname')`
- **Insertion**: `parent.appendChild(child)`

### Event Handling
- **Click events**: `element.addEventListener('click', function)`
- **DOM ready**: `document.addEventListener('DOMContentLoaded', function)`

### HTTP Requests
- **Fetch API**: Modern promise-based approach
- **JSON parsing**: `response.json()` method
- **Promise chaining**: `.then()` for handling responses

## Testing
Each script can be tested with its corresponding HTML file (0-main.html through 8-main.html) by opening in a web browser.