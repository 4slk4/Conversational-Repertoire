from fastapi import APIRouter;
from service import sample;

router = APIRouter(prefix="/test");

@router.get("/")
def test():
    return sample.goodbye();