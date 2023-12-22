from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Select, Static, Input, Label, TextArea, DataTable
from textual import on
import mysql.connector
from rich.console import Console
from textual.containers import ScrollableContainer, Container

query = """SELECT
	p.ProductID
    , p.ProductName
    , CHAR_LENGTH(p.ProductName) AS tamaño
FROM 
	products p
WHERE 
	CHAR_LENGTH(p.ProductName) = 7
;
"""
class conect(Static):
    def compose(self) ->ComposeResult:
        yield Button("Conectar", id="conexion", variant="success")
        yield Button("Desconectar", id="desconectar", variant="error")

class datos(Static):
    def compose(self) -> ComposeResult:
        yield Label("Usuario:")
        user_ = yield Input("root", id="user_")
        yield Label("Contraseña:")
        pass_= yield Input("1221",id="pass_", password=True) 
        yield Label("Host:")
        host_ = yield Input("127.0.0.1",id="host_")
        yield Label("Base de datos:")
        database_ = yield Input("northwind",id="database_")

class consultas(Static):
    def compose(self) -> ComposeResult:
        yield Label("Consulta")
        yield TextArea(query, language="python")
        yield Button("Realizar consulta", id="consultar", variant="warning")

class ConexionSQL(App):
    
    def __init__(self):
        super().__init__()
        self.user_ = None
        self.pass_ = None
        self.host_ = None
        self.database_ = None
        self.cnx = None

    BINDINGS = [("|", "cambiar_tema", "Cambia el tema de pantalla")]
    
    CSS_PATH = 'estilos.css'
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield ScrollableContainer (conect())
        yield ScrollableContainer(
            Container(
                Label("Usuario:"),
                Input("root", id="user_"),
                Label("Contraseña:"),
                Input("1221", id="pass_", password=True),
                Label("Host:"),
                Input("127.0.0.1", id="host_"),
                Label("Base de datos:"),
                Input("northwind", id="database_"),
            )
        )
        yield ScrollableContainer (consultas())
        yield DataTable()

    @on(Button.Pressed, "#conexion")
    def conectar(self):
        try:
            #actualizar datos?
            self.cnx = mysql.connector.connect(user= self.user_, password = self.pass_, host = self.host_, database = self.database_)
        except mysql.connector.Error as e:
            1#yield Label(f"Error al conectar: {e}")

    @on(Button.Pressed, "#desconectar")
    def desconectar(self):
        try:
           self.cnx.close()
        except mysql.connector.Error as e:
            yield Label(str(e))

    @on(Button.Pressed, "#consultar")
    def realizar_consulta(self):
        try:
            cursor = self.cnx.cursor()

            cursor.execute(TextArea.text)
        except mysql.connector.Error as err:
            yield Label(str(err))

if __name__ == "__main__":
    app = ConexionSQL()
    app.run()
    