$(document).ready(function () {

    // info when cart is empty
    var items = $('.item-in-cart');
    if (items.length > 0) {
        $('.not-empty-cart').show();
        $('.empty-cart').hide();
    } else {
        $('.empty-cart').show();
        $('.not-empty-cart').hide();
    }
})