# run_helloworld.exs
alias JidoHelloworld.HelloAgent
alias JidoHelloworld.Actions.OllamaChat

IO.puts("🤖 Starting Jido Hello World Prototype (Supervised Edition)...")

# 1. Warm up Ollama
ollama_url = System.get_env("OLLAMA_URL") || "http://sovereign-llm:11434"
model = System.get_env("MODEL_NAME") || "llama3"

IO.puts("🔥 Warming up Ollama (Model: #{model})...")
try do
  case Req.post("#{ollama_url}/api/generate", 
    json: %{model: model, prompt: "hi", stream: false}, 
    receive_timeout: 120_000
  ) do
    {:ok, %{status: 200}} -> IO.puts("✅ Ollama is warm and ready.")
    _ -> IO.puts("⚠️ Warmup check failed, continuing anyway...")
  end
rescue
  _ -> IO.puts("❌ Warmup connection failed, continuing anyway...")
end

# The server name we configured in Application.ex
server_name = "hello_agent_v1"
registry = Jido.AgentRegistry
server_via = {:via, Registry, {registry, server_name}}

params = %{prompt: "Say 'Hello from the supervised AgentServer!' in a very robot-like way."}

IO.puts("\n🧠 Calling Jido AgentServer via GenServer.call (Formal Workflow)...")
IO.puts("⏳ This uses our patched 300s timeout.")

case Jido.Agent.Server.cmd(server_via, {OllamaChat, params}) do
  {:ok, server_state} ->
    IO.puts("\n✅ Success!")
    
    agent = server_state.agent
    last_response = agent.state[:last_response]
    
    if last_response do
      IO.puts("\n🤖 Robot says: #{last_response}")
    else
      IO.puts("\n⚠️ No response found in agent state.")
      IO.inspect(agent.state, label: "Agent State")
    end

    IO.puts("\nFinal Agent State: #{inspect(agent.state)}")

  {:error, reason} ->
    IO.puts("\n❌ Server Error: #{inspect(reason)}")
end
