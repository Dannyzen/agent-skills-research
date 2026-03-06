defmodule JidoHelloworld.Application do
  @moduledoc false
  use Application

  def start(_type, _args) do
    children = [
      {Phoenix.PubSub, name: JidoHelloworld.PubSub},
      # The HelloAgent Server is started under our own supervision tree
      {Jido.Agent.Server, [
        agent: JidoHelloworld.HelloAgent.new(),
        pubsub: JidoHelloworld.PubSub,
        name: "hello_agent_v1"
      ]}
    ]

    opts = [strategy: :one_for_one, name: JidoHelloworld.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
