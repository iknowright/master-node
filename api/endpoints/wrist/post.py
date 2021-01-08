from fastapi.responses import PlainTextResponse

# Document for generating custom response
# References: https://fastapi.tiangolo.com/advanced/additional-responses
DOC = {
    201: {
        "description": "Created",
        "content": {"text/plain": {"example": "OK"}},
    }
}


def post():
    return PlainTextResponse("OK", 201)
