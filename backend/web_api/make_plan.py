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

@router.get("/test")
async def generate_opening(target: Target=mock_target) -> Plan:
    response = get_completion(get_opening(target))
    return Plan(
        name="Opening Lines",
        content=response
    )

@router.post("/opening")
async def generate_opening(target: Target) -> Plan:
    response = get_completion(get_opening(target))
    return Plan(
        name="Opening Lines",
        content=response
    )

@router.post("/topic")
async def generate_topic(target: Target) -> Plan:
    response = get_completion(get_topic(target))
    return Plan(
        name="Topic",
        content=response
    )

@router.post("/sustain")
async def generate_sustain(target: Target) -> Plan:
    response = get_completion(get_sustain(target))
    return Plan(
        name="Sustain",
        content=response
    )

@router.post("/rapport")
async def generate_rapport(target: Target) -> Plan:
    response = get_completion(get_rapport(target))
    return Plan(
        name="Build Rapport",
        content=response
    )

@router.post("/closing")
async def generate_closing(target: Target) -> Plan:
    response = get_completion(get_closing(target))
    return Plan(
        name="Closing Lines",
        content=response
    )

@router.post("/joke")
async def generate_joke(target: Target) -> Plan:
    response = get_completion(get_joke(target))
    return Plan(
        name="Jokes",
        content=response
    )

@router.post("/excuse")
async def generate_excuse(target: Target) -> Plan:
    response = get_completion(get_excuse(target))
    return Plan(
        name="When you say something wrong",
        content=response
    )


