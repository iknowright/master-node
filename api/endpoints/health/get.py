from fastapi.responses import PlainTextResponse

# Document for generating custom response
# References: https://fastapi.tiangolo.com/advanced/additional-responses
DOC = {
    200: {
        "description": "Normal response",
        "content": {"text/plain": {"example": "OK"}},
    }
}


def get():
    return PlainTextResponse("OK", 200)
