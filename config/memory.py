"""
memory configuration file.this file is used to configure the memory setting for the application.
"""
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

#short term memory configuration
checkpointer= InMemorySaver()
#long term memory configuration
store = InMemoryStore()