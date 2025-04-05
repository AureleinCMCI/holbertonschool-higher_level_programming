const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');
addItem.addEventListener('click', () => {
  const newElement = document.createElement('li');
  newElement.textContent = 'Item';
  myList.appendChild(newElement);
});