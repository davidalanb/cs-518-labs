A 500 error is a server error.  
When you're running your FastAPI (port 8000), you will see error output.
However, when you're running the app through Azure Functions (port 7071), you won't.

This can be a problem if you have a server error that only occurs in your deployed instance, not the local one.
(For example, an error related to different versions of dependencies installed on your machine vs. specified in requirements.txt)
If you go to your Function App > Monitoring > Logs, you won't see helpful information.

In order to show the error information in your Logs, you will need to insert the code below into main.py


```python
import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

# Create a logger instance for your app
logger = logging.getLogger('FastAPILogger')

# This is an example to show how to catch and log
# unhandled exceptions at the FastAPI level.
@app.exception_handler(Exception)
async def unhandled_exception_handler(request, exc: Exception):
    # Log the full traceback before returning the 500
    logger.exception("FATAL UNHANDLED EXCEPTION in FastAPI route", exc_info=True)
    
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )
```