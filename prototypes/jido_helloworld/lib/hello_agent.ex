defmodule JidoHelloworld.HelloAgent do
  use Jido.Agent,
    name: "hello_agent",
    description: "A simple Jido agent that says hello via Ollama",
    schema: [
      last_response: [type: :string, default: ""]
    ],
    actions: [
      JidoHelloworld.Actions.OllamaChat
    ]
end
