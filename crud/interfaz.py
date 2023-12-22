from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Select, Static
from textual import on
import mysql.connector
LINES = """Ventas
Compras
Vendedor
... """.splitlines()

class ConeccionSQL(App):
    BINDINGS = [("|", "cambiar_tema", "Cambia el tema de pantalla")]
    def compose(self) -> ComposeResult:
        yield Conecciones()
        yield Header(show_clock=True)
        yield Footer()
    def action_cambiar_tema(self) -> None:
        self.dark = not self.dark
    
class Conecciones(Static):
    def compose(self) -> ComposeResult:
        yield Button("Conectar", id="conexion", variant="error")
        yield Button("Desconectar", id="desconectar", variant="error")
        yield Select((line, line) for line in LINES)
    
    @on(Button.Pressed, "#desconectar")
    def a_method(self):
        print(f"Botón presionado: {self.id}")
    

if __name__ == "__main__":
    app = ConeccionSQL()
    app.run()
