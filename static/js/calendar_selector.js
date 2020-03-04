const dateForField = (date) => {
    calDay = ("0" + date.getDate()).slice(-2);
    calMonth = ("0" + (date.getMonth() + 1)).slice(-2);
    calYear = date.getFullYear()
    return calYear + "-" + (calMonth) + "-" + (calDay)
}

const aggregatedData = new Set();

const reloadCalendar = (boat_id, year, month) => {
    // Disable buttons while reloading
   $("button").prop('disabled', true);

    $.ajax({url: `/boats/availability/${boat_id}/${year}/${month}`})
        .done(function (data) {

            // Enable buttons back after reload
            $("button").prop('disabled', false);

            data.filter(x => x.in_month && !x.available)
                .forEach(v => aggregatedData.add((new Date(year, month, v.day)).getTime()));

            $("#calendar").find("td").each(function (index) {
                $(this).text(data[index].day)

                $(".selected").removeClass("selected");

                if (data[index].in_month) {
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

const clearSelection = () => {
    const $allSelected = $(".selected");
    $allSelected.removeClass("selected");
    $("#startDay").val('');
    $("#endDay").val('');
}

$(document).ready(function () {
    date = new Date()
    boat_id = $(window.location.href.split("/")).last()[0];
    reloadCalendar(boat_id, date.getFullYear(), date.getMonth())

    let isFirst = true;
    let newStartDate = new Date();
    let newEndDate = new Date();

    $buttons = $("[type=button]");

    $buttons.eq(1).click(function(){
        date = new Date(date.getFullYear(), date.getMonth() - 1);
        reloadCalendar(boat_id, date.getFullYear(), date.getMonth() + 1);
    });

    $buttons.eq(2).click(function(){
        date = new Date(date.getFullYear(), date.getMonth() + 1);
        reloadCalendar(boat_id, date.getFullYear(), date.getMonth() + 1);
    });

    $(document).on('click', '.in_month.available', function () {

        calDay = $(this).text()
        calMonth = date.getMonth();
        calYear = date.getFullYear()

        if (isFirst) {
            newStartDate = new Date(calYear, calMonth, calDay)
            $("#startDay").val(dateForField(newStartDate))
            $('#endDay').val('')
            $('.selected').removeClass('selected')
            $(this).addClass('selected')

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
            if([...aggregatedData].find(d => d >= startMs && d <= endMs)) {
                isFirst = true;
                clearSelection();
                return;
            }

            $(this).addClass('selected')
            const $allAvailable = $(".available")
            const indices = $(".selected").toArray().map(x => $allAvailable.index(x));
            $allAvailable.slice(indices[0], indices[1]).addClass("selected")

            const $allSelected = $(".selected");
            if (parseInt($allSelected.eq(-1).text()) - parseInt($allSelected.eq(0).text()) + 1 !== $allSelected.length) {
                clearSelection();
            }
        }

        isFirst = !isFirst;
    });
})
