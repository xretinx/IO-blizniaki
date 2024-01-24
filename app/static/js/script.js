let breed;
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("dog-form");
  const resultDiv = document.getElementById("result");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    // Animacja znikania diva o klasie "form-group-wider"
    const formGroupWider = document.querySelector(".form-group-wider");
    formGroupWider.style.transition = "opacity 1s";
    formGroupWider.style.opacity = 0;

    const formGroupThinner = document.querySelector(".form-group-thinner");
    formGroupThinner.style.transition = "opacity 1s";
    formGroupThinner.style.opacity = 0;

    // Animacja znikania przycisków z klasą "custom-button"
    const customButtons = document.querySelectorAll(".custom-button");
    customButtons.forEach((button) => {
      button.style.transition = "opacity 1s";
      button.style.opacity = 0;
    });

    setTimeout(function () {
      const formData = new FormData(form);

      fetch("/find_dog_breed", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          breed = data.dog_breed;
          console.log(breed);
          formGroupWider.style.transition = "opacity 1s";
          formGroupWider.style.opacity = 1;
        });
    }, 0);

    console.log(breed);

    // Poczekaj 1 sekundę przed usunięciem zawartości diva
    setTimeout(function () {
      // Usuń zawartość diva o klasie "form-group-wider"
      formGroupWider.innerHTML = `<div class="loader">
      <span style="--i:1;" class="fa-solid fa-bone"></span>
      <span style="--i:2;" class="fa-solid fa-bone"></span>
      <span style="--i:3;" class="fa-solid fa-bone"></span>
      <span style="--i:4;" class="fa-solid fa-bone"></span>
      <span style="--i:5;" class="fa-solid fa-bone"></span>
      <span style="--i:6;" class="fa-solid fa-bone"></span>
      <span style="--i:7;" class="fa-solid fa-bone"></span>
      <span style="--i:8;" class="fa-solid fa-bone"></span>
      <span style="--i:9;" class="fa-solid fa-bone"></span>
      <span style="--i:10;" class="fa-solid fa-bone"></span>
      <span style="--i:11;" class="fa-solid fa-bone"></span>
      <span style="--i:12;" class="fa-solid fa-bone"></span>
      <span style="--i:13;" class="fa-solid fa-bone"></span>
      <span style="--i:14;" class="fa-solid fa-bone"></span>
      <span style="--i:15;" class="fa-solid fa-bone"></span>
      <span style="--i:16;" class="fa-solid fa-bone"></span>
      <span style="--i:17;" class="fa-solid fa-bone"></span>
      <span style="--i:18;" class="fa-solid fa-bone"></span>
      <span style="--i:19;" class="fa-solid fa-bone"></span>
      <span style="--i:20;" class="fa-solid fa-bone"></span>
  
    
  </div>`;

      // Wstaw zdjęcie uploaded-image
      //const uploadedImage = document.getElementById("uploaded-image");
      //formGroupWider.appendChild(uploadedImage);

      // Przywróć widoczność diva o klasie "form-group-wider"
      formGroupWider.style.transition = "opacity 1s, transform 1s";
      formGroupWider.style.opacity = 1;
      formGroupWider.style.transform = "scale(1)";

      setTimeout(function () {
        formGroupWider.style.transition = "opacity 1s, transform 1s";
        formGroupWider.style.opacity = 0;
        formGroupWider.style.transform = "scale(0.8)";
        formGroupWider.innerHTML = "";
      }, 3800);

      setTimeout(function () {
        formGroupWider.style.transition = "opacity 1s, transform 1s";
        formGroupWider.style.opacity = 1;
        formGroupWider.style.transform = "scale(1.2)";
      }, 4100);

      setTimeout(function () {
        formGroupWider.style.transition = "opacity 1s, transform 1s";
        formGroupWider.style.opacity = 0;
        formGroupWider.innerHTML = "";
      }, 4700);

      setTimeout(function () {
        resultDiv.innerHTML = `<i class="heading"> Most similar dog breed: ${breed}</i>`;

        formGroupWider.style.transition = "opacity 1s, transform 1s";
        formGroupWider.style.opacity = 1;
        formGroupWider.style.transform = "scale(1)";

        formGroupWider.innerHTML =
          '<img src="../static/images/Baza_reprezentacja/' +
          breed +
          '.jpg" alt="Your Image">';
      }, 5000);

      // Poczekaj 1 sekundę przed wysłaniem formularza
    }, 300);
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
