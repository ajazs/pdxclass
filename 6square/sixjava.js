/**
 * Created by jaz on 12/21/2016.
 */

/*
var box = document.getElementById('box'),
    colors = ['purple', 'yellow', 'orange', 'brown', 'black'];

function box.onclick(i);{
    color = colors.shift();
    colors.push(color);

    box.style.backgroundColor = color;
}
*/

function changeDivBackground() {

    colors = ["red", "blue", "orange", "green", "yellow","pink","purple","magenta","black"];




    divs = ["one","two","three","four","five","six"];

    for (var i = 0; i <= divs.length; i ++){

        var id = divs[i];

        var rand = colors[Math.floor(Math.random() * colors.length)];


    document.getElementById(id).style.backgroundColor = rand;
    }
}


/*
for (var i=1; i <= 100; i++)
{
    if(i % 5 == 0 && i % 3 == 0) {
        console.log("FizzBuzz");
    }
    else if (i % 3 == 0) {
        console.log("Fizz");
    }
    else if (i % 5 == 0) {

        console.log("Buzz");
    }
    else {
        console.log(i);
    }
}

*/
colors = ["red", "blue", "orange", "green", "yellow","pink","purple","magenta","black"];

function numbers(){
    for (var i = 1; i <=10;i++){
   console.log(i);}
}
numbers();

function listPrint(id){
    for (var i = 0; i <= id.length; i++){
        console.log(colors[i]);}


}
listPrint(colors);