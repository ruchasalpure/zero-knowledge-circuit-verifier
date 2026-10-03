from crewai import Agent

zero_knowledge_circuit_verifier = Agent(
    role="Zero Knowledge Circuit Verifier",
    goal="Deliver high-precision autonomous Zero Knowledge Circuit Verifier operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
