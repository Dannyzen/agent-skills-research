# run_helloworld.exs
alias JidoHelloworld.HelloAgent
alias JidoHelloworld.Actions.OllamaChat

IO.puts("🤖 Starting Jido Hello World Prototype...")

ollama_url = System.get_env("OLLAMA_URL") || "http://sovereign-llm:11434"
model = System.get_env("MODEL_NAME") || "llama3"

# 1. Warm up Ollama with a simple prompt
IO.puts("🔥 Warming up Ollama (Model: #{model})...")
try do
  case Req.post("#{ollama_url}/api/generate", 
    json: %{model: model, prompt: "hi", stream: false}, 
    receive_timeout: 120_000
  ) do
    {:ok, %{status: 200}} -> IO.puts("✅ Ollama is warm and ready.")
    {:ok, %{status: status, body: body}} -> IO.puts("⚠️ Ollama returned #{status}: #{inspect(body)}")
    {:error, reason} -> IO.puts("❌ Ollama connection failed: #{inspect(reason)}")
  end
rescue
  e -> IO.puts("❌ Error during warmup: #{inspect(e)}")
end

# 2. Call the Action directly to bypass Jido's default 5s Workflow timeout
# This still uses the Jido Action module structure.
params = %{prompt: "Say 'Hello from the BEAM!' in a very robot-like way."}

IO.puts("\n🧠 Calling Jido Action directly (Bypassing 5s Workflow timeout)...")
case OllamaChat.run(params, %{}) do
  {:ok, %{last_response: response}} ->
    IO.puts("\n✅ Success!")
    IO.puts("Agent Response: #{response}")
    
    # Update an agent struct manually to show we have the state
    agent = HelloAgent.new()
    agent = %{agent | state: %{last_response: response}}
    IO.puts("\nFinal Agent State: #{inspect(agent.state)}")

  {:error, reason} ->
    IO.puts("\n❌ Action Error: #{inspect(reason)}")

  other ->
    IO.puts("\n❓ Unexpected return format:")
    IO.inspect(other)
end
