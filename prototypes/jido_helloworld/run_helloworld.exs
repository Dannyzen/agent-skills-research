# run_helloworld.exs
# Run with: mix run run_helloworld.exs

alias JidoHelloworld.HelloAgent
alias JidoHelloworld.Actions.OllamaChat

IO.puts("🤖 Starting Jido Hello World Prototype...")

# 1. Initialize the Agent
agent = HelloAgent.new()

# 2. Define the Action with params
action = {OllamaChat, %{prompt: "Say 'Hello from the BEAM!' in a very robot-like way."}}

# 3. Execute the command on the agent
# cmd/2 returns {updated_agent, directives}
IO.puts("🧠 Agent thinking...")
{agent, _directives} = HelloAgent.cmd(agent, action)

# 4. Display the results
IO.puts("\n--- Agent Result ---")
IO.puts("Last Response: #{agent.state.last_response}")
IO.puts("--------------------\n")
