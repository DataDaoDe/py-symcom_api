from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import app.services.derivatives as dx

app = FastAPI()

allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DerivativeRequest(BaseModel):
    formula: str
    nth_derivative: Optional[int] = 1 

@app.post("/take_derivative")
async def take_derivative(derivative_request: DerivativeRequest = Body(..., embed=True)):
    formula = derivative_request.formula
    nth_deriv = derivative_request.nth_derivative
    expression = dx.from_latex(formula)
    symbolic_result = dx.take_derivative(expression, nth_deriv)
    latex_result = dx.to_latex(symbolic_result)

    return {
        'result' : latex_result
    }