document.addEventListener('DOMContentLoaded', function () {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.3 // 30% from the top
    };

    const observerCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-underline');
                observer.unobserve(entry.target); // Stop observing after animation is triggered
            }
        });
    };

    const observer = new IntersectionObserver(observerCallback, observerOptions);

    const target = document.querySelector('.underline-text');
    if (target) {
        observer.observe(target);
    }
});

window.addEventListener("load", function () {
    // Get the preloader element
    var preloader = document.getElementById('preloader');
    // Hide the preloader
    preloader.style.display = 'none';
    // if (window.innerWidth > 768) {
    AOS.init({
        once: true
    });
    // };
});



document.addEventListener('DOMContentLoaded', function () {
    new Splide('#image-slider', {
        type: 'loop',
        perPage: 3,
        perMove: 1,
        gap: '1rem',
        pagination: false,
        focus: 'center',
        padding: {
            left: '5%',
            right: '5%',
        },
        breakpoints: {
            1024: {
                perPage: 1,
                height: 800,
                padding: {
                    left: '10%',
                    right: '10%',
                },
            },
            768: {
                perPage: 1,
                height: 600,
                padding: {
                    left: '12px',
                    right: '12px',
                },
                // width: auto,
            },
            640: {
                perPage: 1,
                gap: '0.5rem',
                height: 400,

            },
        },
    }).mount();
});

const header = document.getElementById("header");
const cta = document.getElementById("cta-light");
const ctaAccent = document.getElementById("cta-white");
const langSelector = document.getElementById("lang-select");

const productsLink = document.getElementById("product-link");
const productDropdown = document.getElementById("product-dropdown");

const industryLink = document.getElementById("industry-link");
const industryDropdown = document.getElementById("industry-dropdown");

const navLinks = document.querySelector(".navlinks");

const logoLight = document.getElementById("logo-light");
const logoDark = document.getElementById("logo-dark");
const logoSize = document.getElementById("logoanchor");

const mobileMenu = document.getElementById("mobile-menu");
const mobileMenuBtn = document.getElementById("mobile-menu-btn");

const mobileProductLink = document.getElementById("mobile-product-link");
const mobileProductWrapper = document.getElementById("mobile-product-link-wrapper");
const mobileProductDropdown = document.getElementById("mobile-product-dropdown");

const mobileIndustryLink = document.getElementById("mobile-industry-link");
const mobileIndustryWrapper = document.getElementById("mobile-industry-link-wrapper");
const mobileIndustryDropdown = document.getElementById("mobile-industry-dropdown");

const whatsappBtn = document.getElementById("whatsapp-btn");

const isHomePage = window.location.pathname === "/"; // Check for homepage URL

let dropdownActive = false;
let mobileMenuActive = false;

function isHomepage() {
    return window.location.pathname === "/" || window.location.pathname === "/index.html";
}

// Show dropdown on hover
productsLink.addEventListener("mouseover", () => {
    productDropdown.classList.remove("hidden", "h-0");
    productDropdown.classList.add("flex");
    industryDropdown.classList.add("hidden", "h-0");
    dropdownActive = true;
    updateHeader();
});

productsLink.addEventListener("mouseout", () => {
    productDropdown.classList.remove("flex");
    productDropdown.classList.add("hidden", "h-0");
    dropdownActive = false;
    updateHeader();
});

// Keep dropdown visible when hovering over it
productDropdown.addEventListener("mouseover", () => {
    productDropdown.classList.remove("hidden", "h-0");
    productDropdown.classList.add("flex");
    dropdownActive = true;
    updateHeader();
});

// Hide dropdown on mouseout
productDropdown.addEventListener("mouseout", () => {
    productDropdown.classList.remove("flex");
    productDropdown.classList.add("hidden", "h-0");
    dropdownActive = false;
    updateHeader();
});

industryLink.addEventListener("mouseover", () => {
    industryDropdown.classList.remove("hidden", "h-0");
    industryDropdown.classList.add("flex");
    productDropdown.classList.add("hidden", "h-0");
    dropdownActive = true;
    updateHeader();
});
industryLink.addEventListener("mouseout", () => {
    industryDropdown.classList.remove("flex");
    industryDropdown.classList.add("hidden", "h-0");
    dropdownActive = false;
    updateHeader();
});

