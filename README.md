<p align="center">
    <img src="./docs/source/temp_logo_hq.png" width="500">
</p>

creVass is about APPLIED intelligence of plumbers.

* The same changes were required again and again to refactor code written by data scientists to make it ready for serving e.g. no standard way to run scripts, no standard way to handle configuration and no standard pipeline architecture.
* Existing model serving solutions focus on serving the model rather than serving an end-to-end solution. Our machine learning projects require multiple models and glue code to tie these models together.
* Existing serving approaches do not allow for the evolution of a machine learning pipeline without re-engineering the solution i.e. using a cloud API for the first release before training a custom model much later on.
* Code was commonly being commented out to run other branches as experimentation was not a first class citizen in the code being written.


## Simple usage

A short explanation is provided in the hello-world example's [README](examples/hello-world/) file.
```python
import logging
from surround import State, Stage, Estimator, Assembler, RunMode

class HelloWorld(Estimator):
    def estimate(self, state, config):
        state.text = "Hello world"

    def fit(self, state, config):
        print("No training implemented")

class InputValidator(Stage):
    def operate(self, state, config):
        if state.text:
            raise ValueError("'text' is not None")

class AssemblerState(State):
    text = None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data = AssemblerState()
    assembler = Assembler("Hello world example").set_stages([InputValidator(), HelloWorld()])
    assembler.run(data, mode=RunMode.PREDICT)
    print("Text is '%s'" % data.text)
```

## Examples

See the [examples](https://github.com/dstil/surround/tree/master/examples) directory for useful examples on how Surround can be utilized.

## Full Documentation
See [our website](https://surround.readthedocs.io/) for an in-depth explanation of Surround (in the About page), a Getting Started Guide, and full documentation of the API.

## Contributing

For guidance on setting up a development environment and how to make a contribution to Surround, see the [contributing guidelines](docs/CONTRIBUTING.md).


## License

Surround is released under a [BSD-3](https://opensource.org/licenses/BSD-3-Clause) license.

## Project Status
Surround is currently under **heavy** development, please submit any issues that occur or suggestions you may have, it is very much appreciated!
