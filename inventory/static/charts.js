const ctx = document.getElementById('stockDistributionChart').getContext('2d');

    const stockDistributionChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Beverages', 'Snacks', 'Cleaning Supplies', 'Stationery'],
            datasets: [{
                label: 'Stock Distribution',
                data: [30, 25, 20, 15], // Replace with your actual stock data
                backgroundColor: [
                    '#F4811F',
                    '#008163',
                    '#EE2526',
                    '#fff340'
                ],
                hoverOffset: 10
            }]
        },
        options: {
            plugins: {
                legend: {
                    position: 'right', // Legend on the right for better readability
                    labels: {
                        boxWidth: 20,
                        padding: 15
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.raw || 0;
                            return `${label}: ${value} items`;
                        }
                    }
                }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });

    const topCtx = document.getElementById('topProductsChart').getContext('2d');

const topProductsChart = new Chart(topCtx, {
    type: 'bar',
    data: {
        labels: ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
        datasets: [{
            label: 'Units Sold',
            data: [100, 85, 70, 55, 40], // Replace with actual sales data
            backgroundColor: ['#4285F4', '#EA4335', '#FBBC05', '#34A853', '#F4811F'],
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
            legend: {
                display: false // Hides legend for a clean look
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return `${context.label}: ${context.raw} units sold`;
                    }
                }
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Products'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Units Sold'
                },
                beginAtZero: true
            }
        },
        responsive: true,
        maintainAspectRatio: false
    }
});