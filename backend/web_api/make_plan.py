from fastapi import APIRouter
from model.target import Target
from model.plan import Plan
from service.prompt import *
from service.client import get_completion

router = APIRouter(prefix="/plan");

mock_target = Target(
    goal="comfort a friend",
    situation="at friend's house",
    occupation="office worker",
    relationship="friends",
    activity="watching TV",
);

@router.post("/opening")
async def generate_opening(target: Target) -> Plan:
    response = get_completion(get_opening(target))
    return Plan(
        name="opening",
        content=response
    )

@router.post("/topic")
async def generate_topic(target: Target) -> Plan:
    response = get_completion(get_topic(target))
    return Plan(
        name="topic",
        content=response
    )

@router.post("/sustain")
async def generate_sustain(target: Target) -> Plan:
    response = get_completion(get_sustain(target))
    return Plan(
        name="sustain",
        content=response
    )

@router.post("/closing")
async def generate_closing(target: Target) -> Plan:
    response = get_completion(get_closing(target))
    return Plan(
        name="closing",
        content=response
    )

@router.post("/joke")
async def generate_joke(target: Target) -> Plan:
    response = get_completion(get_joke(target))
    return Plan(
        name="joke",
        content=response
    )


