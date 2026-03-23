import os
from dotenv import load_dotenv
from langchain_aws import BedrockEmbeddings, ChatBedrockConverse

# Load environment variables from .env file
load_dotenv()

embeddings = BedrockEmbeddings(
    model_id=os.getenv("BEDROCK_EMBEDDING_MODEL_ID", "amazon.titan-embed-text-v2:0"),
    region_name=os.getenv("AWS_REGION", "us-east-1")
)
llm = ChatBedrockConverse(
    model=os.getenv("BEDROCK_MODEL_ID", "global.anthropic.claude-haiku-4-5-20251001-v1:0"),
    region_name=os.getenv("AWS_REGION", "us-east-1")
)