document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("dog-form");
  const resultDiv = document.getElementById("result");

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(form);

    fetch("/find_dog_breed", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        resultDiv.innerHTML = `Most similar dog breed: ${data.dog_breed}`;
      });
  });
  const fileInput = document.getElementById("file-input");
  const fileNameLabel = document.getElementById("file-name-label");
  const uploadedImage = document.getElementById("uploaded-image");

  fileInput.addEventListener("change", function () {
    if (fileInput.files.length > 0) {
      fileNameLabel.textContent = fileInput.files[0].name;

      // Display the selected image
      const reader = new FileReader();
      reader.onload = function (e) {
        uploadedImage.src = e.target.result;
        uploadedImage.style.display = "block";
      };
      reader.readAsDataURL(fileInput.files[0]);
    } else {
      fileNameLabel.textContent = "No file chosen";
      uploadedImage.style.display = "none";
    }
  });
});
