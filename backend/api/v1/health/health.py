from fastapi import APIRouter
from sqlalchemy import text

from core.dependencies.session import AsyncSessionDep

router = APIRouter()


@router.get("/")
async def health_check(session: AsyncSessionDep):
    try:
        result = await session.execute(text("SELECT 1"))
        _ = result.scalar_one()
        return {"status": "healthy", "database": "up"}
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "down",
            "error": str(e),
        }