// Keep dropdown visible when hovering over it
industryDropdown.addEventListener("mouseover", () => {
    industryDropdown.classList.remove("hidden", "h-0");
    industryDropdown.classList.add("flex");
    dropdownActive = true;
    updateHeader();
});

// Hide dropdown on mouseout
industryDropdown.addEventListener("mouseout", () => {
    industryDropdown.classList.remove("flex");
    industryDropdown.classList.add("hidden", "h-0");
    dropdownActive = false;
    updateHeader();
});

mobileMenuBtn.addEventListener("click", () => {
    document.getElementById("open-menu-icon").classList.toggle("hidden");
    document.getElementById("closed-menu-icon").classList.toggle("hidden");
    mobileMenu.classList.toggle("hidden");
    mobileMenuActive = !mobileMenuActive;
    updateHeader();
});

mobileProductLink.addEventListener("click", (e) => {
    e.preventDefault();
    mobileProductDropdown.classList.toggle("hidden");
    mobileProductWrapper.classList.toggle("bg-accentLight");
    mobileProductLink.classList.toggle("text-yellow-500");

    mobileIndustryDropdown.classList.add("hidden");
    mobileIndustryWrapper.classList.remove("bg-gray-400");
});

mobileIndustryLink.addEventListener("click", (e) => {
    e.preventDefault();
    mobileIndustryDropdown.classList.toggle("hidden");
    mobileIndustryWrapper.classList.toggle("bg-gray-400");
    mobileIndustryLink.classList.toggle("text-yellow-500");

    mobileProductDropdown.classList.add("hidden");
    mobileProductWrapper.classList.remove("bg-gray-400");
});
// Update header on scroll
window.addEventListener("scroll", updateHeader);
// Function to check if the current page is the homepage
function isHomepage() {
    return window.location.pathname === "/" || window.location.pathname === "/index.html";
}

function applyScrolledHeaderStyles() {
    whatsappBtn.classList.remove("hidden");
    whatsappBtn.classList.add("fixed");
    header.classList.remove(
        "bg-transparent",
        "text-white",
        "border-b",
        // "lg:h-18"
    );
    header.classList.add(
        "bg-white",
        // "shadow-md",
        // "shadow-shadow",
    );

    langSelector.classList.add("text-black");
    langSelector.classList.remove("text-white");

    navLinks.classList.add("text-black");
    cta.classList.remove("border-white", "text-white");
    ctaAccent.classList.remove("bg-white", "text-black", "hover:bg-yellow-500", "hover:text-white");
    ctaAccent.classList.add("bg-yellow-500", "text-white", "hover:bg-white", "hover:border-black", "hover:border", "hover:text-yellow-500");
    cta.classList.add(
        "border-yellow-500",
        "text-black",
        "hover:bg-yellow-500",
        "hover:text-black"
    );
    // logoSize.classList.remove("h-[35px]", "md:h-[64px]", "xl:h-[96px]");
    // logoSize.classList.add("h-[32px]", "md:h-[60px]", "xl:h-[64px]");
    logoLight.classList.add("hidden");
    logoDark.classList.remove("hidden");
}

function applyInitialHeaderStyles() {
    if (isHomepage()) {
        header.classList.add("text-white", "backdrop-blur-md")
        logoLight.classList.remove("hidden");
        logoDark.classList.add("hidden");
        navLinks.classList.remove("text-black");

        whatsappBtn.classList.add("hidden");
        whatsappBtn.classList.remove("fixed");
        cta.classList.remove(
            "border-yellow-500",
            "text-yellow-500",
            "hover:bg-yellow-500",
            "hover:text-white"
        );
        cta.classList.add("border-white", "text-white");
        langSelector.classList.remove("text-black");
        langSelector.classList.add("text-white");
    } else {
        logoLight.classList.add("hidden");
        logoDark.classList.remove("hidden");
        cta.classList.remove(
            "border-yellow-500",
            "text-yellow-500",
            "hover:bg-yellow-500",
            "hover:text-white"
        );
        cta.classList.add("border-black", "text-black");
        document.getElementById("lang-select").classList.add("text-black")
    }

    header.classList.remove(
        "bg-white",
        // "shadow-sm",
        // "shadow-shadow",
        // "lg:h-22"
    );
    header.classList.add(
        "bg-transparent",
        // "text-white",
        "border-b",
        // "lg:h-24"
    );

    ctaAccent.classList.remove("bg-yellow-500", "text-white", "hover:bg-white", "hover:border-black", "hover:border", "hover:text-yellow-500");
    ctaAccent.classList.add("bg-white", "text-black");

    // logoSize.classList.remove("h-[32px]", "md:h-[60px]", "xl:h-[64px]");
    // logoSize.classList.add("h-[35px]", "md:h-[64px]", "xl:h-[96px]");
}

