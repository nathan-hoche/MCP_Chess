# MCP Chess ♟️

# Introduction

This project is a simple MCP to enable an LLM to play chess. It uses the `python-chess` library to handle the chess logic and a simple text-based interface for interaction.

> [!NOTE]
> The board is handle by the MCP, so the user need to interact with the chess game using an MCP client.

# Usage

To use this project, you will first need to install the required dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

Then, you can run the MCP server using:

```bash
python src/main.py
```

> [!NOTE]
> The MCP server use the `Streamable-http` for the communication, this can be changed in the `main.py` file.

>[!NOTE]
> You can check my repository [LLM Chess Game](https://github.com/nathan-hoche/LLM_Chess_Game), to see how to use this MCP with a language model (LLM) to play chess.

# List of tools

| Tool Name | Arguments | Description |
| --- | --- | --- |
| `get_board` | fen_format (Optional bool: To get the board in the fen format) | Get the current state of the chess board. |
| `make_move` | san_move (str: Move to make) | Make a move on the chess board. |
| `get_legal_moves` | None | Get the list of legal moves for the current player. |
| `check_game_status` | None | Get status of the game |
| `reset_board` | None | Restart the board |