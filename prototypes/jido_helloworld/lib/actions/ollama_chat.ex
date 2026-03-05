defmodule JidoHelloworld.Actions.OllamaChat do
  use Jido.Action,
    name: "ollama_chat",
    description: "Calls local Ollama instance for a response",
    schema: [
      prompt: [type: :string, required: true]
    ]

  def run(params, _context) do
    ollama_url = System.get_env("OLLAMA_URL") || "http://sovereign-llm:11434"
    model = System.get_env("MODEL_NAME") || "llama3"

    IO.puts("📡 Jido calling Ollama at #{ollama_url} with model #{model}...")

    case Req.post("#{ollama_url}/api/generate", json: %{
      model: model,
      prompt: params.prompt,
      stream: false
    }) do
      {:ok, %{status: 200, body: body}} ->
        response = body["response"]
        {:ok, %{last_response: response}}

      {:ok, %{status: status}} ->
        {:error, "Ollama returned status #{status}"}

      {:error, reason} ->
        {:error, "Ollama connection failed: #{inspect(reason)}"}
    end
  end
end
