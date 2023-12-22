from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Select, Static, Input, Label, TextArea, DataTable, Log, OptionList
from datetime import datetime
from textual import on
import mysql.connector
from rich.console import Console
from textual.containers import ScrollableContainer, Container



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
        #yield TextArea(querys, language="python")
        yield Button("Realizar consulta", id="consultar", variant="warning")

class ConexionSQL(App):
    
    def __init__(self):
        super().__init__()
        super().__init__()
        self.user_ = Input("root")
        self.pass_ = Input("1221", id="pass_", password=True)
        self.host_ = Input("127.0.0.1", id="host_")
        self.database_ = Input("northwind", id="database_")
        #self.querys = querys #TextArea(querys, language="python")
        self.cnx = None
        self.log_ = Log()
        self.tabla = DataTable()
        self.tabla.zebra_stripes = True
        self.opciones = OptionList("Conectate primero")

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
        yield Label("Menú de tablas")
        #yield self.querys
        yield self.opciones
        
        yield Container(
                Button("Realizar consulta", id="consultar", variant="warning"),
                
            )
        yield self.tabla

    @on(Button.Pressed, "#conexion")
    def conectar(self):
        try:
            #actualizar datos?
            self.cnx = mysql.connector.connect(user= self.user_.value, password = self.pass_.value, host = self.host_.value, database = self.database_.value)
            self.log_.write_line(datetime.now().strftime("%Y-%m-%d %H:%M:%S") +  "\tConexión exitosa")
            
            cursor = self.cnx.cursor()
            cursor.execute("SHOW TABLES;")
            self.opciones.clear_options()
            tables = [table[0] for table in cursor.fetchall()]
            for table in tables:
                self.opciones.add_option(table)       
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
            self.log_.write_line(f'''{self.opciones.OptionSelected[0]}''')
            
            self.log_.write_line("Consulta realizada con éxito")
        except:
            self.log_.write_line("Error al hacer la consulta ¿Te conectaste wei o no compila tu código?")
            self.log_.write_line(f'''{self.opciones.OptionSelected}''')

if __name__ == "__main__":
    app = ConexionSQL()
    app.run()
    