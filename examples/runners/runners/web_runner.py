import logging
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel # pylint: disable=E0611
from surround import Runner, RunMode
from .stages import AssemblyState

app = FastAPI() # pylint: disable=C0103

# Global variable to store the assembler instance (so FastAPI endpoint handlers can access it).
assembler = None # pylint: disable=C0103

logging.basicConfig(level=logging.INFO)


class WebRunner(Runner):

    def load_data(self, mode, config):
        return None

    def run(self, mode=RunMode.PREDICT):
        self.assembler.init_assembler()
        global assembler # pylint: disable=C0103, W0603

        # Get the Config instance from the Assembler.
        assembler = self.assembler
        uvicorn.run(
            app, port=8080, log_level="info"
        )


class EstimateBody(BaseModel): # pylint: disable=R0903
    message: str


@app.post("/message")
def post_message(body: EstimateBody):
    # Prepare input_data for the assembler
    data = AssemblyState()
    data.output_data = ""
    data.input_data = body.message

    # Execute assembler
    assembler.run(data)
    logging.info("Message: %s", data.output_data)
    return {"output": data.output_data}


@app.get("/info")
def get_info():
    return {"version": "0.0.1"}
