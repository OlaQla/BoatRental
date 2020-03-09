// Function converting date to postable form to store in form fields
const dateForField = (date) => {
    const calDay = ("0" + date.getDate()).slice(-2);
    const calMonth = ("0" + (date.getMonth() + 1)).slice(-2);
    const calYear = date.getFullYear()
    return calYear + "-" + (calMonth) + "-" + (calDay)
}

// A set of booked dated
const bookedDates = new Set();

// Selected beginning date
let newStartDate = undefined;

// Selected end date
let newEndDate = undefined;

// Indicator if click is first or second
let isFirst = true;

// Get new calendar information from endpoint and redraw calendar based on returned data
const reloadCalendar = (boat_id, year, month) => {

    // Disable buttons while reloading
   $("button").prop('disabled', true);

    $.ajax({url: `/boats/availability/${boat_id}/${year}/${month}`})
        .done(function (data) {

            // Enable buttons back after reload
            $("button[type=button]").prop('disabled', false);
            $("button[type=submit]").prop('disabled', !(!!newStartDate && !!newEndDate));

            // Aggregate already booked dates in a set, so we will have all data 
            // that we pulled down for state validation purposes
            data.filter(x => x.in_month && !x.available)
                .forEach(v => bookedDates.add((new Date(year, month, v.day)).getTime()));

            // Clear out all selections in calendar, it will be recreated below
            $(".selected").removeClass("selected");
            
            $("#calendar").find("td").each(function (index) {
                $(this).text(data[index].day)

                // Mark cells between start and end dates
                if (data[index].in_month) {
                    if(!!newStartDate) {
                        if(newStartDate.getTime() === (new Date(year, month, data[index].day)).getTime()) {
                            $(this).addClass("selected");
                        }
                        else if(!!newEndDate) {
                            currentCellMillis = (new Date(year, month, data[index].day)).getTime()
                            if(currentCellMillis >= newStartDate.getTime() && currentCellMillis <= newEndDate.getTime()) {
                                $(this).addClass("selected");
                            }
                        }
                    }

                    $(this).addClass("in_month").removeClass("not_in_month");
                } else {
                    $(this).removeClass("in_month").addClass("not_in_month");
                }

                if (data[index].available) {
                    $(this).addClass("available");
                } else {
                    $(this).removeClass("available");
                }

                $(".month").text(new Date(year, month).toLocaleString('default', { month: 'long' }));

            })
    });
}

// Function resetting all to initial state
const resetState = () => {
    const $allSelected = $(".selected");
    $allSelected.removeClass("selected");
    newStartDate = undefined;
    newEndDate = undefined;
    isFirst = true;
    $("button[type=submit]").prop("disabled", true);
    $("#startDay").val('');
    $("#endDay").val('');
}

$(document).ready(function () {
    // This is calendar movable date to pick year / month
    date = new Date()

    // Get boat if from url
    boat_id = $(window.location.href.split("/")).last()[0];

    // Initially load calendar for current month
    reloadCalendar(boat_id, date.getFullYear(), date.getMonth());

    // Get month change buttons and assign actions to them 
    $buttons = $("[type=button]");

    $buttons.eq(1).click(function(){
        date = new Date(date.getFullYear(), date.getMonth() - 1);
        reloadCalendar(boat_id, date.getFullYear(), date.getMonth());
    });

    $buttons.eq(2).click(function(){
        date = new Date(date.getFullYear(), date.getMonth() + 1);
        reloadCalendar(boat_id, date.getFullYear(), date.getMonth());
    });

    // Attach click event to days in currently chosen month that are available
    $(document).on('click', '.in_month.available', function () {

        calDay = $(this).text()
        calMonth = date.getMonth();
        calYear = date.getFullYear()

        // Mark start date in calendar as selected, set start / end date variables
        if (isFirst) {
            newStartDate = new Date(calYear, calMonth, calDay);
            newEndDate = undefined;
            $("#startDay").val(dateForField(newStartDate));
            $('#endDay').val('');
            $('.selected').removeClass('selected');
            $(this).addClass('selected');
            $("button[type=submit]").prop("disabled", true);

        } else {
            // Pick new end date, swap dates if end date if before start date
            newEndDate = new Date(calYear, calMonth, calDay)
            if (newEndDate > newStartDate) {
                $("#endDay").val(dateForField(newEndDate))
            }
            else {
                [newStartDate, newEndDate] = [newEndDate, newStartDate]
                $("#startDay").val(dateForField(newStartDate))
                $("#endDay").val(dateForField(newEndDate))
            }

            // Test if any day in between is already booked
            startMs = newStartDate.getTime();
            endMs = newEndDate.getTime();
            if([...bookedDates].find(d => d >= startMs && d <= endMs)) {
                // state is invalid, perform state reset to get back to selection mode
                resetState()
                return;
            }

            // Get all potentially available days in currently selected month
            const $allAvailable = $(".in_month.available")
            
            // Mark all dates between start and end as selected
            $allAvailable.each(function(){
                const cellDate = new Date(calYear, calMonth, $(this).text());
                if(cellDate >= newStartDate && cellDate <= newEndDate) {
                    $(this).addClass("selected");
                }
            });

            // Validate state, return to initial state if current is invalid
            const $allSelected = $(".selected");
            if (parseInt($allSelected.eq(-1).text()) - parseInt($allSelected.eq(0).text()) + 1 !== $allSelected.length) {
                resetState();
                return;
            } else {
                $("button[type=submit]").prop("disabled", false);
            }
        }

        // Flip isFirst to know is next click first or not
        isFirst = !isFirst;
    });
})
