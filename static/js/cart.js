$(document).ready(function () {

    var items = $('.item-in-cart');
    if (items.length > 0) {
        $('.not-empty-cart').show();
        $('.empty-cart').hide();
    } else {
        $('.empty-cart').show();
        $('.not-empty-cart').hide();
    }
})