const header = document.querySelector('header');
const newHeader = document.querySelector('#update_header');
newHeader.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});