function changeLogoSize(str) {
    if (str === 'decrease') {
        logoSize.classList.remove("h-[35px]", "md:h-[64px]", "xl:h-[96px]");
        logoSize.classList.add("h-[32px]", "md:h-[60px]", "xl:h-[64px]");

    } else if (str === 'increase') {
        logoSize.classList.remove("h-[32px]", "md:h-[60px]", "xl:h-[64px]");
        logoSize.classList.add("h-[35px]", "md:h-[64px]", "xl:h-[96px]");

    }
}


applyInitialHeaderStyles();
// Update header on scroll
window.addEventListener("scroll", updateHeader);

function updateHeader() {
    const scrollY = window.scrollY;

    if (scrollY > 50 || dropdownActive || mobileMenuActive) {
        applyScrolledHeaderStyles();
    } else {
        applyInitialHeaderStyles();
    }
}

// newsletter 
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('newsletter-form');
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(form);
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(form.action, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                    },
                    body: formData,
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Parsed data:', data); // Log the parsed data
                    const messagesDiv = form.querySelector('.form-messages');
                    if (messagesDiv) {
                        if (data.success) {
                            messagesDiv.innerHTML = '<p>' + data.message + '</p>';
                            form.reset();
                        } else {
                            let errorMessage = '<p>Error: Unknown error</p>';
                            if (data.errors && data.errors.email && data.errors.email.length > 0) {
                                errorMessage = '<p>Error: ' + data.errors.email[0].message + '</p>';
                            }
                            messagesDiv.innerHTML = errorMessage;
                        }
                    } else {
                        console.error('Element with class .form-messages not found in the form.');
                    }
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                    const messagesDiv = form.querySelector('.form-messages');
                    if (messagesDiv) {
                        messagesDiv.innerHTML = '<p>Error: ' + error.message + '</p>';
                    }
                });
        });
    } else {
        console.error('Form with id newsletter-form not found.');
    }

    // lazy loading
    const lazyLoadMedia = document.querySelectorAll('.lazy');

    if ('IntersectionObserver' in window) {
        let lazyMediaObserver = new IntersectionObserver(function (entries, observer) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    let lazyMedia = entry.target;

                    if (lazyMedia.tagName === 'IMG') {
                        lazyMedia.src = lazyMedia.dataset.src;
                        lazyMedia.onload = function () {
                            lazyMedia.classList.add('loaded');
                        };
                    } else if (lazyMedia.tagName === 'VIDEO') {
                        lazyMedia.src = lazyMedia.dataset.src;
                        lazyMedia.onloadeddata = function () {
                            lazyMedia.classList.add('loaded');
                        };
                    }

                    lazyMediaObserver.unobserve(lazyMedia);
                }
            });
        });

        lazyLoadMedia.forEach(function (lazyMedia) {
            lazyMediaObserver.observe(lazyMedia);
        });
    } else {
        // Fallback for older browsers
        lazyLoadMedia.forEach(function (lazyMedia) {
            if (lazyMedia.tagName === 'IMG') {
                lazyMedia.src = lazyMedia.dataset.src;
                lazyMedia.onload = function () {
                    lazyMedia.classList.add('loaded');
                };
            } else if (lazyMedia.tagName === 'VIDEO') {
                lazyMedia.src = lazyMedia.dataset.src;
                lazyMedia.onloadeddata = function () {
                    lazyMedia.classList.add('loaded');
                };
            }
        });
    }
});


document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll('.solution-banner');
    let current = 0;

    function changeImage() {
        images[current].classList.remove('active');
        console.log(current)
        current = (current + 1) % images.length;
        console.log(current)
        
        images[current].classList.add('active');
        console.log('image changed')
    }

    setInterval(changeImage, 3000); // Change image every 3 seconds
});



// agri-drone page