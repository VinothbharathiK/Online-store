const slider = document.querySelector('.slider');
let slides = Array.from(slider.children);
let totalSlides = slides.length;
const slideWidth = 100; // vw
let index = 1;
let autoSlideInterval;

// Clone first and last slides dynamically
const firstClone = slides[0].cloneNode(true);
const lastClone = slides[totalSlides - 1].cloneNode(true);

// Append clones
slider.appendChild(firstClone);
slider.insertBefore(lastClone, slides[0]);

// Update slides array
slides = Array.from(slider.children);
totalSlides = slides.length;

// Set initial position
slider.style.transform = `translateX(${-index * slideWidth}vw)`;

function updateSlide() {
    slider.style.transition = "transform 0.5s ease-in-out";
    slider.style.transform = `translateX(${-index * slideWidth}vw)`;
}

function nextSlide() {
    index++;
    updateSlide();

    setTimeout(() => {
        if (index >= totalSlides - 1) {
            slider.style.transition = "none";
            index = 1;
            slider.style.transform = `translateX(${-index * slideWidth}vw)`;
        }
    }, 500);

    resetAutoSlide();
}

function prevSlide() {
    index--;
    updateSlide();

    setTimeout(() => {
        if (index <= 0) {
            slider.style.transition = "none";
            index = totalSlides - 2;
            slider.style.transform = `translateX(${-index * slideWidth}vw)`;
        }
    }, 500);

    resetAutoSlide();
}

function startAutoSlide() {
    autoSlideInterval = setInterval(nextSlide, 3000);
}

function resetAutoSlide() {
    clearInterval(autoSlideInterval);
    startAutoSlide();
}

startAutoSlide();
