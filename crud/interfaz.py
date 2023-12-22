from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Select, Static, Input, Label, TextArea
from textual import on
import mysql.connector
#stilos para botones ->'default', 'error', 'primary', 'success', or 'warning'
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

class ConexionSQL(App):
    BINDINGS = [("|", "cambiar_tema", "Cambia el tema de pantalla")]
    CSS_PATH = 'estilos.tcss'
    def compose(self) -> ComposeResult:
        yield Conexiones()
        yield Header(show_clock=True)
        yield Footer()

    def action_cambiar_tema(self) -> None:
        self.dark = not self.dark
    
class Conexiones(Static):
    def compose(self) -> ComposeResult:
        yield Button("Conectar", id="conexion", variant="success")
        yield Button("Desconectar", id="desconectar", variant="error")

        yield Label("Usuario:")
        user_ = yield Input("root", id="user_")
        self.user_  = user_
        yield Label("Contraseña:")
        pass_= yield Input("1221",id="pass_", password=True) 
        self.pass_ = pass_
        yield Label("Host:")
        host_ = yield Input("127.0.0.1",id="host_")
        self.host_ = host_
        yield Label("Base de datos:")
        database_ = yield Input("northwind",id="database_")
        self.database_  = database_ 
        yield Label("Consulta")
        yield TextArea(query, language="python")
        yield Button("Realizar consulta", id="consultar", variant="warning")

    @on(Button.Pressed, "#conexion")
    def conectar(self):
        try:
            self.cnx = mysql.connector.connect(
                user=self.user_
                , password=self.pass_
                , host=self.host_
                , database=self.database_
            )
            yield Label("Conectado a MySQL")
        except mysql.connector.Error as e:
            yield Label(f"Error al conectar: {e}")
        

    @on(Button.Pressed, "#desconectar")
    def desconectar(self):
        try:
            self.cnx.close()
            yield Label("Se cerró")
        except mysql.connector.Error as e:
            yield Label(str(e))
            
    @on(Button.Pressed, "consultar")
    def consultar(self):
        try:
            cursor = self.cnx.cursor()
            cursor.execute(query)
        except mysql.connector.Error as err:
            yield Label(str(err))

if __name__ == "__main__":
    app = ConexionSQL()
    app.run()
