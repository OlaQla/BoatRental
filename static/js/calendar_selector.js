const dateForField = (date) => {
    calDay = ("0" + date.getDate()).slice(-2);
    calMonth = ("0" + (date.getMonth() + 1)).slice(-2);
    calYear = date.getFullYear()
    return calYear + "-" + (calMonth) + "-" + (calDay)
}

$(document).ready(function () {
    date = new Date()
    boat_id = $(window.location.href.split("/")).last()[0];
    $.ajax({
        url: `/boats/availability/${boat_id}/${date.getFullYear()}/${date.getMonth()}`,

    }).done(function (data) {
        $("#calendar").find("td").each(function (index) {
            $(this).text(data[index].day)

            if (data[index].in_month) {
                $(this).addClass("in_month")
            }
            if (data[index].available) {
                $(this).addClass("available")
            }

        })

    });

    let isFirst = true;
    let newStartDate = new Date();
    let newEndDate = new Date();

    $(document).on('click', '.in_month.available', function () {

        currDate = new Date()

        calDay = $(this).text()
        calMonth = currDate.getMonth();
        calYear = currDate.getFullYear()

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
            $(this).addClass('selected')
            const $allAvailable = $(".available")
            const indices = $(".selected").toArray().map(x => $allAvailable.index(x));
            $allAvailable.slice(indices[0], indices[1]).addClass("selected")

            const $allSelected = $(".selected")
            if (parseInt($allSelected.eq(-1).text()) - parseInt($allSelected.eq(0).text()) + 1 !== $allSelected.length) {
                $allSelected.removeClass("selected")
                $("#startDay").val('')
                $("#endDay").val('')
            }
        }

        isFirst = !isFirst;
    });
})
