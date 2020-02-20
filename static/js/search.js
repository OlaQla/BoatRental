$(document).ready(function(){

    /** Get all parameters from url */
    const urlParams = (new URL(location.href)).searchParams;
    
    /** True if it's not the first search */
    const hasSearched = urlParams.get("searched");

    /** Load querystring parameters into search form fields */
    $('input[name="search_name"]').val(urlParams.get("search_name"));
    $('input[name="min_passangers"]').val(urlParams.get("min_passangers"));
    $('input[name="min_cabins"]').val(urlParams.get("min_cabins"));

    /** 
     * Checkboxes have default value True if no searches were performed
     * Otherwise they will use the value found in relevant field in query string
     */
    $('input[name="include_sailboat"]').prop("checked", 
        hasSearched ? urlParams.get("include_sailboat") : true);

    $('input[name="include_powerboat"]').prop("checked", 
        hasSearched ? urlParams.get("include_powerboat") : true);

    $('input[name="include_catamaran"]').prop("checked", 
        hasSearched ? urlParams.get("include_catamaran") : true);

    $('input[name="include_motoryacht"]').prop("checked", 
        hasSearched ? urlParams.get("include_motoryacht") : true);

});
