const dateForField = (date) => {
    calDay = ("0" + date.getDate()).slice(-2);
    calMonth = ("0" + (date.getMonth() + 1)).slice(-2);
    calYear = date.getFullYear()
    return calYear + "-" + (calMonth) + "-" + (calDay)
}

const bookedDates = new Set();
let newStartDate = undefined;
let newEndDate = undefined;
let isFirst = true;

const reloadCalendar = (boat_id, year, month) => {
    // Disable buttons while reloading
   $("button").prop('disabled', true);

    $.ajax({url: `/boats/availability/${boat_id}/${year}/${month}`})
        .done(function (data) {

            // Enable buttons back after reload
            $("button[type=button]").prop('disabled', false);
            $("button[type=submit]").prop('disabled', !(!!newStartDate && !!newEndDate));

            data.filter(x => x.in_month && !x.available)
                .forEach(v => bookedDates.add((new Date(year, month, v.day)).getTime()));

            $(".selected").removeClass("selected");
            
            $("#calendar").find("td").each(function (index) {
                $(this).text(data[index].day)

                if (data[index].in_month) {
                    if(!!newStartDate && newStartDate.getTime() === (new Date(year, month, data[index].day)).getTime()) {
                        $(this).addClass("selected");
                    }

                    $(this).addClass("in_month");
                } else {
                    $(this).removeClass("in_month");
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
    date = new Date()
    boat_id = $(window.location.href.split("/")).last()[0];
    reloadCalendar(boat_id, date.getFullYear(), date.getMonth());

    $buttons = $("[type=button]");

    $buttons.eq(1).click(function(){
        date = new Date(date.getFullYear(), date.getMonth() - 1);
        reloadCalendar(boat_id, date.getFullYear(), date.getMonth());
    });

    $buttons.eq(2).click(function(){
        date = new Date(date.getFullYear(), date.getMonth() + 1);
        reloadCalendar(boat_id, date.getFullYear(), date.getMonth());
    });

    $(document).on('click', '.in_month.available', function () {

        calDay = $(this).text()
        calMonth = date.getMonth();
        calYear = date.getFullYear()

        if (isFirst) {
            newStartDate = new Date(calYear, calMonth, calDay);
            newEndDate = undefined;
            $("#startDay").val(dateForField(newStartDate));
            $('#endDay').val('');
            $('.selected').removeClass('selected');
            $(this).addClass('selected');
            $("button[type=submit]").prop("disabled", true);

        } else {
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
                resetState()
                return;
            }

            $(this).addClass('selected')
            const $allAvailable = $(".available")
            const indices = $(".selected").toArray().map(x => $allAvailable.index(x));
            $allAvailable.slice(indices[0], indices[1]).addClass("selected");

            const $allSelected = $(".selected");
            if (parseInt($allSelected.eq(-1).text()) - parseInt($allSelected.eq(0).text()) + 1 !== $allSelected.length) {
                resetState();
                return;
            } else {
                $("button[type=submit]").prop("disabled", false);
            }
        }

        isFirst = !isFirst;
    });
})
