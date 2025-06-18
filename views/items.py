from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr

router = APIRouter(prefix="/items", tags=["Items"])


class ItemCreate(BaseModel):
    name: constr(min_length=1, max_length=30)


class Item(BaseModel):
    id: int
    name: str


# In‑memory storage
items: dict[int, Item] = {}
_next_id = 1


@router.get("/", response_model=list[Item])
def items_list():
    return list(items.values())


@router.post("/", response_model=Item, status_code=201)
def create_item(item_in: ItemCreate):
    global _next_id
    item = Item(id=_next_id, name=item_in.name)
    items[_next_id] = item
    _next_id += 1
    return item


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
