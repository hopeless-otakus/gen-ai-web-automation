---
title: "Form"
draft: false
---

<form action="http://localhost:5000/submit" method="POST">
  <label for="title">Title:</label>
  <input type="text" id="title" name="title" required>
  <br>

  <label for="link">Link:</label>
  <input type="url" id="link" name="link" required>
  <br>

  <label for="image_url">Image URL:</label>
  <input type="url" id="image_url" name="image_url" required>
  <br>

  <button type="submit">Submit</button>
</form>
