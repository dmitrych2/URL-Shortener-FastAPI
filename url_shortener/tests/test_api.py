from httpx import AsyncClient

async def text_generate_alug(ac: AsyncClient):
    result = await ac.post("/short_url", json={"long_url": "https://my-site.com"})
    assert result.status_code == 200