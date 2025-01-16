export function createSubscriptionElement(subscription, notificationList) {
    const li = document.createElement("li");
    li.style.display = "flex";
    li.style.justifyContent = "space-between";
    li.style.alignItems = "center";
    li.style.marginBottom = "10px";
    li.style.padding = "10px";
    li.style.border = "1px solid #ccc";
    li.style.borderRadius = "5px";
    li.style.backgroundColor = "#f9f9f9";

    const pairText = document.createElement("span");
    pairText.textContent = `Pair: ${subscription.pair}`;
    pairText.style.fontWeight = "bold";

    const intervalText = document.createElement("span");
    intervalText.textContent = `Interval: ${subscription.interval}`;

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.style.backgroundColor = "#e74c3c";
    deleteButton.style.color = "#fff";
    deleteButton.style.border = "none";
    deleteButton.style.padding = "5px 10px";
    deleteButton.style.borderRadius = "5px";
    deleteButton.style.cursor = "pointer";

    deleteButton.setAttribute("data-id", subscription.id);

    deleteButton.addEventListener("click", () => {
        const subscriptionId = deleteButton.getAttribute("data-id");
        fetch(`/subscriptions/delete_subscription/${subscriptionId}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then(response => {
            if (response.ok) {
                notificationList.removeChild(li);
                console.log(`Subscription with id ${subscriptionId} deleted successfully.`);
            } else {
                console.error("Failed to delete subscription.");
            }
        })
        .catch(error => {
            console.error("Error deleting subscription:", error);
        });
    });

    li.appendChild(pairText);
    li.appendChild(intervalText);
    li.appendChild(deleteButton);
    notificationList.appendChild(li);
}
