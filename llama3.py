import subprocess

prompt = "What's the capital of France?"
result = subprocess.run(['ollama', 'run', 'llama3'], input=prompt.encode(), stdout=subprocess.PIPE)
print(result.stdout.decode())
