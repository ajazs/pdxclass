/**
 * Created by jaz on 12/29/2016.
 */
/*
$("#click").click(function() {
    var word = $("#word").val();
    var wordList = word.split("");

    var vowels = ["a", "e", "i", "o", "u"];

    for (var i = 0; i <= wordList.length; i++) {

        if (wordList[i] == vowels.indexOf["a", "e", "i", "o", "u"]) {

            console.log("valid");

        } else if (wordList[i] == -1{

            console.log("invalid");
        }


    }


});
*/
$("body").append("<h3 id="textEntered"></h3>");
var vowels = ["a","e","i","o","u"];


$("#click").click(function(){
  var userWord = $("#word").val();
console.log(userWord);
    var isValid = false;
    for(var i = 0;i<userWord.length;i++){

        var letter = userWord[i];
        for(var k = 0; k <vowels.length;k++){

            if(letter==vowels[k]){
                isValid = true;

            }

        }
    }


    if(isValid){
        $("body").html("<h3>this is a valid word"</h3>");
        $("#textEntered").html("This is a valid word")
    }else{
        $("body").append("this is invalid");
    }
//$("#click").click(function())

});

