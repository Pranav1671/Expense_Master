


var copy = document.querySelector(".container521").cloneNode(true);
document.querySelector("#container52").appendChild(copy);



const toggleButtons = document.querySelectorAll('.toggleButton');

// Add event listener to each toggle button
toggleButtons.forEach(function(button, index) {
  button.addEventListener('click', function() {
    // Hide all hidden paragraphs and reset toggle buttons
    document.querySelectorAll('.hide').forEach(function(hiddenContent, i) {
      if (i !== index) {
        hiddenContent.style.display = 'none';
        const correspondingButton = toggleButtons[i];
        correspondingButton.textContent = '+';
        correspondingButton.classList.remove('minus');
      }
    });

    // Get the corresponding hidden paragraph
    const hiddenContent = document.querySelector('.hide' + (index + 1));

    // Toggle the display of the hidden paragraph
    if (hiddenContent.style.display === 'none' || hiddenContent.style.display === '') {
      // Show the hidden paragraph and update the button
      hiddenContent.style.display = 'block';
      button.textContent = '-';
      button.classList.add('minus'); // Add the 'minus' class
    } else {
      // Hide the hidden paragraph and update the button
      hiddenContent.style.display = 'none';
      button.textContent = '+';
      button.classList.remove('minus'); // Remove the 'minus' class
    }
  });
});



  // Function to scroll to container4 smoothly
  function scrollToContainer4(event) {
      event.preventDefault(); // Prevent default behavior of anchor tag
      var container4 = document.getElementById('container4'); // Get reference to container4 element
      container4.scrollIntoView({ behavior: 'smooth' }); // Scroll to container4 smoothly
  }

  // Add click event listener to the "Features" link
  var featuresLink = document.querySelector('a[href="#container4"]');
  featuresLink.addEventListener('click', scrollToContainer4);

  function scrollToContainer6(event) {
    event.preventDefault(); // Prevent default behavior of anchor tag
    var container6 = document.getElementById('container6'); // Get reference to container4 element
    container6.scrollIntoView({ behavior: 'smooth' }); // Scroll to container4 smoothly
}

// Add click event listener to the "Features" link
var featuresLink = document.querySelector('a[href="#container6"]');
featuresLink.addEventListener('click', scrollToContainer6);





  
function scrollToTop() {
  window.scrollTo({
      top: 0,
      behavior: 'smooth'
  });
}

// Show the button when the user scrolls down 20px from the top of the document
window.onscroll = function() { scrollFunction() };

function scrollFunction() {
  var scrollToTopBtn = document.getElementById("scrollToTopBtn");
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      scrollToTopBtn.style.display = "flex";
      scrollToTopBtn.style.right = "100px"; // Adjust as needed
  } else {
      scrollToTopBtn.style.display = "none";
  }
}