from fastmcp import FastMCP
import chess

mcp = FastMCP("Chess MCP")

BOARD = chess.Board()

@mcp.tool
def get_board(fen_format:bool=False) -> str:
    """Get the current state of the chess board."""
    return BOARD.fen() if fen_format else BOARD

@mcp.tool
def make_move(san_move: str) -> str:
    """Make a move on the chess board using standard algebraic notation."""
    try:
        BOARD.push_san(san_move)
    except chess.InvalidMoveError:
        return f"{san_move} is not a valid move; please provide a valid move in standard algebraic notation."
    except chess.IllegalMoveError:
        return f"{san_move} is an illegal move; please provide a legal move in standard algebraic notation."
    except chess.AmbiguousMoveError:
        return f"{san_move} is an ambiguous move; please provide a disambiguated move in standard algebraic notation."
    return f"Move {san_move} has been made. Current board state: {BOARD.fen()}"

@mcp.tool
def get_legal_moves() -> str:
    """Get all legal moves from the current position."""
    legal_moves = [move.uci() for move in BOARD.legal_moves]
    if not legal_moves:
        return "There are no legal moves available."
    return f"Legal moves: {', '.join(legal_moves)}"

@mcp.tool
def reset_board() -> str:
    """Reset the chess board to the starting position."""
    global BOARD
    BOARD = chess.Board()
    return "The chess board has been reset to the starting position."

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000, path="/mcp")