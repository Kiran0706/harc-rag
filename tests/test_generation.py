from harc_rag.generation.ollama import OllamaLLM


def test_create_llm():

    llm = OllamaLLM(model="qwen2.5:3b")

    assert llm.model == "qwen2.5:3b"