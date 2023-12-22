from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Select, Static, Input, Label, TextArea, DataTable, Log
from textual import on
import mysql.connector
from rich.console import Console
from textual.containers import ScrollableContainer, Container

querys = """SELECT
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
        yield TextArea(querys, language="python")
        yield Button("Realizar consulta", id="consultar", variant="warning")

class ConexionSQL(App):
    
    def __init__(self):
        super().__init__()
        super().__init__()
        self.user_ = Input("root")
        self.pass_ = Input("1221", id="pass_", password=True)
        self.host_ = Input("127.0.0.1", id="host_")
        self.database_ = Input("northwind", id="database_")
        self.querys = TextArea(querys, language="python")
        self.cnx = None
        self.log_ = Log()

    BINDINGS = [("|", "cambiar_tema", "Cambia el tema de pantalla")]
    
    CSS_PATH = 'estilos.css'
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield ScrollableContainer (conect())
        yield Label("Usuario:")
        yield self.user_        
        yield Label("Contraseña:")
        yield self.pass_
        yield Label("Host:")
        yield self.host_
        yield Label("Base de datos:")
        yield self.database_
        yield self.log_
        yield Label("Consulta")
        yield self.querys
        yield Button("Realizar consulta", id="consultar", variant="warning")
        yield DataTable()

    @on(Button.Pressed, "#conexion")
    def conectar(self):
        try:
            #actualizar datos?
            self.cnx = mysql.connector.connect(user= self.user_.value, password = self.pass_.value, host = self.host_.value, database = self.database_.value)
            self.log_.write_line("Conexión exitosa")
        except mysql.connector.Error as e:
            self.log_.write_line("Error al conectarse")

    @on(Button.Pressed, "#desconectar")
    def desconectar(self):
        try:
           self.cnx.close()
           self.log_.write_line("Se desconectó")
        except mysql.connector.Error as e:
            self.log_.write_line("Hubo un pedo")

    @on(Button.Pressed, "#consultar")
    def realizar_consulta(self):
        try:
            cursor = self.cnx.cursor()
            cursor.execute(self.querys.text)
            column_names = [column[0] for column in cursor.description]
            self.log_.write_line(", ".join(column_names))
            # Iterar sobre las filas y agregarlas al log
            for row in cursor:
                self.log_.write_line(", ".join(str(value) for value in row))
            self.log_.write_line("Consulta realizada con éxito")
        except mysql.connector.Error as err:
            self.log_.write_line("hubo pedo")

if __name__ == "__main__":
    app = ConexionSQL()
    app.run()
    