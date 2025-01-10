async function fetchPopularPairs() {
    try {
        const response = await fetch('/api/v1/currency/popular-pairs');
        const data = await response.json();
        const pairsList = document.querySelector('#popular-pairs .pairs-list');

        // Очистим текущие данные
        pairsList.innerHTML = '';

        // Заполним новыми популярными парами
        for (let [symbol, price] of Object.entries(data.popular_pairs)) {
            const pairItem = document.createElement('div');
            pairItem.classList.add('pair-item');
            pairItem.innerHTML = `
                <span class="symbol">${symbol}</span>
                <span class="price">${price}</span>
            `;
            pairsList.appendChild(pairItem);
        }
    } catch (error) {
        console.error('Error fetching popular pairs:', error);
    }
}


// Обновлять популярные пары каждые 60 секунд
setInterval(fetchPopularPairs, 60 * 1000);

// Вызвать fetchPopularPairs сразу при загрузке страницы
window.onload = fetchPopularPairs;