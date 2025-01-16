import { createSubscriptionElement } from './utils.js';

document.getElementById('start-notifications').addEventListener('click', async () => {
    const pair = document.getElementById('notify-pair').value.trim();
    const interval = parseInt(document.getElementById('notify-interval').value, 10);
    const notificationList = document.getElementById("notification-list");

    if (!pair || isNaN(interval) || interval <= 0) {
        alert('Please provide valid inputs for Pair and Interval.');
        return;
    }

    const notifData = { pair, interval };

    try {
        const response = await fetch('/subscriptions/add_subscription', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(notifData),
        });

        if (!response.ok) {
            const error = await response.json();
            alert(`Error: ${error.message || 'Could not add subscription.'}`);
            return;
        }

        const result = await response.json();
        console.log('Subscription added:', result);
        alert(`Subscription added successfully for pair: ${pair}`);

        createSubscriptionElement(result, notificationList);
    } catch (error) {
        console.error('Error adding subscription:', error);
        alert('An error occurred while adding the subscription.');
    }
});
