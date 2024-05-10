'''pydantic is a library used primarily for data validation
and settings management using Python type annotations.
The BaseModel class is a central feature of this library,
enabling you to create data models where types and constraints are
defined using Python's standard type hints.'''
from pydantic import BaseModel


class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float