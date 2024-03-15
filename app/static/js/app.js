/* Add your Application JavaScript */
console.log('this is some JavaScript code');

function notify() {
  alert('in here I will do something');
}

// notify();
window.onload = commaSep();
function commaSep(){
    nfObject = new Intl.NumberFormat('en-US');
    let elements = document.getElementsByClassName('property-price')
    for (let i=0; i < elements.length; i++){
        output = nfObject.format(Number(elements[i].textContent.slice(1)));
        elements[i].textContent = '$'+output
    }
}