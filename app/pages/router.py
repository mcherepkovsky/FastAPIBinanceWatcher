from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.services.binance import get_all_pairs

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(
    tags=["Фронтенд"]
)


@router.get("/")
async def read_root(
        request: Request,
        pairs=Depends(get_all_pairs)
):
    return templates.TemplateResponse(
        name="example.html",
        context={
            "request": request,
            "all_pairs": pairs,
        }
    )
