const navbar = document.querySelector('.navbar');

document.addEventListener( 'DOMContentLoaded', function() {
    var splide = new Splide('.splide', {
      perPage: 3,
      rewind : true,
    } );

    splide.mount();
} );

document.addEventListener('scroll', ()=> {
    const scrollTop = this.pageYOffset;
    if(scrollTop >= 50){
        navbar.classList.add('scrolled');
        navbar.classList.remove('is-dark');
    } else {
        navbar.classList.remove('scrolled');
        navbar.classList.add('is-dark');
    }
});

