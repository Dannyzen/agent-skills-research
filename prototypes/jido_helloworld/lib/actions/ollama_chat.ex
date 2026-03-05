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
    full_url = "#{ollama_url}/api/generate"

    IO.puts("📡 Action started. Jido calling Ollama at #{full_url}...")

    case Req.post(full_url, 
      json: %{
        model: model,
        prompt: params.prompt,
        stream: false
      },
      receive_timeout: 300_000
    ) do
      {:ok, %{status: 200, body: body}} ->
        IO.puts("✅ Ollama responded successfully.")
        {:ok, %{last_response: body["response"]}}

      {:ok, %{status: status, body: body}} ->
        {:error, "Ollama returned status #{status}: #{inspect(body)}"}

      {:error, reason} ->
        {:error, "Ollama connection failed: #{inspect(reason)}"}
    end
  end
end
