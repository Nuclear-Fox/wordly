const req = new XMLHttpRequest();
const web = "http://127.0.0.1:5000/"
const defaultBoard = [
                        ["", "", "", "", ""],
                        ["", "", "", "", ""],
                        ["", "", "", "", ""],
                        ["", "", "", "", ""],
                        ["", "", "", "", ""],
                        ["", "", "", "", ""]
                    ];

var vm = function () {
    var self = this;

    this.countTry = 6;
    this.currentTry = 0;
    this.title = "5 букв";
    this.word = ko.observable("");
    this.board = ko.observable(defaultBoard);



    this.getWord = function() {
        req.open("GET", web+"getWord", true);
        req.addEventListener("load", function() {
            this.word(req.responseText);
        });
        req.send(null);
    }
}


var vmApp = new vm();
ko.applyBindings(vmApp, document.getElementById("wordly"));
