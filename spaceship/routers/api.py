from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

import numpy as np

@router.get("/matrix")
def get_matrix():
    matrix_a = np.random.rand(10, 10)
    matrix_b = np.random.rand(10, 10)
    product = np.dot(matrix_a, matrix_b)
    return {"matrix_a": matrix_a.tolist(), "matrix_b": matrix_b.tolist(), "product": product.tolist()}
