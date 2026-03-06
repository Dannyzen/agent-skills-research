defmodule JidoHelloworld.MixProject do
  use Mix.Project

  def project do
    [
      app: :jido_helloworld,
      version: "0.1.0",
      elixir: "~> 1.17",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  def application do
    [
      extra_applications: [:logger],
      mod: {JidoHelloworld.Application, []}
    ]
  end

  defp deps do
    [
      {:jido, "~> 1.0.0"},
      {:req, "~> 0.5.0"}
    ]
  end
end
