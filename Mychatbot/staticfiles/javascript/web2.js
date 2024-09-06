window.onload = function() {
    document.getElementById('calcbutton').addEventListener('click', calculateExpenses);
};

function calculateExpenses() {
    var textarea = document.getElementById("txt1");
    var text = textarea.value.split('\n'); 

    var monthlyExpenses = {};

    for (var i = 0; i < text.length; i++) {
        var line = text[i].trim(); 

        if (line.match(/^\w+$/)) {
            currentMonth = line; 
            monthlyExpenses[currentMonth] = 0;
        } else if (line.includes('₹')) {             
            var amountString = line.split('₹')[1].trim();
            var amount = parseInt(amountString.match(/\d+/)[0]);
            monthlyExpenses[currentMonth] += amount; 
        }
    }

    var output = '<b>Your Monthly Expenses</b><br>'; // Add the bold first line
    for (var month in monthlyExpenses) {
        output += month + ': ₹' + monthlyExpenses[month] + '<br>';
    }

    document.getElementById('pval').innerHTML = output;
}
