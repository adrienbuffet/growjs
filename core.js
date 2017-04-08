var exec = require('child_process').exec;

var relay = function(pin, time) {
    return "sudo python /home/pi/growjs/scripts/relay.py " + pin + " " + time; 
};

var hygrometer = function(pin) {
    return "sudo python /home/pi/growjs/scripts/hygrometer.py " + pin;
};

var water = function(pin, time) {
    exec(relay(pin, time));
};

var hygro = function(n) {
    exec(hygrometer(pin));
};

module.exports = {testing: hygro, watering: water};
