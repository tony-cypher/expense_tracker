const cats = [];
const catValues = [];

const catSum = document.getElementById('cat-sum').getElementsByTagName('span')

for (i = 0; i < catSum.length; i++) {
    if (i % 2 == 1) {
        catValues.push(catSum[i].innerText.replace('$', ''))
    } else {
        cats.push(catSum[i].innerText)
    }
};
console.log(cats)
console.log(catValues)

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: cats,
        datasets: [{
            label: 'Gross Category',
            data: catValues,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
            ],
            borderWidth: 1
        }]
    }
});