from datetime import datetime

from pydantic import BaseModel


class QueryRequest(BaseModel):
    query_name: str = ""
    query_params: dict = {}


class SearchCriteriaRequest(BaseModel):
    version: str = "1.0.0"
    reg_type: str = ""
    reg_sub_type: str = ""
    query_type: str = "graphql"
    query: str = ""


class SingleSearchRequest(BaseModel):
    reference_id: str = ""
    timestamp: datetime = datetime.now()
    search_criteria: SearchCriteriaRequest
    locale: str = "en"


class MessageRequest(BaseModel):
    transaction_id: str = ""
    search_request: list[SingleSearchRequest]


class PaginationResponse(BaseModel):
    page_size: int | None = None
    page_number: int | None = None
    total_count: int = None


class QueryDataResponse(BaseModel):
    version: str = "1.0.0"
    reg_type: str | None = None
    reg_sub_type: str | None = None
    reg_record_type: str | None = None
    reg_records: dict = {}


class SingleSearchResponse(BaseModel):
    reference_id: str | None = None
    timestamp: datetime = datetime.now()
    status: str
    status_reason_code: str | None = None
    status_reason_message: str | None = None
    data: QueryDataResponse
    pagination: PaginationResponse | None = {}
    locale: str = "en"


class MessageResponse(BaseModel):
    transaction_id: str
    correlation_id: str | None = None
    search_response: list[SingleSearchResponse]
