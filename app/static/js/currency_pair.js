// Функция для получения данных о паре (уже была написана выше)
async function fetchCurrencyPairDetails(pair) {
    try {
        const response = await fetch(`/api/v1/currency/${pair}`);
        if (!response.ok) throw new Error('Failed to fetch pair details');
        const data = await response.json();

        const pairDetails = document.getElementById('pair-details');
        pairDetails.innerHTML = `
            <p>Pair: ${pair}</p>
            <p>Price: ${data.price}</p>
        `;
    } catch (error) {
        console.error('Error fetching pair details:', error);
        document.getElementById('pair-details').innerHTML =
            '<p style="color: red;">Error loading pair details.</p>';
    }
}

// Обработчик для формы
const pairForm = document.getElementById('pair-form');
pairForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Предотвращаем отправку формы

    const pairInput = document.getElementById('pair-input').value;
    const pairSelect = document.getElementById('pair-select').value;

    // Используем введённое значение или выбранное из списка
    const selectedPair = pairInput || pairSelect;

    if (!selectedPair) {
        alert('Please enter or select a pair!');
        return;
    }

    // Выполняем функцию для получения данных
    fetchCurrencyPairDetails(selectedPair);
});
