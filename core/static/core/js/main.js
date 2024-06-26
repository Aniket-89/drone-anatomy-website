AOS.init({
    once: true
});

// function setupScrollTriggerAnimation() {
//     if (window.innerWidth >= 1024) { // Change 1024 to your desired screen width
//         gsap.registerPlugin(ScrollTrigger);

//         gsap.utils.toArray(".panel").forEach((panel, i) => {
//             ScrollTrigger.create({
//                 trigger: panel,
//                 start: "top top",
//                 end: "+=500",
//                 pin: true,
//                 pinSpacing: false,
//                 scrub: 1
//             });
//         });

//         gsap.to(".scale-up-video", {
//             scrollTrigger: {
//                 trigger: ".scale-up-video",
//                 start: "top 50%",

//                 toggleActions: "play none reverse none",
//             },
//             scale: 1, // Final scale value
//             duration: 1
//         });

//     }
// }

// setupScrollTriggerAnimation();
// window.addEventListener('resize', function() {
//     setupScrollTriggerAnimation();
// });


document.addEventListener('DOMContentLoaded', function () {
    new Splide('#image-slider', {
        type: 'loop',
        perPage: 1,
        perMove: 1,
        gap: '1rem',

        focus: 'center',
        padding: {
            left: '25%',
            right: '25%',
        },
        breakpoints: {
            1024: {
                perPage: 1,
                padding: {
                    left: '10%',
                    right: '10%',
                },
            },
            768: {
                perPage: 1,
                height: 400,
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
    mobileProductWrapper.classList.toggle("bg-gray-400");
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
// window.addEventListener("scroll", updateHeader);
// Function to check if the current page is the homepage
function isHomepage() {
    return window.location.pathname === "/" || window.location.pathname === "/index.html";
}

function applyScrolledHeaderStyles() {
    whatsappBtn.classList.remove("hidden");
    whatsappBtn.classList.add("fixed");
    header.classList.add(
        "bg-white",
        // "shadow-md",
        // "shadow-shadow",
    );

    header.classList.remove(
        "bg-transparent",
        "text-white",
        "border-b",
        // "lg:h-18"
    );
    navLinks.classList.add("text-black");
    cta.classList.remove("border-white", "text-white");
    ctaAccent.classList.remove("bg-white");
    ctaAccent.classList.add("bg-yellow-500");
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
    whatsappBtn.classList.add("hidden");
    whatsappBtn.classList.remove("fixed");
    header.classList.remove(
        "bg-white",
        // "shadow-md",
        // "shadow-shadow",
        // "lg:h-22"
    );
    header.classList.add(
        "bg-transparent",
        "text-white",
        "border-b",
        // "lg:h-24"
    );
    cta.classList.remove(
        "border-yellow-500",
        "text-yellow-500",
        "hover:bg-yellow-500",
        "hover:text-white"
    );
    cta.classList.add("border-white", "text-white");
    ctaAccent.classList.remove("bg-yellow-500");
    ctaAccent.classList.add("bg-white");
    navLinks.classList.remove("text-black");
    logoLight.classList.remove("hidden");
    logoDark.classList.add("hidden");
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

if (isHomepage()) {
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

    // Initial check
    updateHeader();

} else {
    // Apply scrolled header styles by default for all other pages
    applyScrolledHeaderStyles();
    // changeLogoSize('increase')


    
}



// counter

function createCounter(elementId, targetNumber, duration = 1000, onUpdate) {
    const counterElement = document.getElementById(elementId);

    if (!counterElement) {
        throw new Error(`Element with ID "${elementId}" not found!`);
    }

    let currentCount = Number(counterElement.textContent) || 0; // Get initial count or set to 0

    const increment = Math.ceil((targetNumber - currentCount) / (duration / 10)); // Calculate increment per update

    const intervalId = setInterval(() => {
        currentCount += increment;

        if (currentCount >= targetNumber) {
            currentCount = targetNumber;
            clearInterval(intervalId); // Stop animation when target reached
        }

        counterElement.textContent = currentCount;

        if (onUpdate) {
            onUpdate(currentCount); // Call optional update callback
        }
    }, 100); // Update every 10 milliseconds (adjust as needed)

    return function stopCounter() {
        clearInterval(intervalId);
    };
} // Update every 10 milliseconds
createCounter('project-counter', 200, 150);
createCounter('exp-counter', 9);
createCounter('client-counter', 100, 150);
createCounter('flying-time-counter', 100000, 100);


// agri-drone page
