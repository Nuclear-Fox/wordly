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
    this.currentTry = ko.observable(0);
    this.currentPos = ko.observable(0);
    this.title = "5 букв";
    this.word = ko.observable("");
    this.board = ko.observableArray(defaultBoard);

    this.getWord = () => {
        req.open("GET", web+"getWord", true);
        req.addEventListener("load", function() {
            self.word(req.responseText);
        });
        req.send(null);
    }

    this.addLetter = (letter) => {
        if (self.currentPos() < 5) {
            console.log(letter);
            self.board()[self.currentTry()][self.currentPos()] = letter;
            self.currentPos(self.currentPos() + 1);
            //self.board.valueHasMutated();
        }
    }

    this.eraseLetter = () => {
        if (self.currentPos() > 0) {
            self.currentPos(self.currentPos() - 1);
            self.board()[self.currentTry()][self.currentPos()] = "";
        }
    }

    this.checkWord = () => {
        let resultWord = self.board()[self.currentTry()].reduce((word, letter) => word + letter, "");
        if (resultWord.length === 5) {
            req.open("POST", "checkWord", true);
            req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
            //req.onreadystatechange = function() {//Call a function when the state changes.
            //    if (req.readyState == 4 && req.status == 200) {
            //        alert(req.responseText);
            //    }
            //}
            //req.addEventListener("load", function() {
            //    self.word(req.responseText);
            //});
            req.send("word=" + self.word() + "&resultWord=" + resultWord);
        }
    }
}
var vmApp = new vm();

window.addEventListener("keyup", (e) => {

    if (typeof e !== "undefined") {
        if (e.key.match(/[а-яА-ЯЁё]/gi)) {
            vmApp.addLetter(e.key);
        } else if (e.key === "Enter") {
            vmApp.checkWord();
        } else if (e.key === "Backspace") {
            vmApp.eraseLetter();
        }
    }

});

ko.applyBindings(vmApp, document.getElementById("wordly"));

vmApp.getWord();


