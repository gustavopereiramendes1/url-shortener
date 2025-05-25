from pydantic import BaseModel, Field

class Url(BaseModel):
    originalUrl : str
    shortUrl: str = Field(unique=True)
    
class UrlRequest(BaseModel):
    originalUrl: str