DEFAULT_SCENARIO_CLASSIFICATION_TMPL = (
    "The sceario is {scenario} with tabular data. "
    "We first provide sample description contains columns and corresponding values, " 
    "and then we provide labels the sample may belong to.\n"
    "-----------sample description-----------\n"
    "{sample_description}\n"
    "-----------labels-----------\n"
    "{labels}\n"
    "---------------------\n"
    "Using the sample description above and your knowledge, return the label that "
    "is most relevant to the sample.\n"
    "Provide label in the following format: 'ANSWER: <label>' and explain why "
    "this label was selected.\n"
)

DEFAULT_SCENARIO_REGRESSION_TMPL = (
    "The sceario is {scenario} with tabular data. "
    "We first provide sample description contains columns and corresponding values, " 
    "and then we provide context information to define a regression task.\n"
    "-----------sample description-----------\n"
    "{sample_description}\n"
    "-----------context information-----------\n"
    "{context_info}\n"
    "---------------------\n"
    "Using the sample description above and your knowledge, return a value that "
    "is most possible to the sample.\n"
    "Provide value in the following format: 'ANSWER: <value>' and explain why "
    "this value was predicted.\n"
)

DEFAULT_SCENARIO_EXPLANATION_TMPL = (
    "The sceario is {scenario} with tabular data. "
    "We will provide sample description contains columns and corresponding values\n" 
    "-----------sample description-----------\n"
    "{sample_description}\n"
    "---------------------\n"
    "read the sample description above and use your knowledge"
    "to perform interpretative enhancement of the sample." 
    "To make it more detailed, contents can include background information, highlight potential impacts and so on.\n"
    "Provide value in the following format: 'ANSWER: <explanation>'\n"
)


