from fastapi import APIRouter, Depends
from pydantic import parse_obj_as

from app.exceptions import NotificationCannotBeAddedException, SubscriptionNotFound
from app.subscriptions.schemas import NotificationData, SSubscription

from app.subscriptions.dao import SubscriptionsDAO
from app.users.dependences import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/subscriptions",
    tags=["Subscriptions"]
)


@router.post("/add_subscription")
async def add_subscription(
    notif_data: NotificationData,
    user_id: int = Depends(get_current_user)
):
    result = await SubscriptionsDAO.add(
        user_id=user_id,
        pair=notif_data.pair,
        interval=notif_data.interval
    )

    return {
        "id": result.id,
        "pair": result.pair,
        "interval": result.interval
    }


@router.post("/get_user_subscriptions")
async def get_user_subscriptions(
    user_id: int = Depends(get_current_user)
):
    return await SubscriptionsDAO.find_all_subscriptions(user_id=user_id)


@router.delete("/delete_subscription/{subscription_id}")
async def delete_subscription(
    subscription_id: int,
    user_id: int = Depends(get_current_user)
):
    await SubscriptionsDAO.delete(user_id=user_id, id=subscription_id)

