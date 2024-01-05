
const web = "http://127.0.0.1:5000/"

const letter = function (i) {
    this.letter = ko.observable(i || "");
    this.status = ko.observable(0); // 0 - неактивен, 1 - нет в слове, 2 - есть, но на другом месте, 3 - есть, на этом месте
}

const rowWord = function () {
    this.letters = ko.observableArray([new letter(), new letter(), new letter(), new letter(), new letter()]);
}

const keyboard = function () {
    this.keys = ko.observableArray([
        // первый ряд
        new letter("й"), new letter("ц"), new letter("у"), new letter("к"), new letter("е"), new letter("н"),
        new letter("г"), new letter("ш"), new letter("щ"), new letter("з"), new letter("х"), new letter("ъ"),
        // второй ряд
        new letter("ф"), new letter("ы"), new letter("в"), new letter("а"), new letter("п"), new letter("р"),
        new letter("о"), new letter("л"), new letter("д"), new letter("ж"), new letter("э"),
        // третий ряд
        new letter("я"), new letter("ч"), new letter("с"), new letter("м"), new letter("и"), new letter("т"),
        new letter("ь"), new letter("б"), new letter("ю"),
    ]);
}

const vm = function () {
    var self = this;

    this.countTry = 5; // с нуля
    this.currentTry = ko.observable(0);
    this.currentPos = ko.observable(0);
    this.title = "5 букв";
    this.word = ko.observable("");
    this.board = ko.observableArray([new rowWord(),
                        new rowWord(),
                        new rowWord(),
                        new rowWord(),
                        new rowWord(),
                        new rowWord()]);
    this.keyboard = ko.observable(new keyboard());
    this.backspaceText = ko.computed(() => {
        if (window.screen.availWidth <= 580) {
            return "⌫";
        } else {
            return "Backspace";
        }
    });
    this.enterText = ko.computed(() => {
        if (window.screen.availWidth <= 580) {
            return "↵";
        } else {
            return "Enter";
        }
    });

    this.getWord = () => {
        const req = new XMLHttpRequest();
        req.open("GET", web+"getWord", true);
        req.addEventListener("load", function() {
            self.word(req.responseText);
        });
        req.send(null);
    }

    this.addLetter = (letter) => {
        if (self.currentPos() < 5 && self.currentTry() <= self.countTry) {
            //console.log(letter);
            self.board()[self.currentTry()].letters()[self.currentPos()].letter(letter);
            self.currentPos(self.currentPos() + 1);
        }
    }

    this.eraseLetter = () => {
        if (self.currentPos() > 0 && self.currentTry() <= self.countTry) {
            self.currentPos(self.currentPos() - 1);
            self.board()[self.currentTry()].letters()[self.currentPos()].letter("");
        }
    }

    this.checkWord = () => {
        if (vmApp.currentTry() <= vmApp.countTry) {
            let resultWord = self.board()[self.currentTry()].letters().reduce((word, letter) => word + letter.letter(), "");
            if (resultWord.length === 5) {
                const req = new XMLHttpRequest();
                req.open("POST", "checkWord", true);
                req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
                req.onreadystatechange = () => {
                    if (req.readyState == 4 && req.status == 200) {

                        let array = JSON.parse(req.responseText);
                        for (i = 0; i < array.length; ++i) {
                            self.board()[self.currentTry()].letters()[i].status(array[i]);
                            self.keyboard().keys().forEach((item) => {
                                if (item.letter() === self.board()[self.currentTry()].letters()[i].letter() && item.status() < array[i]) {
                                    item.status(array[i]);
                                }
                            });
                        }
                        toastr.success("Вы выиграли!");
                        self.currentTry(7);
                    } else if (req.readyState == 4 && req.status == 400) {
                        toastr.error(req.responseText);

                    }
                    else if (req.readyState == 4) {
                        let array = JSON.parse(req.responseText);
                        for (i = 0; i < array.length; ++i) {
                            self.board()[self.currentTry()].letters()[i].status(array[i]);
                            self.keyboard().keys().forEach((item) => {
                                if (item.letter() === self.board()[self.currentTry()].letters()[i].letter() && item.status() < array[i]) {
                                    item.status(array[i]);
                                }
                            });
                        }
                        self.currentTry(self.currentTry() + 1);
                        self.currentPos(0);
                        if (self.currentTry() > self.countTry) {
                            toastr.error(`Вы проиграли!<br>Слово: ${self.word()}`);
                        }
                    }
                }
                req.send("word=" + self.word() + "&resultWord=" + resultWord);
            } else {
                toastr.error("Слово должно состоять из 5 букв!");
            }
        }
    }
}
var vmApp = new vm();

window.addEventListener("keyup", (e) => {

    if (typeof e !== "undefined" && vmApp.currentTry() <= vmApp.countTry) {
        if (e.key.match(/[а-яА-ЯЁё]/gi) && e.key !== "ё") {
            vmApp.addLetter(e.key);
        } else if (e.key === "Enter") {
            vmApp.checkWord();
        } else if (e.key === "Backspace") {
            vmApp.eraseLetter();
        }
    } else if (vmApp.currentTry() > vmApp.countTry && e.key === "Enter") {
        location.reload();
    }

});

ko.applyBindings(vmApp, document.getElementById("wordly"));

toastr.options = {
  "closeButton": true,
  "debug": false,
  "progressBar": false,
  "preventDuplicates": true,
  "positionClass": "toast-top-right",
  "onclick": null,
  "showDuration": "400",
  "hideDuration": "1000",
  "timeOut": "7000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
};

vmApp.getWord();