const randomNumber = math.floor(math.random()*100) +1;
console.log(randomNumber)
let attemp = 0;

function checkGuess(){
    const guess = parseint(document.getElementById("guessField").value)
    attempt++;
    if(isNaN(guess)  ||guess  < 1 || guess > 100){
        setMessage("please enter a valid number between 1 and 100")
        return;
    }
    if(guess === randomNumber){
        setMessage("congratulations Guessed correctly")
        document.getElementById("guessfield").disabled = true;
    }else if(guess <randomNumber){
        setMessage("to low, try again")
    }else{
        setMessage("to high,try again")
    }

}
function setMessage(message){
    document.getElementById("message").textcontent = message
}