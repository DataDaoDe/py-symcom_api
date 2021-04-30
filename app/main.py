from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator
from typing import Optional
import app.services.derivatives as dx
import app.services.integrals as integrals
import app.services.latex as latex

app = FastAPI(
    title="QuantU Symbolic Computation Engine",
    description="This project provides symbolic computational services to quantu applications",
    version="0.1.0"
)

allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NthDerivativeRequest(BaseModel):
    formula: str
    nth_derivative: Optional[int] = 1

    @validator('nth_derivative')
    def nth_derivative_must_be_nonnegative(cls, v):
        if v and v < 0:
            raise ValueError('derivatives must be nonnegative')
        return v


@app.post("/nth_derivative_of")
async def nth_derivative_of(
    data: NthDerivativeRequest = Body(..., embed=True)
):
    formula, nth_deriv = data.formula, data.nth_derivative
    expression = latex.from_latex(formula)

    symbolic_result = dx.find_nth_derivative_of(expression, nth_deriv)

    latex_result = latex.to_latex(symbolic_result)

    return {
        'result' : latex_result
    }


class IndefiniteIntegralRequest(BaseModel):
    formula: str

@app.post("/indefinite_integral")
async def indefinite_integral_of(
    data: IndefiniteIntegralRequest = Body(..., embed=True)
):
    formula = data.formula
    expression = latex.from_latex(formula)

    symbolic_result = integrals.find_integral_of(expression)

    latex_result = latex.to_latex(symbolic_result)

    return {
        'result' : latex_result
    }