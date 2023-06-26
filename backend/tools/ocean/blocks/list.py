from langchain.tools import StructuredTool
from pydantic import BaseModel, Field

from ..utils import getOcean


class ToolInputSchema(BaseModel):
    limit: int = Field(..., description="Number of blocks to list")


def list(limit: int) -> str:
    return getOcean().blocks.list(limit)


description = """Lists the latest blocks with the corresponding information."""

blocksListTool = StructuredTool(
    name="list_latest_blocks",
    description=description,
    func=list,
    args_schema=ToolInputSchema,
)
