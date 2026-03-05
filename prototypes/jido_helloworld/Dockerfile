FROM elixir:1.17-alpine

RUN apk add --no-cache build-base git

WORKDIR /app

# Install hex + rebar
RUN mix local.hex --force && \
    mix local.rebar --force

COPY mix.exs .
# Pre-fetch deps to speed up rebuilds
RUN mix deps.get

COPY . .

CMD ["iex", "-S", "mix"]
