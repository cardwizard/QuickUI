function add_placeholder(element, id) {
    if (!("help" in element))
        return;
    $(id).attr("placeholder", element["help"]);
}

function add_default(element, id) {
    if (!("default" in element))
        return;

    let default_value = element["default"];

    if ((element["type"] == "tuple") || (element["type"] == "dict") ||
            (element["type"] == "list") || (element["type"] == "json"))

        default_value = JSON.stringify(default_value);

    if (element["type"] == "bool")
    {
        if (default_value == "True")
        {
            default_value = true;
            $(id).attr("checked", "checked");
        }
        else
            default_value = false;
    }
    if (default_value)
        $(id).attr("value", default_value);
}

function add_required_check(element, id) {
    if (!("required" in element))
        return;

    if (!(element["required"] == "True"))
        return;

    $(id).prop("required", true);
}

function cleanup_divs(id) {
    var parent_id = $(id).parent().parent().attr("id");
    $(id).parent().remove();
    return parent_id;
}

function add_data_type(element, id) {
    if (!("type" in element))
        return;

    if (element["type"] == "str")
        $(id).attr("type", "text");

    if (element["type"] == "int") {
        $(id).attr("type", "number");
        $(id).attr("step", "1");
    }

    if (element["type"] == "float") {
        $(id).attr("type", "number");
    }

    if (element["type"] == "bool") {
        $(id).attr("type", "checkbox");
    }

}

function fill_input_boxes() {
    fields = {{ form_fields|safe }};

    for (var i in fields) {
        var element = fields[i];
        var id = "#input_" + i.toString();
        $(id).attr("name", element["parameter"]);

        // 1. Set the placeholder value if default value exists.
        add_placeholder(element, id);

        // 2. Set the default if it exists
        add_default(element, id);

        // 3. Add the required attribute. Jinja sends booleans as a string
        add_required_check(element, id);

        // 4. Add a data type
        add_data_type(element, id);
    }
}

const submitBtn = $('#btn-submit');
const submitForm = $('#submit-form');
const input0 = $('#input_0');

$('#submit-form').submit(function(e) {
    e.preventDefault();
    // get all the inputs into an array.
    var $inputs = $('#submit-form :input');

    // get an associative array of just the values.
    var values = {};

    $inputs.each(function() {
        if (this.type == "checkbox")
            values[this.name] = $(this).prop("checked");
        else if (this.type == "number")
            values[this.name] = parseFloat($(this).val());
        else
            values[this.name] = String($(this).val());
    });

    run_step(values);
});

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
}

function getFormattedDate() {
    var date = new Date();

    var month = date.getMonth() + 1;
    var day = date.getDate();
    var hour = date.getHours();
    var min = date.getMinutes();
    var sec = date.getSeconds();

    month = (month < 10 ? "0" : "") + month;
    day = (day < 10 ? "0" : "") + day;
    hour = (hour < 10 ? "0" : "") + hour;
    min = (min < 10 ? "0" : "") + min;
    sec = (sec < 10 ? "0" : "") + sec;

    var str = date.getFullYear() + "-" + month + "-" + day + " " +  hour + ":" + min + ":" + sec;
    return str;
}


function run_step(values)
{
    // 1. Create a new terminal object
    var random_id = String(getRandomInt(0, 1000))
    var term_id = "terminal_" + random_id;
    var time_header = "time_box_" + random_id;

    $('#terminals').prepend("<div id='" + time_header + "'>Run time: " + getFormattedDate() +  "</div><br><div id='" + term_id + "'> </div><br>");

    var term = $('#' + term_id).terminal({
        python: function(...args) {
            var options = $.terminal.parse_options(args);
            console.log(options);
        }
    }, {checkArity: false});

    // 2. Clear the terminal
    term.exec("clear");
    term.echo("----------------------------------------------------------");
    term.echo("Running ->");

    // 3. Add term_id to the values field
    values["term_id"] = term_id;

    socket.connect();
    console.log("Established a connection");

    socket.emit("run_script", {data: values});
    socket.on("process_output", function(msg) {
        term.echo(msg.data);
        console.log(msg.data);
        if (msg.data == "Process Run Completed.")
        {
            console.log("Closing the connection");
            socket.disconnect();
            socket.off("process_output");
        }
    });
}
fill_input_boxes();

// 4. Call the run script function
var socket = io.connect('http://' + document.domain + ':' + location.port + '/stream');