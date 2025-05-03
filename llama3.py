import subprocess

prompt = input("llama3> ")
result = subprocess.run(['ollama', 'run', 'llama3'], input=prompt.encode(), stdout=subprocess.PIPE)
print(result.stdout.decode())
