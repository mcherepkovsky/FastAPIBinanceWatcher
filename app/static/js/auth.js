import { createSubscriptionElement } from './utils.js';

document.addEventListener("DOMContentLoaded", () => {
    const notificationSettings = document.getElementById("notification-settings");
    const notificationList = document.getElementById("notification-list");

    window.onTelegramAuth = function (user) {
        fetch("/auth/telegram", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                id: user.id,
                first_name: user.first_name,
                username: user.username,
                photo_url: user.photo_url,
                auth_date: user.auth_date,
                hash: user.hash,
            }),
        })
        .then(response => response.json())
        .then(data => {
            console.log("Authorization success:", data);
            document.getElementById("auth-status").innerHTML = `<p><b>Welcome, ${data.username}!</b></p>`;
            notificationSettings.style.display = "block";

            fetch("/subscriptions/get_user_subscriptions", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    user_id: data.id,
                }),
            })
            .then(response => response.json())
            .then(subscriptions => {
                console.log("User subscriptions:", subscriptions);

                notificationList.innerHTML = "";
                subscriptions.forEach(sub => {
                    createSubscriptionElement(sub, notificationList);
                });
            })
            .catch(error => {
                console.error("Error fetching subscriptions:", error);
            });
        })
        .catch(error => {
            console.error("Authorization error:", error);
            document.getElementById("auth-status").innerHTML = "<p><b>Authorization failed. Please try again.</b></p>";
        });
    };
});
