---
title: "Form"
draft: false
---

<form id="submissionForm" action="http://127.0.0.1:5000/submit" method="POST">
  <label for="title">Title:</label>
  <input type="text" id="title" name="title" required>
  <br>

  <label for="link">Link:</label>
  <input type="text" id="link" name="link" required>
  <br>

  <label for="image_url">Image URL:</label>
  <input type="text" id="image_url" name="image_url" required>
  <br>

  <button type="submit">Submit</button>
</form>

<script>
document.getElementById('submissionForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the default form submission

  const formData = new FormData(this); // Create a FormData object from the form

  fetch(this.action, {
    method: this.method,
    body: formData,
  })
  .then(response => {
    if (response.ok) {
      return console.log("worked"); // Assuming the backend responds with JSON
    }
    throw new Error('Network response was not ok.');
  })
  .then(data => {
    alert(data.message); // Show success message
  })
  .catch((error) => {
    console.error('Error:', error);
    alert('There was a problem with your submission.');
  });
});
</script>