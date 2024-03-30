from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from api.schema import ResponseSchema, RegisterSchema, CompleteRegisterSchema, CompleteActivationSchema, LoginSchema, ForgotPasswordSchema
from api.v1.services.authentication import Authentication

router = APIRouter(prefix="/api/v1/auth", tags=['Authentication'])


@router.get("/load")
async def load():
    result = await Authentication.load()
    response = JSONResponse(content=result)
    return response


@router.get("/root")
async def root():
    result = await Authentication.root()
    response = JSONResponse(content=result)
    return response


@router.post("/register")
async def register(request_body: RegisterSchema):
    result = await Authentication.register(request_body)
    response = JSONResponse(content=result)
    return response


@router.post("/complete")
async def register(request_body: CompleteRegisterSchema):
    result = await Authentication.complete(request_body)
    response = JSONResponse(content=result)
    return response


@router.post("/activation")
async def register(request_body: CompleteActivationSchema):
    result = await Authentication.activation(request_body)
    response = JSONResponse(content=result)
    return response


@router.post("/login")
async def login(request_body: LoginSchema):
    result = await Authentication.login(request_body)
    refreshToken = result["refreshToken"]
    del result['refreshToken']
    response = JSONResponse(content=result)
    response.set_cookie(key="jwt", value=refreshToken)
    return response


@router.post("/refresh")
async def refresh(request: Request):
    cookies = request.cookies.get("jwt")
    if cookies is None:
        raise HTTPException(
            status_code=401, detail="Invalid password!")
    result = await Authentication.refresh(cookies)
    response = JSONResponse(content=result)
    return response


@router.post("/forgot", response_model=ResponseSchema, response_model_exclude_none=True)
async def forgotPassword(request_body: ForgotPasswordSchema):
    result = await Authentication.forgetPassword(request_body)
    return ResponseSchema(status=1, message="Successfully update data!", result=result)
