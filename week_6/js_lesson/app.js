//Data types:
/*//Mulitiline
1.String, 
2. integers/numbers
3.Booleans 
4.Arrays
5. 
*/
let name = "Mike"
let height = 50


function submit(){
var input = document.getElementById("Input Field").value
var input = parseInt(input); //data type conversion
var input = input+1
console.log(typeof(input))}


let adult = true; //Boolean datatype
let fruits=['kiwi','banana','apple', 30,false] //array or a list
let person = {
    firstname:'Adam',
    lastname:'lovelace',
    age:18,
    address:{
        country:'Sudan',
        city:'Khartoum',
        street:'Bani bani',

    },
    children:['Kelly','Mary']

}
console.log(person.address.country)
console.log(typeof(person))

function saveItem(){
    var input = document.getElementById("inputField").value
    localStorage.setItem('inputItem', input);
    ShowWelcomeMessage(input)
}

function ShowWelcomeMessage(input){
    var messageElement = document.getElementById("showMessage")
    messageElement.textContent = "we have saved your input as"+ input
}

var storedItem = localStorage.getItem('inputField');
if(storedItem)
