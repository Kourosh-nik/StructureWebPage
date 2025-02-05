//    var swiper = new Swiper(".swiper-container", {
//        slidesPerView: 3,     // Show 3 cards at a time (adjust as needed)
//        spaceBetween: 20,     // Space between slides
//        loop: true,           // Infinite loop
//        autoplay: {           // Auto-slide
//            delay: 2000,      // 2 seconds per slide
//            disableOnInteraction: false
//        },
//        pagination: {
//            el: ".swiper-pagination",
//            clickable: true
//        },
//        navigation: {
//            nextEl: ".swiper-button-next",
//            prevEl: ".swiper-button-prev"
//        }
//    });

//     var swiper = new Swiper(".swiper-container", {
//     slidesPerView: 1,  /* Show 4 slides */
//     spaceBetween: 20,
//     loop: true,
//     autoplay: { delay: 2000, disableOnInteraction: false },
//     pagination: { el: ".swiper-pagination", clickable: true },
//     navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" }
//
// });

   var swiper = new Swiper('.swiper-container', {
       slidesPerView: 4,     // Show 3 cards at a time (adjust as needed)
       spaceBetween: 20,     // Space between slides
       loop: true,           // Infinite loop
       autoplay: {           // Auto-slide
           delay: 2000,      // 2 seconds per slide
           disableOnInteraction: false
       },
       pagination: {
           el: ".swiper-pagination",
           clickable: true
       },
       navigation: {
           nextEl: '.swiper-button-next',
           prevEl: '.swiper-button-prev',
       },
       breakpoints: {
           1024: { slidesPerView: 4, spaceBetween: 20 }, /* Large screens */
           768: { slidesPerView: 2, spaceBetween: 15 },  /* Tablets */
           300: { slidesPerView: 1, spaceBetween: 10 },  /* Mobile */
       },
   });

